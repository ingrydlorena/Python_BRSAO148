'''5- Verificador de Número Primo
Enunciado:
Crie um programa que solicite um número inteiro positivo ao usuário e verifique se ele é um número primo. Um número primo só é divisível por 1 e por ele mesmo.'''

# Solicita o número
num = int(input("Digite um número inteiro positivo: "))

# Verifica se é primo
eh_primo = True
if num < 2:
    eh_primo = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break

# Exibe o resultado
if eh_primo:
    print("É primo")
else:
    print("Não é primo")
