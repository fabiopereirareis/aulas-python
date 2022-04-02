# exercício 11

#entrada 2 números inteiros e 1 número real
numero01 = int(input("Entre com primeiro número inteiro:"))
numero02 = int(input("Entre com segundo número inteiro:"))
numero03 = float(input("Entre com um número real:"))

# solução01:
# produto do dobro do primeiro com metade do segundo
dobro = numero01 * 2
metadeSegundo = numero02 / 2
somaSolucao01 = dobro + metadeSegundo

# solução02:
# a soma do triplo do primeiro com o terceiro
triplo = dobro + numero01
somaSolucao02 = triplo + numero03

# solução03:
# o terceiro elevado ao cubo
solucao03 = numero03 ** 3

print("Solução 01:", somaSolucao01)
print("Solução 02:", somaSolucao02)
print("Solução 03:", solucao03)