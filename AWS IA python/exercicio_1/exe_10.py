'''
Crie uma função que receba um número como argumento e retorne o quadrado 
desse número. Depois, chame essa função passando um número digitado pelo usuário.
'''
def solicitacao():
    valor = int(input(f"Diga um numero colega: "))
    return valor
def quadradinho(valor):
    quadrado = valor ** 2
    print(f"O seu numero quadradinho é {quadrado}")

valor = solicitacao()
quadradinho(valor)
