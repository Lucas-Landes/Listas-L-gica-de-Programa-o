a=int(input("Entre  com um primeiro valor: "))
b=int(input("Entre com um segundo valor: "))
c=int(input("Entre com um terceiro valor: "))

numeros_sort=sorted([a,b,c])

print(f"O maior número é o: {numeros_sort[2]}")
print(f"O segundo maior número é o: {numeros_sort[1]}")
print(f"O menor número é o: {numeros_sort[0]}")