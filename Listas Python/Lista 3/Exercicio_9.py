N=int(input("Digite uma base para potência: "))
M=int(input("Digite um expoente para potência: "))
base=N
potencia=1
i=1
for i in range (1,M):
    potencia=base*N
    base=potencia
print(potencia)