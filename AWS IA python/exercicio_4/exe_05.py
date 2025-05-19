"5 - Crie um programa que solicite ao usuário a idade de várias pessoas. Armazene apenas idades válidas (entre 0 e 120) em uma lista. Use for, try/except, continue para ignorar entradas inválidas, e break para encerrar o programa se o usuário digitar "fim". No final, exiba a lista das idades válidas."

idades = []

while True:
    entrada = input("Digite a idade ou 'fim': ")
    if entrada == 'fim':
        break
    try:
        idade = int(entrada)
        if 0 <= idade <= 120:
            idades.append(idade)
        else:
            print("Idade fora do intervalo.")
    except ValueError:
        print("Entrada inválida.")
        continue

print("Idades válidas:", idades)
