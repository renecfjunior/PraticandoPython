Raio = float(input("Digite o raio do circulo"))


pi = 3.1415
Area = pi * (Raio * Raio)

# Variavel para arredondar o numero
Resultado = round(Area, 2)

# Converter em string para poder colocar virgula no resultado em vez de ponto

converterEmString = str(Resultado)

#colocando virgula no resultado
ResultadoComVirgula = converterEmString.replace('.',',')

print("A area do seu circulo é de ", ResultadoComVirgula)