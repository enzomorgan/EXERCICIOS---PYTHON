#O sistema de avaliação de determinada disciplina é composto por três provas.
#A primeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5.
#Elabore um algoritmo que calcule a média final de um aluno desta disciplina

print("Informe a primeira nota: ")
nota1 = float(input(''))
print("Informe a segunda nota: ")
nota2 = float(input(''))
print("Informe a terceira nota: ")
nota3 = float(input(''))

media_ponderada = (nota1 * 2) + (nota2 * 3) + (nota3 * 5)/2 + 3 + 5

if media_ponderada >= 7.0:
    print("APROVADO!!")
else:
    print("REPROVADO!!")


print(media_ponderada)



