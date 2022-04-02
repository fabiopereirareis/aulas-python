# exercício 17
# regras
# cobertura da tinta é de 1 litro para cada 6 metros quadrados
# a tinta é vendida em latas de 18 litros a R$ 80,00
# a tinta é vendida em galões de 3,6 litros a R$ 25,00
 
#entradas: área em metros quadrados a ser pintada,
metrosQuadrados = int(input("Entre com a quantidade de metros quadrados da área a ser pintada: "))
 
# 1 lata = 18 litros / 1 litro = 6 metros quadrados
# 1 lata = 18 * 6
metrosQuadradosPorLata = 18 * 6
 
# 1 galão = 3.6 litros / 1 litro = 6 metros quadrados
# 1 galão = 3.6 * 6
metrosQuadradosPorGalao = 3.6 * 6
 
# saída quantidade de latas necessárias
restoDivisaoLata = int(metrosQuadrados % metrosQuadradosPorLata)
quantidadeLataTinta = int(metrosQuadrados / metrosQuadradosPorLata) +1
 
# saída quantidade de galões necessários
restoDivisaogalao = int(metrosQuadrados % metrosQuadradosPorGalao)
quantidadeGalaoTinta = int((metrosQuadrados + restoDivisaogalao) / metrosQuadradosPorGalao)
 
# saída valor total a ser pago usando latas
valorTotalPinturaLata = int(quantidadeLataTinta * 80.00)
 
# saída valor total a ser pago usando galões
valorTotalPinturaGalao = int(quantidadeGalaoTinta * 25.00)
 
# saída com os dados completos
# usando latas de tinta
print("São necessárias ", quantidadeLataTinta,
", lata(as) de tinta e o valor total do trabalho é de: R$",valorTotalPinturaLata)

# usando galões de tinta
print("São necessárias ", quantidadeGalaoTinta,
", galão(es) de tinta e o valor total do trabalho é de: R$",valorTotalPinturaGalao)
 
# usando latas e galões
litragemTotal = int(metrosQuadrados / 6) + 1
litragemTotalFolga = int(litragemTotal + (litragemTotal * 0.10) + 1)
metragemTotalFolga = litragemTotalFolga * 6
 
quantidadeLataTinta = int(metragemTotalFolga / metrosQuadradosPorLata)
restoDivisaoLata = int(metragemTotalFolga % metrosQuadradosPorLata)
 
quantidadeGalaoTinta = int(restoDivisaoLata / metrosQuadradosPorGalao) + 1
 
valorTotal = int(quantidadeLataTinta * 80) + int(quantidadeGalaoTinta * 25)
 
print("São necessárias ", quantidadeLataTinta,
", lata(as) de tinta,", quantidadeGalaoTinta," galão(es) de tinta e o valor total do trabalho é de: R$",valorTotal)