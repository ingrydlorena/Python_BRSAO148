from datetime import datetime
task_dict = {}
contador_id = 1

menu = '''
O que deseja fazer?
[A] Adicionar task
[E] Editar uma task
[D] Deletar uma task
[L] Listar todas as tasks
'''

while True:
    print(menu)
    escolha = input('')
    if escolha.upper() == "A":
        task_dict[contador_id] = {"descrição" : input("Descreva sua task\n"),
                         "status": input("Qual o estado da sua tarefa?\n"),
                         "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M")}
        contador_id += 1
        print(task_dict)
    else:
        break

        