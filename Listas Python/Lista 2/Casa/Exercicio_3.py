nota=float(input("Entre com uma nota: "))
nota_inteira=int(nota)
nota_decimal=nota-nota_inteira
if nota_decimal>0.5:
    nota_arredondada=nota_inteira+1
else:
    nota_arredondada=nota_inteira
print(f"A nota do aluno pós arredondamento foi de: {nota_arredondada}")