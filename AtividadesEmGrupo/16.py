# exercício 16
# regras
# cobertura da tinta é de 1 litro para cada 3 metros quadrados
# a tinta é vendida em latas de 18 litros a R$ 80,00


#entradas: área em metros quadrados a ser pintada, 
metrosQuadrados = int(input("Entre com a quantidade de metros quadrados da área a ser pintada: "))

# 1 lata = 18 litros / 1 litro = 3 metros quadrados
# 1 lata = 18 * 3 
metrosQuadradosPorLata = 18 * 3
# saída quantidade de latas necessárias
restoDivisao = int(metrosQuadrados % metrosQuadradosPorLata)
quantidadeLataTinta = int((metrosQuadrados + restoDivisao) / metrosQuadradosPorLata)
# saída valor a ser total a ser pago 
valorTotalPintura = int(quantidadeLataTinta * 80.00)

# saída com os dados completos
print("São necessárias ", quantidadeLataTinta,
", latas de tinta e o valor total do trabalho é de: R$",valorTotalPintura)

