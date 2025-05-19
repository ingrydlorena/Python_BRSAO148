'''7 - Crie um programa que percorre uma lista de números inteiros e imprime apenas os que são números primos. Use o for para iterar, if para a verificação e continue para pular os que não são primos.'''
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numeros:
    if num < 2:
        continue
    primo = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            primo = False
            break
    if not primo:
        continue
    print(num)
