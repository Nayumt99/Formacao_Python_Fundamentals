def elementos_comuns(lista1, lista2):
    try:
        # Converte as listas de strings para listas de inteiros
        set1 = set(map(int, lista1))
        set2 = set(map(int, lista2))
        
        # Encontra a interseção entre os dois conjuntos
        comuns = set1.intersection(set2)
        
        # Retorna a lista dos elementos comuns
        return sorted(list(comuns))
    except ValueError:
        # Caso haja erro na conversão para inteiro, retorna a mensagem de erro
        return "Entrada inválida."

# Leitura das listas
lista1 = input().split()
lista2 = input().split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    if comuns == "Entrada inválida.":
        print(comuns)
    else:
        print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")
