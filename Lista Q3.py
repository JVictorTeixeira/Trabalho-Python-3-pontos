#3 - Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada.
Nota1 = float(input("Digite sua primeira Nota: "))
Nota2 = float(input("Digite sua segunda Nota: "))
Nota3 = float(input("Digite sua terceira Nota: "))
Peso1 = float(input("Digite o primeiro peso: "))
Peso2 = float(input("Digite o segundo peso:"))
Peso3 = float(input("Digite o terceiro peso: "))

Soma1 = Nota1*Peso1 + Nota2*Peso2 + Nota3*Peso3
Soma2 = Peso1+Peso2+Peso3
Soma3 = Soma1/Soma2
print('Seu resultado é: {:.2f}'.format(Soma3))