""" while True:

    try:

        user_input = int(input('How old are you? ')) 
    
    except ValueError as error:

        print(f'Incorrect value, should be {error}')
    else:

        break

current_year = 2022
year_of_birth = current_year - user_input 
print (year_of_birth) """


""" user_input = int(input('How old are you? ')) 

if user_input <=18:
    try:    
        raise ValueError ('You are not allowed')
    except ValueError as error:
        print(f'{error}')  """


""" # Nymber of Febanachi
result = 0 
number1 = 0

for i in range (0, 10):
    result = i+number1
    number1 = result

    print(result) """

""" Задание
Благодаря интенсивному маркетингу ваш стартап привлекает все больше людей. 
Сейчас вам поступило целых 10 заказов.

Работники могут сделать 5 продуктов за один час, однако, из-за интенсивности работы, 
каждый час скорость производства домов уменьшается на 1.

Вам нужно посчитать, за сколько часов работники смогут выполнить заказ или через 
сколько часов их продуктивность упадет до О.

•	speed - количество продуктов в час.
•	hours_passed - количество прошедших часов.
•	product_count - количество продуктов, которое надо сделать.
Выполните задачу при помоши цикла while .
 """
""" while True:
    try:
        number = int(input("Enter number: "))
        if number == 0:
            break 
        if number%2:
            print ("Odd")
        else:
            print ("Even")

    except ValueError:
        print("It is not number") """


text = input('Your text: ') 
word = ''

for char in text:

    if char == ' ':
        print(word) 
        word = ' '
    else:
        word += char

print(word)

