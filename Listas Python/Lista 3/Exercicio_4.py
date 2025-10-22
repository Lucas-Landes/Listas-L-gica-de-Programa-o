a=int(input("Entre com um valor menor ou igual a 50: "))
while a>50:
    print("Erro: Digite novamente outro valor: ")
    
produto=a
while produto<250:
    print(f"O produto é: {produto}")
    produto *= 3

