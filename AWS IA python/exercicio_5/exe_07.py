'''7 - Crie um programa que permita ao usuário montar uma lista de compras. O usuário poderá adicionar itens até digitar "fim". Ao final, o programa exibirá todos os itens da lista. O programa deve estar estruturado com uma função main() e ser executado com if __name__ == "__main__":.'''

def main():
    lista = []
    while True:
        try:
            item = input("Digite um item (ou 'fim'): ")
            if item.lower() == "fim":
                break
            lista.append(item)
        except:
            print("Erro ao adicionar item.")
    print("Lista de compras:")
    for i in lista:
        print(f"- {i}")

if __name__ == "__main__":
    main()
