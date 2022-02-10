# si tenemos [1, 1, 2, 2, 4] → retornará [1, 2, 4]

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

#Otra forma
def remove_duplicates_sets(some_list):
    return list(set(some_list))


if __name__ == '__main__':

    ramdon_list = [1, 1, 2, 2, 4]
    print(remove_duplicates_sets(ramdon_list))