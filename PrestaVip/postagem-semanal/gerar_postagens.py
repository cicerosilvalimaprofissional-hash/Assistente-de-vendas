#!/usr/bin/env python3
"""Gera links de postagem para todos os produtos da loja PrestaVip.

Uso:
    python3 gerar_postagens.py            # gera links e a postagem da semana
    python3 gerar_postagens.py --publicar # também envia ao Telegram (se configurado)

Saídas (nesta pasta):
    links/links_produtos.csv   - todos os links de compartilhamento por produto
    links/links_produtos.md    - mesma lista em formato legível
    postagens/AAAA-MM-DD.md    - texto pronto da postagem semanal

Publicação automática no Telegram usa as variáveis de ambiente
TELEGRAM_BOT_TOKEN e TELEGRAM_CHAT_ID (opcionais).
"""
import csv
import datetime as dt
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent
LIMITE_TELEGRAM = 4000


def carregar(nome):
    with open(BASE / nome, encoding="utf-8") as f:
        return json.load(f)


def url_produto(config, produto):
    url = produto["url"]
    if not url.startswith("http"):
        url = config["url_loja"].rstrip("/") + "/" + url.lstrip("/")
    partes = urllib.parse.urlsplit(url)
    query = dict(urllib.parse.parse_qsl(partes.query))
    query.update(config.get("utm", {}))
    query["utm_content"] = produto["id"]
    return urllib.parse.urlunsplit(partes._replace(query=urllib.parse.urlencode(query)))


def links_compartilhamento(config, produto):
    link = url_produto(config, produto)
    texto = f"{produto['nome']} por R$ {produto['preco']} na {config['nome_loja']}"
    q = urllib.parse.quote
    links = {
        "produto": link,
        "whatsapp": f"https://wa.me/?text={q(texto + ' ' + link)}",
        "facebook": f"https://www.facebook.com/sharer/sharer.php?u={q(link)}",
        "x_twitter": f"https://twitter.com/intent/tweet?text={q(texto)}&url={q(link)}",
        "telegram": f"https://t.me/share/url?url={q(link)}&text={q(texto)}",
        "linkedin": f"https://www.linkedin.com/sharing/share-offsite/?url={q(link)}",
        "pinterest": f"https://pinterest.com/pin/create/button/?url={q(link)}&description={q(texto)}",
    }
    numero = config.get("whatsapp_vendas", "").strip()
    if numero.isdigit() and numero.strip("0") not in ("", "55"):  # ignora o número de exemplo
        msg = f"Olá! Tenho interesse em: {produto['nome']} ({link})"
        links["whatsapp_vendedor"] = f"https://wa.me/{numero}?text={q(msg)}"
    return links


def gerar(config, produtos, hoje):
    ativos = [p for p in produtos if p.get("ativo", True)]
    linhas = []
    for p in ativos:
        linhas.append({"id": p["id"], "nome": p["nome"], "preco": p["preco"],
                       **links_compartilhamento(config, p)})

    colunas = sorted({k for l in linhas for k in l}, key=lambda c: (
        ["id", "nome", "preco", "produto"].index(c) if c in ("id", "nome", "preco", "produto") else 9, c))
    with open(BASE / "links" / "links_produtos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=colunas)
        w.writeheader()
        w.writerows(linhas)

    md = [f"# Links de postagem — {config['nome_loja']}", "",
          f"Atualizado em {hoje:%d/%m/%Y} · {len(linhas)} produtos ativos", ""]
    for l in linhas:
        md.append(f"## {l['nome']} — R$ {l['preco']}")
        md += [f"- **{k}**: {v}" for k, v in l.items() if k not in ("id", "nome", "preco")]
        md.append("")
    (BASE / "links" / "links_produtos.md").write_text("\n".join(md), encoding="utf-8")

    post = [config.get("chamada", ""), ""]
    for p in ativos:
        bloco = f"✅ {p['nome']} — R$ {p['preco']}"
        if p.get("descricao"):
            bloco += f"\n{p['descricao']}"
        bloco += f"\n👉 {url_produto(config, p)}"
        post += [bloco, ""]
    post.append(" ".join(config.get("hashtags", [])))
    texto = "\n".join(post).strip() + "\n"
    arquivo = BASE / "postagens" / f"{hoje:%Y-%m-%d}.md"
    arquivo.write_text(texto, encoding="utf-8")
    return texto, arquivo, len(linhas)


def dividir(texto, limite=LIMITE_TELEGRAM):
    partes, atual = [], ""
    for bloco in texto.split("\n\n"):
        if atual and len(atual) + len(bloco) + 2 > limite:
            partes.append(atual)
            atual = ""
        atual = f"{atual}\n\n{bloco}" if atual else bloco
    if atual:
        partes.append(atual)
    return partes


def publicar_telegram(texto):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat:
        print("Telegram não configurado (TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID); pulando publicação.")
        return
    for parte in dividir(texto):
        dados = urllib.parse.urlencode({"chat_id": chat, "text": parte,
                                        "disable_web_page_preview": "false"}).encode()
        req = urllib.request.Request(f"https://api.telegram.org/bot{token}/sendMessage", data=dados)
        with urllib.request.urlopen(req, timeout=30) as r:
            if r.status != 200:
                raise SystemExit(f"Falha ao publicar no Telegram: HTTP {r.status}")
    print("Postagem publicada no Telegram.")


def main():
    config, produtos = carregar("config.json"), carregar("produtos.json")
    texto, arquivo, total = gerar(config, produtos, dt.date.today())
    print(f"{total} produtos → {arquivo.relative_to(BASE)}")
    if "--publicar" in sys.argv:
        publicar_telegram(texto)


if __name__ == "__main__":
    main()
