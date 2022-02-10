
def my_gen():
    """Un ejemplo de generadores"""

    print('Hello world!')
    n = 0
    yield n

    print('Hello heaven!')
    n = 1
    yield n

    print('Hello hell!')
    n = 2
    yield n


a = my_gen()

print(next(a))
print(next(a))
print(next(a))
#print(next(a))

#Usando Generator expression
my_gen2 = (i for i in range (1, 21)) #se crea un generador con los números del 1 al 20
print(my_gen2) #Imprime la dirección en memoria del generador
sum_gen = sum(my_gen2) #suma todos los números del 1 al 20, solo guarda el resultado
print(sum_gen)