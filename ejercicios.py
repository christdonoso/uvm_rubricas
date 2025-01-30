'''
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''

#palabra = input('Dime una palabra: ')   

#bucles
#bucles for:consume un iterable [nibaldo]
'hola mundo'

# for letra in 'hola mundoOOOOOOOOOOOOO':
#     print(palabra)

#bucles while: se ejecuta mientra se cumpla una condicion

# numero = 1

# while numero != 10:
#     print(numero)
#     numero = numero + 1



'''
Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla la cuenta atrás desde ese número hasta cero.
'''

#1.- pedir al usuario un numero entero positivo
#pedir numero al usuario
numero = input('Dime un numero entero positivo: ')

#confirmar que el numero sea entero:
if numero.isdigit():
    #confirmar que el numero sea positivo
    if int(numero) > 0:
    #2.- operacion del bucle
        numero = int(numero)
        for _ in range(numero):
            numero = numero - 1
            print(numero)
    else:
        print('Escriba un numero entero positivo')
else:
    print('ingresa un numero')
