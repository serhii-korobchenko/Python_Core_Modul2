"""
Перепишите пример из теории, но для положительного числа проверяйте — четное оно или нет. 
Таки образом после проверок переменная result должна содержать одно из четырех значений:
"Positive even number"
"Positive odd number"

"""

num = int(input("Enter a number: "))

if num >0:
    if num%2:
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num <0:
    result = "Negative number"
else:
    result = "It is zero"

print(result)