qtdade_pepsi = 130
preco_pepsi = 1.50
custo = 2500
faturamento_pepsi = (qtdade_pepsi * preco_pepsi)
print('Faturamento da PEPSI FOI DE'+ ' '+ str(faturamento_pepsi))

qtdade_coca = 150
preco_coca = 1.50
faturamento_coca = (qtdade_coca * preco_coca)
print('Faturamento da COCA FOI DE'+ ' ' + str(faturamento_coca))

lucro = (faturamento_pepsi + faturamento_coca)
print('Lucro da Loja do ultimo mês' + ' ' + str(lucro)) #  usar a função str() para converter o lucro em uma string antes de concatená-lo. 