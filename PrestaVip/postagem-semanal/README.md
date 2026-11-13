# Postagem semanal — PrestaVip

Gera links de postagem (WhatsApp, Facebook, X, Telegram, LinkedIn, Pinterest) para
**todos os produtos ativos** da loja e monta a postagem da semana.

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `config.json` | URL da loja, número de WhatsApp de vendas, UTMs, hashtags e chamada da postagem |
| `produtos.json` | Catálogo de produtos (`ativo: false` tira o produto da postagem) |
| `gerar_postagens.py` | Script que gera os links e a postagem |
| `links/links_produtos.csv` / `.md` | Todos os links de compartilhamento por produto |
| `postagens/AAAA-MM-DD.md` | Histórico das postagens semanais |

## Como usar

1. Edite `config.json` com a URL real da loja (`url_loja`) e o WhatsApp de vendas.
2. Cadastre os produtos em `produtos.json` (`url` pode ser caminho relativo ou URL completa).
3. Rode localmente: `python3 gerar_postagens.py`

## Agendamento semanal

O workflow `.github/workflows/postagem-semanal.yml` roda **toda segunda-feira às 08:47
(Brasília)**, gera os links, salva a postagem em `postagens/` e faz commit.
Também pode ser disparado manualmente em *Actions → Postagem semanal PrestaVip → Run workflow*.

### Publicação automática no Telegram (opcional)

Em *Settings → Secrets and variables → Actions*, crie:

- `TELEGRAM_BOT_TOKEN` — token do bot (via @BotFather)
- `TELEGRAM_CHAT_ID` — ID do canal/grupo (o bot precisa ser admin do canal)

Sem esses segredos o workflow só gera e salva a postagem, sem publicar.
