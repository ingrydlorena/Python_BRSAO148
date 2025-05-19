'''1 - Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.
As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
Trate os seguintes erros:
Entrada inválida (não numérica) para os números
Divisão por zero
Operação inválida
Use try/except para capturar e tratar os erros apropriadamente.
Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa'''

while True:
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        op = input("Digite a operação (+, -, *, /): ")

        if op == "+":
            print("Resultado:", n1 + n2)
        elif op == "-":
            print("Resultado:", n1 - n2)
        elif op == "*":
            print("Resultado:", n1 * n2)
        elif op == "/":
            if n2 == 0:
                print("Erro: divisão por zero.")
                continue
            print("Resultado:", n1 / n2)
        else:
            print("Operação inválida.")
            continue
        break
    except ValueError:
        print("Erro: insira apenas números válidos.")
