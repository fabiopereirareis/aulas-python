# print('hello world')

# enquanto o resultado da divisão for maior que zero
# divida o valor de entrada pela base e guarde o resto da divisão num vetor
# entrada = 400
# base = 2


def conversaoBases(entrada:int, base:int):
    """método que recebe um valor inteiro e um valor da base para conversão"""
    divisao = int(entrada / base)
    resto = entrada % base
    resultado = [resto]

    while (divisao > 0):
        resto = divisao % base
        divisao = int(divisao / base)
        resultado.append(resto)

    resultado.reverse()
    textoCompleto = ''

    if base == 16:
        textoCompleto = formatacaoHexadecimal(resultado)
    else:
        for numero in resultado:
            textoCompleto += str(numero)

    return textoCompleto
    # print(textoCompleto)
# print(resultado)
def formatacaoHexadecimal(vetor: int):
    """método que formata o valor de entrada com as letras usadas na base Hexadecimal"""
    textoCompleto = ''
    for elemento in vetor:
        if elemento >= 10:
            if elemento == 10:
                textoCompleto += 'A'
            if elemento == 11:
                textoCompleto += 'B'
            if elemento == 12:
                textoCompleto += 'C'
            if elemento == 13:
                textoCompleto += 'D'
            if elemento == 14:
                textoCompleto += 'E'
            if elemento == 15:
                textoCompleto += 'F'
        else:
            textoCompleto += str(elemento)
    return textoCompleto

resultado = conversaoBases(2748,16)
print(resultado)
# sobra = 2 / 8

# print(sobra)


# def msgTela(msg):
#     print(msg)

# msgTela('Ola mundo')
