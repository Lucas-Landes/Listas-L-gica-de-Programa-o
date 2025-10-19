curso=int(input("Qual o número do curso: "))
if curso>5 or curso<1:
    print("O número digitado não corresponde a um curso.")
    while curso>5 or curso<1:
        curso=int(input("Qual o número do curso: "))
        if curso>5 or curso<1:
            print("O número digitado não corresponde a um curso.")
match curso:
    case 1:
        print("Engenharia")
    case 2:
        print("Edificações")
    case 3: 
        print("Sistemas Elétricos")
    case 4:
        print("Turismo")
    case 5: 
        print("Análise de Sistemas")

