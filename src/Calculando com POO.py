# TODO: Crie uma classe e método para realizar a soma:
class Calculadora:
    def soma(self, num1, num2):
        return num1 + num2

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

# Criando uma instância da calculadora
calc = Calculadora()

resultado = calc.soma(num1, num2)
print(resultado)
