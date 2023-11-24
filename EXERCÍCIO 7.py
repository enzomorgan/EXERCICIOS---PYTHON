#Crie um algoritmo que leia dois números nas variáveis numA e numB, nessa ordem
#e os mostre na tela em ordem inversa. um embaixo do outro (em linhas distintas).


print("Digite o primeiro valor: ")
numA = int(input(''))

print("Digite o segundo valor: ")
numB = int(input(''))

if numA < numB:
    print(numB,"\n", numA,)
else: 
    print(numA, "\n", numB) 


