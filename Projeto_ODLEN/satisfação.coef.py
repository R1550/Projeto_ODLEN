#CALCULADORA DE SATISFAÇÃO

#função

def divide(a, b):
    if (b == 0):
        print("Não pode ser zero a sua expectativa!")
    else:
        print("O seu coeficiente de satisfação é: ", a / b)
        if(a>b):
            print("VOÇÊ FICOU SATISFEITO!")
        else:
            print("VOÇÊ FICOU INSATISFEITO!")

# Programa

print("Nível de satisfação de um determinado fato.")

print(" De sua nota de 1 até 10 para:")

num1 = float(input("Expectativa: "))
num2 = float(input("Realidade: "))

divide(num2, num1)

#	O coeficiente vai de uma escala de 0.1 até 10.0
