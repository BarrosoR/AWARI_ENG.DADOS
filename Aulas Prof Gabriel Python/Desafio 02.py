# Crie um algoritmo que tenha como entrada o nome e o ano de nascimento de uma pessoas e retorne o texto abaixado fazendo o calculo de sua idade
# Olá Maria, você é de 1994 e sua idade é de 27 anos.
from datetime import date

nome = input('Digite seu nome:')
ano_de_nascimento = int(input('Digite o ano de nascimento:'))
idade = date.today().year - ano_de_nascimento

#Na primeira tentativa não consegui importar o date.today().year, depois de ver o problema utilizei. 

print('Olá', nome + ',', 'você é de', ano_de_nascimento, 'e sua idade é de', idade, 'anos.')