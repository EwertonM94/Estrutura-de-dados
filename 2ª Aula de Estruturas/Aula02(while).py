notas = int(input("Você vai inserir quantas notas?"))
aluno=input("Nome do Aluno: ")

count = 1; soma = 0.0
while count <= notas:
    print("Nota ", count, ":")
    nota = float(input())
    if nota >= 0 and nota <= 10:
        print("-------------")
        soma+=nota
        count += 1
    else:
        print("###################")
        print("Nota errada, ", nota, ":")
        print("Digite novamente a nota do aluno ", count, "de valores entre 0.0 à 10.0 :")
        nota=float(input())
        soma+=nota
        count += 1

    print("Média do aluno:", aluno,"-",(soma/notas))
