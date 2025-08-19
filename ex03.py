# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

produto = float (input('Valor do produto:'))
desconto = produto - (produto * 5 / 100)
print ('O produto do valor R${:.2f} com 5% de desconto fica por:R${:.2f}'.format(produto,desconto))

# {:.2f} O 2f em Python é uma especificação de formatação que indica que o valor deve ser apresentado como um float com duas casas decimais 
