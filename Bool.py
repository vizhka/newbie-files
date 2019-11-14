#Boolean and comprasion

# Больше чем 3 > 6 - False
# Меньше чем 3 < 5 - True
# Больше чем или равно 2 >= 2 - True
# Меньше чем или равно 3 <= 5 - True
# Равно 3 == 3 - True
# 4 == '4' - False
#'Hi' == 'Bye' - False
# Не равно 2 != 2 - False
# x in list 2 in [1,2,4] - True
# x not in list
# and оба операнда должны иметь одно значение
# or если хотя бы один операнд истинный, то и его значение TRUE
# not
truthy = True
falsy = False
age = 20
is_over_age = age >= 18
print(is_over_age)
is_under_age = age <=18
print(is_under_age)
is_twenty = age == 20
print(is_twenty)

my_number = 5
user_number = int(input("Enter a number: "))
print(my_number == user_number)
print(my_number != user_number)
Yes = True and True
No = True and False
print(No)


#кортежи неизменяемый тип данных
'''
tuple = ()
t1 = (1,2,3)
t1[0]
t2 = (3,)
t3 = ('a', True, 123)
t3[0] = 'b'
str, b, num = t3
'''

#множества изменяемый тип данных
x = set()
x.add(1)
x.add(2)
x.add(3)
x.add(3.14)
print(x)

words = ['hi', 'hi', 'Peter']
set(words)
print(set(words))
converted = set([1, 2, 3, 1, 2, 4, 5, 2, 2, 2, 3, 3, 3])
print(converted)