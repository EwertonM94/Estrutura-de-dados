print("Média das notas")

num1 = float(input("nota 1: "))
num2 = float(input("nota 2: "))
num3 = float(input("nota 3: "))

soma = (num1 + num2 + num3) / 3

print("A média é", round(soma,2))

if soma < 7:
    print("Reprovado")
elif soma == 10:
    print("Aprovado com Distinção")
else:
    print("Aprovado")