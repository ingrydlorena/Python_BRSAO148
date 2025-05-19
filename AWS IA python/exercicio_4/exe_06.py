'''6 - Peça ao usuário que digite 10 números inteiros. Armazene apenas os números pares válidos em uma lista. Use try/except para capturar erros, continue para ignorar números ímpares ou inválidos, e exiba a lista final ao terminar.'''

pares = []

for _ in range(10):
    try:
        num = int(input("Digite um número inteiro: "))
        if num % 2 == 0:
            pares.append(num)
    except ValueError:
        continue

print("Números pares válidos:", pares)
