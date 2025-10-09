#2)- Ler 2 valores referentes a 2 notas de um aluno e exibir uma mensagem dizendo que
#o aluno foi aprovado, se o valor da média for maior ou igual a 6.0. Se o valor da média
#for menor que 6.0, solicitar a nota de exame, somar com o valor da média e obtiver
#uma nova média. Se a nova média for maior ou igual a 5, exibir mensagem dizendo
#que o aluno foi aprovado em exame. Se o aluno não foi aprovado, exibir uma
#mensagem informando essa condição. Exibir junto com uma das mensagens, o valor
#da média para qualquer condição.

a=float(input("Primeira Nota: "))
b=float(input("Segunda Nota: "))
c=float(input("Terceira Nota: "))

media=(a+b+c)/3

if media>=6.0:
    print("Aluno aprovado com média '%.2f'" %(media))

else:
    nota_exame=float(input("Nota de Exame: "))
    nova_media=(media+nota_exame)/2
    if nova_media>=5.0:
        print("Aluno aprovado em exame com média: '%.2f'" %(nova_media))
    else:
        print("Aluno reprovado: '%.2f'" %(nova_media))