a=int(input("Entre  com um primeiro valor: "))
b=int(input("Entre com um segundo valor: "))
c=int(input("Entre com um terceiro valor: "))
if a>=b>=c:
    print(f"O maior número é o: {a}")
    print(f"O segundo maior número é o: {b}")
    print(f"O menor número é o: {c}")
elif a>=c>=b:
    print(f"O maior número é o: {a}")
    print(f"O segundo maior número é o: {c}")
    print(f"O menor número é o: {b}")
elif b>=a>=c:
    print(f"O maior número é o: {b}")
    print(f"O segundo maior número é o: {a}")
    print(f"O menor número é o: {c}")
elif b>=c>=a:
    print(f"O maior número é o: {b}")
    print(f"O segundo maior número é o: {c}")
    print(f"O menor número é o: {a}")
elif c>=a>=b:
    print(f"O maior número é o: {c}")
    print(f"O segundo maior número é o: {a}")
    print(f"O menor número é o: {b}")
else:
    print(f"O maior número é o: {c}")
    print(f"O segundo maior número é o: {b}")
    print(f"O menor número é o: {a}")
