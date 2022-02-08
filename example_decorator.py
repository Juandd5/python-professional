# modulo para trabajar con fechas
from datetime import datetime

#con este decorardor puedo saber cuánto tarda en ejecutarse una función
def execution_time(func):
    def wrapper(*args, **kwargs):
        #el método now() devuelve la fecha y hora exacta del momento en el que se ejecuta
        initial_time = datetime.now() 
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        #el método total_seconds() permite obtener el total de segundos de la diferencia de tiempo
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper

#*args: No importa la cantidad de argumentos posicionales que se le envíen, la función los recibe
#**kwargs: No importa la cantidad de argumentos nombrados que se le envíen, la función los recibe

@execution_time
def random_func():
    #Cuando hacemos un ciclo for y no nos interesa obtener el valor que se está iterando
    #se suele poner _
    for _ in range(1, 10000000):
        pass #con esto solo vemos cuánto tarda un for en dar 10'000.000 de vueltas

@execution_time
#Estos son parámetros posicionales
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
#estos son parámetros nombrados. Ya tienen un valor por defecto 
def saludo(nombre = 'Carlos'):
    print(f'Hola {nombre}')


random_func()
suma(5, 2)
saludo('Juan')
