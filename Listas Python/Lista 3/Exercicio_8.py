f1=1
f2=0
termo_fibonacci=1
print(f"O termo 1 da sequência de fibonacci é igual a: {termo_fibonacci}")
for i in range (1,15):
    termo_fibonacci=f1+f2
    f2=f1
    f1=termo_fibonacci
    print(f"O termo {i+1} da série de Fibonacci é igual a: {termo_fibonacci}")

