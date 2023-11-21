#ESCREVA UM PROGRAMA QUE RECEBA DOIS NÚMEROS E UM SINAL
#ENTÃO FAÇA A OPERAÇÃO MATEMÁTICA DEFINIDA PELO SINAL

# -*- coding: utf-8 -*-


numero1 = float(input(''))
numero2 = float(input(''))
operacao = input(("+, *, /, -" "\n"))


if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
elif operacao == "-":
    resultado = numero1 - numero2
else:
    resultado = 0
    print("OPERAÇÃO INVÁLIDA!!")


print(resultado)

            


