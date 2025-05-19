'''2 - Crie um programa que solicite um número ao usuário e exiba a tabuada desse número de 1 a 10, utilizando a estrutura de repetição for.'''
num = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

