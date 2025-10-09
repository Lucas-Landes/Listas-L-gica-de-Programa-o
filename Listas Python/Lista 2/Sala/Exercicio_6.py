#6)- Ler 3 valores (A, B e C) e calcular a equação de segundo grau, 
#exibindo as duas raízes, se para os valores informados for possível
#efetuar o referido cálculo.
import math
a=float(input("Coeficiente a: "))
b=float(input("Coeficiente b: "))
c=float(input("Coeficiente c: "))
delta=pow(b,2)-4*a*c
if delta>0:
    print(f"x1: {(-b+math.sqrt(delta))/(2*a)}")
    print(f"x2: {(-b-math.sqrt(delta))/(2*a)}")
elif delta==0:
    print(f"x= {-b/(2*a)}")
else:
    print("Não existem raízes reais")