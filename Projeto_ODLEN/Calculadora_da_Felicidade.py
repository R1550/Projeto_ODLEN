#CALCULADORA DE SATISFAÇÃO

#função

def divide(a, b):
    if (b == 0):
        print("Não pode ser zero a sua expectativa!")
    else:
        print("O seu coeficiente é: ", a / b)
        if(a>b):
            print("VOÇÊ FICOU SATISFEITO COM O FATO!")
        else:
            print("VOÇÊ FICOU INSATISFEITO COM O FATO!")

#Programa

print("Calculo do coeficiente de satisfação de um determinado fato.")

print(" De sua nota de 1 até 10 para:")

num1 = float(input("Realidade: "))
num2 = float(input("Expectativa: "))

divide(num1, num2)

#A medida da satisfação vai de uma escala de 0.1 até 10.0
