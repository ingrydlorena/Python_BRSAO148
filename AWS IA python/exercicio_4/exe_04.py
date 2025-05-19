"4 - Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma."

notas = []

while True:
    entrada = input("Digite a nota (0 a 10) ou 'fim': ")
    if entrada == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida.")
    except ValueError:
        print("Erro: entrada inválida.")

if notas:
    print("Média da turma:", sum(notas) / len(notas))
else:
    print("Nenhuma nota válida registrada.")
