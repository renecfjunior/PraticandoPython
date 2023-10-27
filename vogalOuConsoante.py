print("Olá, eu vou adivinhar se você vai digitar uma vogal ou Consoante :D")

letraDigitada = input("Digite aqui uma volgal ou consoante: ")

if len(letraDigitada) >1:
    print("tu digitou mais de uma letra mlk, TA MALUCO??????")

else:
    vogais = ["a","e","i","o","u"]
    if letraDigitada in vogais:
        print("Voce digitou uma vogal rapá")
    
    else:
        print("Tu digitou consoante manezao")