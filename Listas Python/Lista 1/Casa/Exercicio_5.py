massa=float(input("Qual a massa da pessoa (em kg): "))
altura=float(input("Qual a altura da pessoa (em m): "))
if altura<=0 or massa<=0:
    print("Erro, pois altura e massa devem ser maiores do que 0")
else:
    print(f"O Índice de Massa Corporal dessa pessoa é de: {massa/(altura**2)}")