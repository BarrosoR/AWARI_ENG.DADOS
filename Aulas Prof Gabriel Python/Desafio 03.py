#A partir de um novo texto, traga os dados básicos como:

#Quantidade de caracteres
#Quantidade de cada vogal no texto
#Quantas vezes aparece a palavra América no texto
#Depois, substítua Brasil por BRASIL.

texto = """ Brasil, oficialmente República Federativa do Brasil é o maior país da América do Sul e da região da América Latina, sendo o quinto maior do mundo em área territorial (equivalente a 47 porcento do território sul-americano) e sexto em população (com mais de 200 milhões de habitantes). É o único país na América onde se fala majoritariamente a língua portuguesa e o maior país lusófono do planeta, além de ser uma das nações mais multiculturais e etnicamente diversas, em decorrência da forte imigração oriunda de variados locais do mundo."""

qtd_caracteres = len(texto)

print('O tamanho  da string é:',qtd_caracteres)

print('vogal a:', texto.count('a'))
print('vogal e:', texto.count('e'))
print('vogal i:', texto.count('i'))
print('vogal o:', texto.count('o'))
print('vogal u:', texto.count('u'))

palavra = 'América'

contar = palavra.count('América')
#conta quantas vezes o string 'América' aparece.

print(contar)
#Ele deve imprimir a ocorrência


texto = texto.replace('Brasil','BRASIL')

print(texto)