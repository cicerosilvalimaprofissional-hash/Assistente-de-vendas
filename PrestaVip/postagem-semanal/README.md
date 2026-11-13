# Postagem semanal — PrestaVip

Gera links de postagem (WhatsApp, Facebook, X, Telegram, LinkedIn, Pinterest) para
**todos os produtos ativos** da loja e monta a postagem da semana.

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `config.json` | URL da loja, número de WhatsApp de vendas, UTMs, hashtags e chamada da postagem |
| `produtos.json` | Catálogo de produtos, sincronizado com o site da loja (`ativo: false` tira o produto da postagem) |
| `gerar_postagens.py` | Script que gera os links e a postagem |
| `links/links_produtos.csv` / `.md` | Todos os links de compartilhamento por produto |
| `postagens/AAAA-MM-DD.md` | Histórico das postagens semanais |

## Como usar

Loja: https://minha-loja-xvrw.onrender.com

- `python3 gerar_postagens.py --atualizar` lê todos os produtos do site, atualiza
  `produtos.json` e gera os links e a postagem.
- `python3 gerar_postagens.py` gera só a partir do `produtos.json` atual.

Produto novo no site entra sozinho na próxima postagem. Para tirar um produto da
postagem sem tirá-lo do site, mude `"ativo"` para `false` em `produtos.json`.

## Agendamento semanal

O workflow `.github/workflows/postagem-semanal.yml` roda **toda segunda-feira às 08:47
(Brasília)**, sincroniza os produtos com o site, gera os links, salva a postagem em `postagens/` e faz commit.
Também pode ser disparado manualmente em *Actions → Postagem semanal PrestaVip → Run workflow*.

### Publicação automática no Telegram (opcional)

1. Crie o bot no @BotFather e adicione-o como administrador do canal.
2. Em *Settings → Secrets and variables → Actions*, crie o segredo `TELEGRAM_BOT_TOKEN`
   com o token do bot.
3. Em `config.json`, preencha `telegram_canal` com `@nomedocanal` (ou o ID `-100...`
   de um canal privado).

Sem o token e o canal o workflow só gera e salva a postagem, sem publicar.
