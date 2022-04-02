# exercício 15
# regras
# descontos 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato

#entradas: valor por hora, horas trabalhadas
horasTrabalhadas = int(input("Entre com a quantidade de horas trabalhadas: "))
valorPorHora = float(input("Entre com o valor ganho por hora: "))

# saída salário bruto
salarioBruto = horasTrabalhadas * valorPorHora

# saída valor a ser pago INSS
inss = salarioBruto * 0.08

# saída valor a ser pago Imposto de Renda
impostoRenda = salarioBruto * 0.11

# saída valor contribuição do sindicato
contribuicaoSindicato = salarioBruto * 0.05

# saída salário líquido
salarioLiquido = salarioBruto - inss - impostoRenda - contribuicaoSindicato

# saída com os dados completos
print("Salário bruto: R$", salarioBruto)
print("Valor INSS: R$", inss)
print("Contribuição ao sindicato: R$", contribuicaoSindicato)
print("Salário líquido: R$", salarioLiquido)
