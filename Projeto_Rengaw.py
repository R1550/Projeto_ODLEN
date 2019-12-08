#Treinamneto de um programa interativo em python!

print()
print("Olá eu me chamo Rengaw, sou um programa em Python!" )
print()
nome = input("Qual é o seu nome? ")
print(f"Prazer em conhece-lo {nome}! ")
print()
idade = input("Qual é a sua idade? ")
print(f"Eu não tenho uma idade definida.\nMas {idade} anos parece ser uma boa idade humana. ")
print()
ano_nasc = 2019 - int(idade)
print(f"Então {nome} você nasceu em {int(ano_nasc)} legal! ")
print()
altura = input("Qual a sua altura? ")
print(f"Não sei exatamente o quanto é isso, mas {float(altura)} de altura parece ser algo bom. ")
print()
peso = input("Qual é o seu peso? ")
print(f"Acho que {float(peso)}Kg parece ser bom haha...")
print()
imc = float(peso) / float(altura) ** float(2)
print(f"Observei que seu IMC é {int(imc)} {nome} então tome cuidado sempre!\nLembrando que os valores normais de IMC é entre 18,5 e 24,99 então cuide da sua saúde. ") 
print(f"Não esqueça {nome} que voçê não é um ser imortal que nem eu haha...")
print()
print(f"Bom, eu vou aguardar meu programador me aperfeiçoar mais para falar com voçê novamente, foi bom conhecer você. ")
print("Até mais humano!")

#CONTINUAR... Criar a escala de normalidade do IMC  e fazer a maquina responder conforme a escala.

