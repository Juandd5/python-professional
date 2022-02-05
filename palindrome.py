"""This programa is for testing the mypy module
    you have to use the next command in your shell
    mypy palindrome.py --check-untyped-defs
"""

def is_palindrome(string: str) -> bool:
    string = string.replace(' ','').lower() #I delete spaces
    return string == string[::-1]


def run():
    #string = input('Enter a word o sentence: ')
    #print(f'This string {"is" if is_palindrome(string) else "is not"} a palindrome!')

    print(is_palindrome(100))


if __name__=='__main__':
    run()