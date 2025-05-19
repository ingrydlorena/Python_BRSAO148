"8 - Crie um programa para registrar as temperaturas de vários dias. O usuário deve digitar a temperatura em graus Celsius (ex: 25.5). O programa continua coletando até que o usuário digite "fim" ou colete 7 temperaturas. Valores inválidos devem ser ignorados. Ao final, exiba a média das temperaturas registradas.
"

temperaturas = []

while len(temperaturas) < 7:
    entrada = input("Digite a temperatura em °C (ou 'fim'): ")
    if entrada == 'fim':
        break
    try:
        temp = float(entrada)
        temperaturas.append(temp)
    except ValueError:
        continue

if temperaturas:
    print("Média das temperaturas:", sum(temperaturas) / len(temperaturas))
else:
    print("Nenhuma temperatura válida registrada.")
