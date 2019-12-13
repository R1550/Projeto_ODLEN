#inputs - Váriaveis

print()
print("OLÁ HUMANO, EU SOU UM PROGRAMA EM DESENVOLVIMENTO!.  " )
print()
nome = input("Qual é o seu nome? ")
print(f"Prazer em conhece-lo {nome}! ")
print()
idade = input("E a sua a sua idade? ")
print(f"Eu ainda não tenho uma noção de tempo definida. ")
print()
ano_nasc = 2019 - int(idade)
print(f"Então {nome} você nasceu no ano de {int(ano_nasc)}. ")
print()
altura = input("Qual é a sua altura? ")
print(f"Tens {float(altura)}m fisicamente não faço ideia disso, mas em números sei bem. ")
print()
peso = input("Qual é o seu peso? ")
print(f"Tens {float(peso)}Kg, então pelos meus calculos aqui.")
print()

#Condicionais 1

if int(peso) >= 80: 
    print(f"Acho que voçê é um humano bem pesado! ")
else:
    print(f"Até que voçê deve ser um humano leve {nome}! ") 
print()

imc = float(peso) / float(altura) ** float(2)  #Formula do IMC

#Condicionais 2

print(f"Observei {nome} que seu IMC é {int(imc)} então: ")
if imc <= 16.99:
    print("Você está muito abaixo do peso.")
elif imc >= 17 and imc <= 18.49:
    print("Voçê está abaixo do peso.")
elif imc >= 18.5 and imc <= 24.99:
    print("Voçê está com um peso ideal.")  
elif imc >= 25 and imc <= 29.99: 
    print("Voçê está acima do peso ideal.")
elif imc >= 30 and imc <= 34.99:
    print(f"Voçê está está em estado de obesidade {nome}, se cuide!")
elif imc >= 35 and imc <= 39.99:
    print("Voçê está em um grau de obesidade severa!")

else:
    print(f"Voçê se encontra em estdado de obesidade mórmida já {nome}.") 
    print("Procure ajuda médica urgente, por favor!") 
print()

print()

print(f"Foi bom conhecer você humano.\nAté uma próxima se voçê ainda tiver vivo haha... ")
print("Tchau!") 
