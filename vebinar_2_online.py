""" # Exceptions
result = 0
try:
    value_1 = int(input('Please set first value: '))
    value_2 = int(input('Please set second value: '))
    result =  value_1 / value_2
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as err:
    print(f"Somethink is broken. Error is:  {err}") """

""" # Cycle work demonstration
for item in range(10):
    for new_item in range(10):
        print(f"new_item is {new_item}")
        if new_item == 5:
            print("it's break inside `new_item` cyclic")
            break
        else:
            print("it's continue inside `new_item` cyclic")
            continue
    print(f"item is {item}")
    if item == 8:
        print("it's break inside `item` cyclic")
        break
    else:
        print("it's continue inside `item` cyclic")
        continue """

""" Задача 3. Напишіть програму, яка зчитує цілі числа з консолі по одному числу в рядку.
 Для кожного введеного числа перевірити:
● якщо число менше 10, то пропускаємо це число;
 ● якщо число більше 100, то припиняємо зчитувати числа;
 ● в інших випадкахв ивести це число назад на консоль в окремому рядку. """

""" while True:
    try:
        number = int(input("Please set value: "))
    except ValueError as e:
        print(f"We catch ValueError {e}")
    if number < 10:
        continue
    elif number > 100:
    
        break
        print(number) """

""" # Задача 4. Напишіть програму, яка зчитує з клавіатури два числа a та b, рахує та виводить в
# консоль середнє арифметичне всіх чисел з відрізка [a; b], які кратні числу 3.
# консоль середнє арифметичне всіх чисел з відрізка [2; 10], які кратні числу 3.
# a, b = [int(input()) for i in range(2)]
a = int(input("Please set 'a'"))
b = int(input("Please set 'b'"))
counter, sum = 0, 0

for item in range(a, b+1):
    if item % 3 == 0:
        counter = counter + 1
        # counter = 1 + 1 + 1
        sum = sum + item
        # sum = 3 + 6 + 9
print(sum / counter) """


""" Задача 5. Відбувається турнір між розробниками Java i Python. 
Переможець отримає торт. У команді Java - X людей, а команді Python
Y людина. Потрібно заздалегідь розрізати пиріг таким чином, щоб можна було 
роздати шматочки пирога будь-якій команді, яка виграла змагання, при цьому кожному учаснику 
цієї команди має дістатися однакова кількість шматочків торта. І так як не хочеться різати пиріг 
на занадто дрібні шматочки, потрібно знайти мінімальне відповідне число. Напишіть програму, 
яка допомагає знайти це число.
Програма повинна зчитувати розміри команд (два позитивні цілі числа  Х i  Y, 
кожне число вводиться на окремому рядку) і виводити найменше число d, яке ділиться 
на обидва ці числа без залишку. """

""" x = int(input("Set first team: "))
y = int(input("Set second team: "))
d = 1  # к-сть кусочків торта
while True:
    if d % x == 0 and d % y == 0:
        break
    else:
        d += 1
print(d) """









