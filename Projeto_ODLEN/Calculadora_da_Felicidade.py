
    #CALCULADORA DE SATISFAÇÃO

#função

def divide(a, b):
    if (b == 0):
        print("Não pode ser zero a sua expectativa!")
    else:
        print("O seu coeficiente de felicidade é: ", a / b)
        if(a>b):
            print("VOCÊ FICOU SATISFEITO!")
        else:
            print("VOÇÊ FICOU INSATISFEITO!")

# Programa

print("Calculadora do nível de satisfação de um determinado fato.")

print(" De sua nota de 1 até 10 para:")

num1 = float(input("Realidade: "))
num2 = float(input("Expectativa: "))

divide(num1, num2)

#A medida da felicidade vai de uma escala de 0.1 até 10.0