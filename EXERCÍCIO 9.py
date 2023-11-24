#Crie um programa no qual o usuário deverá inserir os valores da altura
#largura e profundidade de uma caixa d’água, em cm
#No final, exiba o volume dessa caixa d’água

print("Informe a altura: ")
altura = float(input(''))
print("Informe a largura: ")
largura = float(input(''))
print("Informe a pronfundidade: ")
profun = float(input(''))

volume = altura * largura * profun

print(volume)

centimetros = volume * 100

print(centimetros)

