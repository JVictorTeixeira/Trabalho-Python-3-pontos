#4 - Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu aumento de 25%.
sal = int(input('informe seu salário: '))
aumento = 0.25
saltotal = sal+sal*aumento
print('Seu salário será de: {:.2f}'.format(saltotal))