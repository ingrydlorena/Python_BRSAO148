'''5 - Crie um programa com uma função que cadastre alunos e suas respectivas notas.
O sistema deve:
Solicitar o nome do aluno.
Solicitar 3 notas válidas (entre 0 e 10).
Armazenar os dados em um dicionário, onde a chave é o nome e o valor é uma lista de notas.
Permitir o cadastro de vários alunos até que o usuário digite "fim".
Exibir ao final:
A lista de alunos e suas médias.
O aluno com a maior média.
Use def para as funcionalidades e try/except para tratar entradas inválidas.'''

def cadastrar_alunos():
    alunos = {}
    while True:
        nome = input("Nome do aluno (ou 'fim'): ")
        if nome.lower() == "fim":
            break
        notas = []
        for i in range(3):
            while True:
                try:
                    nota = float(input(f"Nota {i+1}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota deve ser entre 0 e 10.")
                except:
                    print("Entrada inválida.")
        alunos[nome] = notas
    return alunos

def exibir_resultados(alunos):
    maior_media = 0
    melhor_aluno = ""
    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)
        print(f"{nome} - Média: {media:.2f}")
        if media > maior_media:
            maior_media = media
            melhor_aluno = nome
    if melhor_aluno:
        print(f"Aluno com maior média: {melhor_aluno} - {maior_media:.2f}")

alunos = cadastrar_alunos()
exibir_resultados(alunos)
