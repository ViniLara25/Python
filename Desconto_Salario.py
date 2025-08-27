#Dados do usúario.
nome = input("Digite seu nome: ");
print(f"Olá, {nome}.");

#Informações do Salário.
salario_texto = input("Digite seu salario: ");
salario_texto_correto = salario_texto.replace(",",".");
salario = float(salario_texto_correto);
desconto_inss = salario * 0.2;
salario_liquido = salario - desconto_inss;

print(f"Seu sálario com desconto é de: R$ {salario_liquido:,.2f}");