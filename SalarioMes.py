salarioHora = float(input("Digite quanto voce ganha por hora: R$"))

horasTrabalhadas = float(input("Digite Quantas horas você trabalha no mes"))

salarioBruto = salarioHora * horasTrabalhadas



def descontos(salarioBruto):
    irrf = salarioBruto * 0.11
    inss = salarioBruto * 0.08
    sindicato = salarioBruto * 0.05
    salarioComDescontos = salarioBruto - irrf - inss - sindicato
    return salarioComDescontos

salarioNovo = descontos(salarioBruto)



def formatarSalario(salarioNovo):
    salarioFormatado = "{:.2f}".format(salarioNovo)
    salarioString = str(salarioFormatado)
    resultadoConvertido = salarioString.replace('.',',')

    return resultadoConvertido

salarioLiquido = formatarSalario(salarioNovo)


print("Voce recebe R$", salarioBruto, "  de salário bruto por mes")
print("Com os descontos o seu salário fica: R$", salarioLiquido)