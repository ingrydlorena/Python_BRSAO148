'''4 - Crie uma função que recebe dois números e retorna a soma. O programa deve pedir os números ao usuário, chamar a função e exibir o resultado.'''

def soma(a, b):
    return a + b

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = soma(num1, num2)
    print(f"Soma: {resultado}")
except:
    print("Entrada inválida.")
