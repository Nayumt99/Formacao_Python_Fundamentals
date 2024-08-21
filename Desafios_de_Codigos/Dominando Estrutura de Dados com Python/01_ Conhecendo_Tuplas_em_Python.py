def soma_tupla(tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = input()
    # Converte a entrada em uma tupla de inteiros
    elementos = tuple(map(int, entrada.split()))
    
    # Calcula a soma usando a função soma_tupla
    resultado = soma_tupla(elementos)
    
    # Imprime o resultado
    print(f"A soma dos elementos da tupla é: {resultado}")
