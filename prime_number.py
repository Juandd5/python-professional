
def is_prime_number(number: int) -> bool:
    """This function evaluates whether "number" is a prime or not
    Args: number (int): 
    Returns: bool: The function returns True if "number" is prime or returns False if not
    """

    if number < 2 or number == 4:
        return False

    for divisor in range(2, number//2):
        if number % divisor == 0:
            return False
    
    return True


def run():
    #number = int(input('Enter a natural number: '))
    #print(f'{number} {"is" if is_prime_number(number) else "is not"} a prime number')

    print(is_prime_number(2.5)) #this line is to test mypy module


if __name__=='__main__':
    run()