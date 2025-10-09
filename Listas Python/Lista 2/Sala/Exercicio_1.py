a=float(input("Primeira nota: "))
b=float(input("Segunda nota: "))
c=float(input("Terceira nota: "))
media=(a+b+c)/3
if media>=6.0:
    print("Aluno aprovado com média: '%.2f'" %(media))
else:
    print("Aluno reprovado com média: '%.2f'" %(media))
