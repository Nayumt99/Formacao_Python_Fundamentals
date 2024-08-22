# Criação da classe para converter temperaturas de Celsius para Fahrenheit
class ConversorTemperatura:
    def celsius_para_fahrenheit(self, celsius):
        # Fórmula de conversão
        return (celsius * 9/5) + 32

# Entrada do usuário
celsius = float(input())  # A entrada é lida diretamente sem texto adicional

# Criação de uma instância do conversor
conversor = ConversorTemperatura()

# Realizando a conversão
fahrenheit = conversor.celsius_para_fahrenheit(celsius)

# Exibindo o resultado
print(f"{fahrenheit:.1f}")
