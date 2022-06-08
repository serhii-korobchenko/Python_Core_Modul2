"""
### 1 

age = input("How old are you? ")

if int(age) >= 18:
    print("You are adult already.")
else:
    print("You are infant yet.")

### 2 
a = input('Введите число')
a = int(a)
if a > 0:
    print('Число положительное')
# bloc of code -  avoided
elif a == 1:
    print('Число равно 1')
    
else:
    print("a <= 0")

### 3

money = ""
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")
print(type(money))


### 4 Булева алгебра

name = "Taras"
age = 22
has_driver_licence = True


if name and age >= 18 and has_driver_licence:
    print(f"User {name} can rent a car")


### 5 Тернарные операции
is_nice = True
state = "nice" if is_nice else "not nice"
print(state)


some_data = ""
msg = some_data or "Не было возвращено данных"
print(msg)


### Блоки инструкций
x = int(input("X: "))
y = int(input("Y: "))

if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))

result = y / x
print(result)



x = int(input("X: "))
y = int(input("Y: "))

if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))

    if x == 0:
        print("X can`t be equal to zero")
        x = int(input("X: "))

        if x == 0:
            print("X can`t be equal to zero")
            x = int(input("X: "))

result = y / x
print(result)
"""


if x >= 0:
    if y >= 0:               # x > 0, y > 0
        print("Первая четверть")
    else:                    # x > 0, y < 0
        print("Четвертая четверть")
else:
    if y >= 0:               # x < 0, y > 0
        print("Вторая четверть")
    else:                    # x < 0, y < 0
        print("Третья четверть")