
def decorador(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

@decorador
def saludo():
    print('Hola!')

#función decoradora que recibe a mensaje() como parámetro
def mayusculas(func): 

    #envoltura: nested function, esta recibe un parámetro al igual que mensaje. Por qué?
    #porque vamos a decorar mensaje() y cuando esto pasa se crea una nested function "envoltura"
    #que recibe los mismos parámetros que la función que estoy decorando.
    #lo mismo sucede con el return, debe retornar algo
    def envoltura(texto): 
        return func(texto).upper()
    return envoltura

@mayusculas #esto reemplaza: mensaje = mayusculas(mensaje)
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'


saludo()

print(mensaje('Luis'))
