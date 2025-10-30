A=[]
print("Valores de A: ")
for i in range(0,10):
    A.append(int(input(f"Valor {i+1}: ")))

B=[0]*10
print("Valores de B: ")
j=9
for i in range(0,10):
    if j>=0:
        B[i]=A[j]
        j=j-1

for i in range(0,10):
    print(f"Valor: {i+1}: {B[i]}")