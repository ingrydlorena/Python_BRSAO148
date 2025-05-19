'''1 - Crie um programa que solicite ao usuário uma nota (de 0 a 10) e exiba uma mensagem dizendo se o aluno foi reprovado, em recuperação ou aprovado.
Use as estruturas de decisão if, elif e else.'''

nota = float(input("Digite a nota (0 a 10): "))

if nota < 5:
    print("Reprovado")
elif nota < 7:
    print("Recuperação")
else:
    print("Aprovado")
