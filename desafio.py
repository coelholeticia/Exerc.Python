# exercicio 1 função que retorna o maior valor de uma lista
def amplitude ():
    number = [2, 4 ,6, 8, 10]
    print(max(number))
    
#amplitude()

#Exercicio 2

def string_vertical():
   print(*input('Digite alguma coisa '), sep="\n")

    
#string_vertical()

#exercio 3

peso = int(input('Qual o peso da cerga ?'))

if peso <= 10:
    print('O valor é de R$ 50.00')
elif peso >= 11 and peso <=20:
    print('O valor é de R$ 80.00')
else:
    print('O valor do peso não é aceito.')
 



