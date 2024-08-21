class Calculadora:
    def soma(self, a, b):
        return a + b

# Leitura dos números inteiros fornecidos pelo usuário
num1 = int(input())
num2 = int(input())

# Criando uma instância da Calculadora
calc = Calculadora()

# Realizando a soma
resultado = calc.soma(num1, num2)

# Imprimindo o resultado
print(resultado)
