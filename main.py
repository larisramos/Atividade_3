'''Fazer um programa em linguagem Python que ao receber o salário atual de um funcionário, calcule o valor do novo salário, reajustado de acordo com a tabela abaixo: (2,0)
Salário atual
Reajuste
Abaixo de R$500,00
15%
de R$500,00 até R$1000,00
10%
Acima de R$1000,00	                     
5%'''
salario_atual = float(input('Digite o seu salário atual: '))
if salario_atual < 500:
  salario_reajustado = salario_atual + (salario_atual*0.15)
  print(f'O seu novo salario será R${salario_reajustado}')
elif salario_atual >= 500 and salario_atual <= 1000:
  salario_reajustado = salario_atual + (salario_atual*0.10)
  print(f'O seu novo salario será R${salario_reajustado}')
else:
  salario_reajustado = salario_atual + (salario_atual*0.05)
  print(f'O seu novo salario será R${salario_reajustado}')
  