
def decorador(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

@decorador
def saludo():
    print('Hola!')


def mayusculas(func): #función decoradora que recibe a mensaje() como parámetro
    def envoltura(texto): #nested function, esta recibe un texto al igual que mensaje
        return func(texto).upper()
    return envoltura

@mayusculas #esto reemplaza: mensaje('Luis'); mensaje = mayusculas(mensaje)
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'


saludo()

print(mensaje('Luis'))
