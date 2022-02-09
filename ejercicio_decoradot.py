
def show_operation(operation):
    def decorator(func):
        def wrapper(*args):
            return f'El resultado de la {operation} es: {func(*args)}'
        return wrapper
    return decorator

@show_operation('suma')
def sum(*args):
    result = 0
    for number in args:
        try:
            result += number
        except TypeError:
            print('You cannot add a number with a "str"')
            result += 0
    return result

@show_operation('resta')
def subtraction(*args):
    result = 0
    for number in args:
        try:
            result -= number
        except TypeError:
            print('You cannot subtracting a number with a "str"')
            result += 0
    return result


if __name__=='__main__':
    
    print(sum(2, 9, 5))
    print(subtraction(10, 6, 2))