import random
numero_chave=random.randint(1,99)
a=int(input("Qual o número desejado: "))
print(f"A distância entre o número desejado e o criado pela máquina é de: {abs(a-numero_chave)}")
#Mostrar o número gerado pela máquina
print(f"O número chave era: {numero_chave}")