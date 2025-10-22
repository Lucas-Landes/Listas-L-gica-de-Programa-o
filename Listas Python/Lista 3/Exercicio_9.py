N=int(input("Digite uma base para potência: "))
M=int(input("Digite um expoente para potência: "))
base=N
potencia=1
i=1
while i<=M:
    potencia=base*N
    base=potencia
print(potencia)