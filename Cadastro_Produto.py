#Desenvolver um pequeno sistema para uma loja. Cadastro de produtos, calculo de preço final (com impostos) e exibir o total.
#1. Pedir ao usuário o nome do produto.
#2. Preço de custo do produto.
#3. Porcentagem de lucro desejada.
#4. Imposto sobre o valor de venda.

#Cadastro do produto
produto = ""
while not produto: 
    produto = input("Digite o produto: ").strip()
if not produto: print("O produto não pode ficar em branco")
print ("Item cadastrado com sucesso");

#Valor do produto

#valor_texto = ""
#while not valor_texto:
#    valor_texto = input("Digite o valor pago pelo produto: ").strip()
#    valor_correto = valor_texto.replace(",",".")
#    valor_pago = float(valor_correto)
#if not valor_texto: print("O valor não pode ficar em branco")

#print(f'O valor é: R${valor_pago:,.2f}')

while True: 
    try: 
        valor_texto = input("Digite o valor do produto: ")
        valor_correto = valor_texto.replace(',','.')
        valor = float(valor_correto) 
        print("Valor cadastrado com sucesso!")
        break
    except ValueError: print("Valor inválido, digite novamente.")

#Margem de lucro.

while True:
    try:
        lucro_texto = input("Digite a porcentagem de lucro: ")
        lucro_correto = lucro_texto.replace(',','.')
        lucro = float(lucro_correto)
        print("Valor cadastrado com sucesso")
        break
    except ValueError: print("Valor inválido, digite novamente.")

#Calculos de venda com ICMS de São Paulo 18%.


