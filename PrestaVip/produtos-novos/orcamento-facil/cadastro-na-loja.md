# Orçamento Fácil — cadastro na loja

**Preço sugerido:** R$ 27,00 (pagamento único)
**Selo:** Novo
**Capa:** `capa-orcamento-facil.jpg` (800 × 800, mesmo formato das outras capas da loja)
**Arquivo para entregar ao cliente:** `orcamento-facil.zip` (app + manual em PDF)

## Nome
Orçamento Fácil — Orçamentos e Recibos em PDF com a Sua Marca

## Descrição
Faça orçamentos e recibos com a sua logo e os seus dados em menos de um minuto. Gere o PDF, mande o resumo pelo WhatsApp e acompanhe quais orçamentos foram aprovados. Funciona sem internet e sem mensalidade.

## Benefícios
- Sua logo, cor, CPF/CNPJ e chave Pix no documento
- Orçamento numerado com validade, prazo e forma de pagamento
- PDF pronto para enviar ao cliente
- Recibo gerado a partir do orçamento, com valor por extenso
- Resumo pronto para o WhatsApp do cliente
- Controle de aprovados e recusados, com taxa de aprovação

## Aviso (linha pequena)
Abre no Chrome ou no Edge do computador e no Chrome do Android. Orçamento e recibo não substituem a nota fiscal quando ela for exigida.

## Passo a passo para colocar na loja
1. No PagBank, crie um **link de pagamento** de R$ 27,00 com o nome "Orçamento Fácil" e copie o link (`https://pag.ae/...`).
2. Envie a capa `capa-orcamento-facil.jpg` para a pasta `/capas/` do site.
3. Cole o bloco HTML abaixo na lista de produtos do site, trocando `COLE_AQUI_O_LINK_DO_PAGBANK` pelo link do passo 1.
4. Quando o cliente mandar o comprovante no WhatsApp, envie o arquivo `orcamento-facil.zip`.

Na segunda-feira seguinte, a postagem semanal encontra o produto novo no site e já inclui na lista de links e posts.

## Bloco HTML (mesmo formato dos cards atuais da loja)
```html
<article class="card" id="p-orcamento-facil"><span class="badge">Novo</span>
      <img class="cover" src="/capas/capa-orcamento-facil.jpg" alt="Orçamento Fácil — Orçamentos e Recibos em PDF com a Sua Marca" loading="lazy"><h3>Orçamento Fácil — Orçamentos e Recibos em PDF com a Sua Marca</h3><p class="desc">Faça orçamentos e recibos com a sua logo e os seus dados em menos de um minuto. Gere o PDF, mande o resumo pelo WhatsApp e acompanhe quais orçamentos foram aprovados. Funciona sem internet e sem mensalidade.</p><ul class="ben"><li>Sua logo, cor, CPF/CNPJ e chave Pix no documento</li><li>Orçamento numerado com validade, prazo e forma de pagamento</li><li>PDF pronto para enviar ao cliente</li><li>Recibo gerado a partir do orçamento, com valor por extenso</li><li>Resumo pronto para o WhatsApp do cliente</li><li>Controle de aprovados e recusados, com taxa de aprovação</li></ul><p class="pay">Abre no Chrome ou no Edge do computador e no Chrome do Android. Orçamento e recibo não substituem a nota fiscal quando ela for exigida.</p>
      <div class="price-row"><span class="price">R$ 27,00</span></div>
      <a class="btn" href="COLE_AQUI_O_LINK_DO_PAGBANK" target="_blank" rel="noopener" style="display:block;text-align:center;text-decoration:none">Comprar agora</a>
      <p class="pay">Pagamento seguro pelo PagBank. Depois de pagar, <a href="https://wa.me/5511913634162?text=Paguei%20o%20Or%C3%A7amento%20F%C3%A1cil%20%E2%80%94%20Or%C3%A7amentos%20e%20Recibos%20em%20PDF%20com%20a%20Sua%20Marca.%20Segue%20o%20comprovante%3A" target="_blank" rel="noopener">mande o comprovante no WhatsApp</a> para receber o arquivo.</p></article>
```

## Mensagem para enviar junto com o arquivo
```
Oi! Obrigado pela compra do Orçamento Fácil 🎉
Segue o arquivo. Dentro dele tem o app e o manual em PDF.
1. Salve o arquivo e extraia (descompacte).
2. Abra o arquivo .html no Chrome ou no Edge.
3. Siga o manual. Comece pelos dados do seu negócio.
Qualquer dúvida, é só me chamar aqui.
```
