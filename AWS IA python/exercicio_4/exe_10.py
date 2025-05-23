"10 - Peça ao usuário para digitar palavras. Armazene apenas as palavras com mais de 5 letras em uma lista. Se a palavra for "parar", o programa encerra (break). Se a palavra for numérica (como "123"), ignore com continue. Use try/except para garantir que só palavras (strings) sejam processadas. No final, exiba a lista das palavras longas inseridas."

palavras_longas = []

while True:
    try:
        palavra = input("Digite uma palavra (ou 'parar'): ")
        if palavra == "parar":
            break
        if palavra.isnumeric():
            continue
        if len(palavra) > 5:
            palavras_longas.append(palavra)
    except Exception:
        continue

print("Palavras com mais de 5 letras:", palavras_longas)
