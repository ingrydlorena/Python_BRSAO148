'''
8 - Crie um programa que solicita a nota de avaliação de um restaurante (de 0 a 5) e exibe a quantidade de estrelas equivalente, juntamente com uma mensagem personalizada. Use if, elif e else para lidar com diferentes faixas de nota.
'''

nota = int(input("Nota do restaurante (0 a 5): "))

if nota == 5:
    print("★★★★★ - Excelente!")
elif nota == 4:
    print("★★★★ - Muito bom!")
elif nota == 3:
    print("★★★ - Bom")
elif nota == 2:
    print("★★ - Regular")
elif nota == 1:
    print("★ - Ruim")
else:
    print("Sem estrelas - Péssimo")
