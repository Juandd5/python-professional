import time
from typing import Counter

def fibo_generator(n=None):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if not n or counter < n:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield aux
        else:
            raise StopIteration

#otra forma mucho más corta
def fibo_generator2(n=None):
    n1 = 0
    n2 = 1
    counter = 0
    while not n or counter < n:
        yield n1
        n1, n2 = n2, n1+n2
        counter += 1


if __name__ == '__main__':
    fibonacci = fibo_generator(10)
    fibonacci2 = fibo_generator2(6)

    for element in fibonacci2:
        print(element)
        time.sleep(0.5)

