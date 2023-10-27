print('''Vou calcular a probabilidade entre dois números
      ex: 1 em 2 = 50% de chance''')

numeroProbabilidade = float(input("Digite aqui o número da probabilidade "))

numeroChances = float(input("Digite aqui o numero total de chances "))

total = (numeroProbabilidade / numeroChances) * 100

def limitarCasasDecimais(total):
    ResultadoFormatado = "{:.2f}".format(total)
    ResultadoString = str(ResultadoFormatado)
    ResultadoVirgula = ResultadoString.replace('.',',')
    return ResultadoVirgula


numeroFinal = limitarCasasDecimais(total)

print("A chance é de " + numeroFinal + "%")