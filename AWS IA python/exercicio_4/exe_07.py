"7 - Crie um programa que permita que o usuário monte uma lista de compras digitando nomes de produtos. O usuário pode digitar até 10 itens. Se digitar "fim", o programa para imediatamente (break). Se o item for vazio (só apertar Enter), ele é ignorado com continue. Use try/except para garantir que apenas strings sejam inseridas.
"

compras = []

for _ in range(10):
    try:
        item = input("Digite um item de compra (ou 'fim'): ")
        if item == "fim":
            break
        if item.strip() == "":
            continue
        compras.append(item)
    except Exception:
        continue

print("Lista de compras:", compras)
