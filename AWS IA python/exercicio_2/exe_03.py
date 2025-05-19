'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

# Solicita a temperatura e unidades
temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Unidade de destino (C/F/K): ").upper()

# Converte para Celsius
if origem == "F":
    temp = (temp - 32) * 5/9
elif origem == "K":
    temp = temp - 273.15

# Converte de Celsius para destino
if destino == "F":
    temp = (temp * 9/5) + 32
elif destino == "K":
    temp = temp + 273.15

# Exibe o resultado
print("Temperatura convertida:", round(temp, 2), destino)
