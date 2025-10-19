total_salarios=0
while True:

    salario_bruto=float(input("Qual o salário do funcionário da sua empresa (caso digiyte 0, o programa irá encerrar.): "))
    if salario_bruto==0:
        break;
    horas_trabalhadas=int(input("Quantas horas esse funcionário trabalhou no mês: "))
    
    if salario_bruto<800:
        salario_descontado=salario_bruto

    elif salario_bruto>=800 and salario_bruto<=1600:
        salario_descontado = salario_bruto - (0.08*salario_bruto + 0.05*salario_bruto)

    elif salario_bruto>1600:
        salario_descontado = salario_bruto - (0.15*salario_bruto + 0.07*salario_bruto)
    else:
        print("Este salário é invalido")

    if horas_trabalhadas>160:
        acrescimo_salarial=((salario_bruto/160)*0.5)*(horas_trabalhadas-160)
        salario_liquido=salario_descontado+acrescimo_salarial
    else:
        salario_liquido=salario_descontado
    print(f"O salário líquido do funcionário foi de: {salario_liquido}")
    total_salarios=total_salarios+salario_liquido
print(f"O total a ser pago com salários foi de: {total_salarios}")