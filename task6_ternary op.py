"""
Выполните задание, для определения четное число или нет, с помощью тернарного оператора.
Программа устанавливает значение переменной is_even в True или False, 
в зависимости от того, является ли число в переменной num четным или нечетным.
Подсказка: проверка на четность выполняется сравнением остатка от деления на 2 с 0 или 1. 
Напомним, остаток от деления можно получить после операции %

"""
num = int(input("Enter an integer number: "))

is_even = False if num % 2 else True
print(is_even)