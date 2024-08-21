class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def informacoes_formatadas(self):
        # Retorna uma string formatada com o nome e a idade
        return f"Nome: {self.nome}, Idade: {self.idade}"

# Entrada do usuário
nome = input()
idade = int(input())

# Cria uma instância da Pessoa
pessoa = Pessoa(nome, idade)

# Chama o método para retornar as informações formatadas e imprime o resultado
print(pessoa.informacoes_formatadas())
