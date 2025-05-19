"9 - Solicite ao usuário números inteiros até que ele digite "0". Armazene os positivos e negativos separadamente em duas listas. Ignore valores não inteiros com try/except. No final, mostre quantos positivos e negativos foram inseridos.
"

positivos = []
negativos = []

while True:
    entrada = input("Digite um número inteiro (ou '0' para sair): ")
    try:
        num = int(entrada)
        if num == 0:
            break
        elif num > 0:
            positivos.append(num)
        else:
            negativos.append(num)
    except ValueError:
        continue

print("Positivos:", len(positivos))
print("Negativos:", len(negativos))
