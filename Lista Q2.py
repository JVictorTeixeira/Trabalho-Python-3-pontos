#2 - Faça um programa que recaba três notas, calcule e mostre a média aritmética.
nota1 = float
nota2 = float
nota3 = float

nota1 = float(input('Escreva a primeira nota: '))
nota2 = float(input('Escreva a segunda nota: '))
nota3 = float(input('Escreva a terceira nota: '))
resultado = (nota1+nota2+nota3)/3
print('Sua média aritmética é: {:.2f}'.format(resultado))