a=float(input("Valor 1: "))
b=float(input("Valor 2: "))
c=float(input("Valor 3: "))

if a+b>c and a+c>b  and b+c>a:
    if a==b and b==c:
        print("Triângulo Equilátero")
    elif a==b or a==c or b==c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não é um triângulo")