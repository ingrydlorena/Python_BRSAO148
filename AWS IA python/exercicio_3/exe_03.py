'''3 - Crie um programa que faça uma contagem regressiva a partir de um número informado pelo usuário até 0. O programa deve mostrar cada número da contagem e, ao final, exibir "FIM!".'''
inicio = int(input("Digite um número para a contagem regressiva: "))

for i in range(inicio, -1, -1):
    print(i)
print("FIM!")
