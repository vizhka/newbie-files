# Объявление функции
def my_func(x, y, my_string='Python'):
    #pass # тело функции
    '''
    THIS IS DOCSTRING
    '''
    print(my_func('hello', 'peter'))
    print('My first {} function!'.format(my_string))

def func(*args):
    return args
print(func(2,7,True,44))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def even(num):
    return num % 2 == 0
evens = filter(even, l)
print(list(evens))

lambda num: num % 2 == 0
evens2 = filter(lambda num: num% 2 == 0, l)
print(list(evens2))