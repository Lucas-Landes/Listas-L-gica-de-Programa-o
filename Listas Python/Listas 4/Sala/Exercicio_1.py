A=[]
for i in range(0,5):
    A.append(int(input("Digite o número para a lista de 5 valores: ")))
print("Os elementos da matriz B são: ")
B=[]*5
for i in range(0,5):
    B[i]=A[i]*3
    print(f"{i+1}º Elemento: {B[i]}")