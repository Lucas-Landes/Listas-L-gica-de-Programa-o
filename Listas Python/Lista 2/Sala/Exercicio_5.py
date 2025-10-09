
A=float(input("Valor A: "))
B=float(input("Valor B: "))
C=float(input("Valor B: "))
if A==B==C or A==B and B>C or A>B and B>C:
    print("Ordem Crescente: ", C, B, A)
elif B>A and A>C or B>A and A==C:
    print("Ordem Crescente: ", C, A, B)
elif B>C and C>A:
    print("Ordem Crescente: ", A, C, B)
elif C>A and A>B or C>A and A==B:
    print("Ordem Crescente: ", B, A, C)
elif A>C and C>B:
    print("Ordem Crescente: ", B, C, A)
else:
    print("Ordem Cresente: ", A, B, C)

