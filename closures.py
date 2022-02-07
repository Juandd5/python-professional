
def make_repeater_of(times: int):

    def repeater(string: str):
        assert type(string) == str, 'Solo puedes utilizar cadenas'
        return string * times
    return repeater


def make_division_by(divisor: int):

    def division(dividend: int):
        try:
            return dividend / divisor
        except:
            return 'You cannot divide by zero'
    return division

#también puedo usar lambda function, pero si quiero usar tipado estático esta no me lo permite
def division_by(divisor: int):
    return lambda dividend: dividend / divisor


def run():
    
    repeat_3 = make_repeater_of(3) #repeat_3 va a recordar el valor de times=3
    repeat_5 = make_repeater_of(5)

    print(repeat_3('Platzi'))
    #print(repeat_5(5)) #Error porque debo pasar un string como parámetro

    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_0 = make_division_by(0)
    print(division_by_0(50))

    division_by_2 = division_by(2)
    print(division_by_2(10))
    

if __name__=='__main__':
    run()