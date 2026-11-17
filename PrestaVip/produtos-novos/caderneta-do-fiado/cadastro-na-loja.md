# Caderneta do Fiado — cadastro na loja

**Preço sugerido:** R$ 24,90 (pagamento único)
**Selo:** Novo
**Capa:** `capa-caderneta-do-fiado.jpg` (800 × 800, mesmo formato das outras capas da loja)
**Arquivo para entregar ao cliente:** `caderneta-do-fiado.zip` (app + manual em PDF)

## Nome
Caderneta do Fiado — Controle de Vendas Fiado e Cobrança no WhatsApp

## Descrição
App para quem vende fiado: anote as compras de cada cliente, veja na hora quem está devendo e quem está atrasado, e cobre pelo WhatsApp com a mensagem pronta e a sua chave Pix. Funciona sem internet e sem mensalidade.

## Benefícios
- Saldo de cada cliente e total a receber na tela inicial
- Aviso de compra vencida, de vencimento próximo e de limite estourado
- Cobrança pronta no WhatsApp, com o saldo e a sua chave Pix
- Pagamento parcial abate as compras mais antigas primeiro
- Movimentos do mês, extrato do cliente e exportação para planilha
- Manual em PDF, passo a passo

## Aviso (linha pequena)
Abre no Chrome ou no Edge do computador e no Chrome do Android. Os dados ficam no navegador do aparelho; o manual explica o backup.

## Passo a passo para colocar na loja
1. No PagBank, crie um **link de pagamento** de R$ 24,90 com o nome "Caderneta do Fiado" e copie o link (`https://pag.ae/...`).
2. Envie a capa `capa-caderneta-do-fiado.jpg` para a pasta `/capas/` do site.
3. Cole o bloco HTML abaixo na lista de produtos do site, trocando `COLE_AQUI_O_LINK_DO_PAGBANK` pelo link do passo 1.
4. Quando o cliente mandar o comprovante no WhatsApp, envie o arquivo `caderneta-do-fiado.zip`.

Na segunda-feira seguinte, a postagem semanal encontra o produto novo no site e já inclui na lista de links e posts.

## Bloco HTML (mesmo formato dos cards atuais da loja)
```html
<article class="card" id="p-caderneta-do-fiado"><span class="badge">Novo</span>
      <img class="cover" src="/capas/capa-caderneta-do-fiado.jpg" alt="Caderneta do Fiado — Controle de Vendas Fiado e Cobrança no WhatsApp" loading="lazy"><h3>Caderneta do Fiado — Controle de Vendas Fiado e Cobrança no WhatsApp</h3><p class="desc">App para quem vende fiado: anote as compras de cada cliente, veja na hora quem está devendo e quem está atrasado, e cobre pelo WhatsApp com a mensagem pronta e a sua chave Pix. Funciona sem internet e sem mensalidade.</p><ul class="ben"><li>Saldo de cada cliente e total a receber na tela inicial</li><li>Aviso de compra vencida, de vencimento próximo e de limite estourado</li><li>Cobrança pronta no WhatsApp, com o saldo e a sua chave Pix</li><li>Pagamento parcial abate as compras mais antigas primeiro</li><li>Movimentos do mês, extrato do cliente e exportação para planilha</li><li>Manual em PDF, passo a passo</li></ul><p class="pay">Abre no Chrome ou no Edge do computador e no Chrome do Android. Os dados ficam no navegador do aparelho; o manual explica o backup.</p>
      <div class="price-row"><span class="price">R$ 24,90</span></div>
      <a class="btn" href="COLE_AQUI_O_LINK_DO_PAGBANK" target="_blank" rel="noopener" style="display:block;text-align:center;text-decoration:none">Comprar agora</a>
      <p class="pay">Pagamento seguro pelo PagBank. Depois de pagar, <a href="https://wa.me/5511913634162?text=Paguei%20o%20Caderneta%20do%20Fiado%20%E2%80%94%20Controle%20de%20Vendas%20Fiado%20e%20Cobran%C3%A7a%20no%20WhatsApp.%20Segue%20o%20comprovante%3A" target="_blank" rel="noopener">mande o comprovante no WhatsApp</a> para receber o arquivo.</p></article>
```

## Mensagem para enviar junto com o arquivo
```
Oi! Obrigado pela compra do Caderneta do Fiado 🎉
Segue o arquivo. Dentro dele tem o app e o manual em PDF.
1. Salve o arquivo e extraia (descompacte).
2. Abra o arquivo .html no Chrome ou no Edge.
3. Siga o manual. Comece pelos dados do seu negócio.
Qualquer dúvida, é só me chamar aqui.
```
