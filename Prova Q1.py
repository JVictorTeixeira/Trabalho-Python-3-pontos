#1 - Faça um programa que calcule e mostre a área de um círculo. Sabe-se que: Área = 3,14*r²
raio = float(input('Informe o valor do raio para obter a área: '))
area = 3.14 * (raio * raio)
print('A área do circulo é: {:.2f}'.format(area))