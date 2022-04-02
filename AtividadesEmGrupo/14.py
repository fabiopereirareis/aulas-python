# exercício 14
# regras
# acima de 50kg multa de R$4.00 por kg

#entrada peso dos peixes
entradaKg = float(input("Entre com a quantidade de peixes em kg: "))

# saída peso além do limite
pesoExcedido = entradaKg - 50.0

# saída valor da multa a ser paga
multaPorExcesso = pesoExcedido * 4.00

# saída com os dados completos

print("O peso excedido da pesca foi:", pesoExcedido, "kg")
print("A multa por peso excedido é de: R$", multaPorExcesso)