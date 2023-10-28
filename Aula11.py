                      #AULA 11 - FUNÇÃO LAMBDA (map(), filter(), e reduce())

#Exemplo com map(): Pode-se usar qualquer função matematica após o X
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x +4, numeros))
print(quadrados)  # Saída: [1, 4, 9, 16, 25]

#Exemplo com filter(): Após o X, numeros dividos por 2, com resto = 0. Mas pode-se alterar para qualquer outro numero.)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = list(filter(lambda x: x % 3 == 1 , numeros))
print(number)  # Saída: [2, 4, 6, 8, 10]

#Exemplo com reduce(): - A função `reduce()` é usada para aplicar uma função acumuladora a uma sequência de elementos, reduzindo-a a um único valor acumulado. Para usar `reduce()`, você precisa importá-lo do módulo `functools`.

from functools import reduce
numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # Saída: 15


#Exercicios 

1 - Crie uma função lambda que retorne o dobro de um número.
db = lambda x: x *2
dobro = int(input('Digite um numero, para saber qual é o dobro dele: '))
print(db(dobro))

# 2 - Crie uma função lambda que calcule a soma de dois números.
soma = lambda x,y : x+y 
soma = int(input('Digite um numero: '))
soma2 = int(input('Digite outro numero: '))
print(soma+soma2)

3 - Crie uma função lambda que verifique se um número é par.


# 5 - Crie uma função lambda que calcule o produto de três números.
produto = lambda x,y,z: x*y*z
print(produto(2,3,4))
