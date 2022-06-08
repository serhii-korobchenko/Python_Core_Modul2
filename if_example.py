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


x=int(input("Enter X:"))
y=int(input("Enter Y:"))


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
#print("This is border position")



### Цикли
fruit = 'apple'
for char in fruit:

    print(char)



a = 1
while a <= 10:
    print(a)
    a = a + 1

a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1



while True:
    user_input = input()
    print(user_input)
    if user_input == "exit":
        break

a = 0
while a < 6:
    a = a + 1
    print(a)
    if not a % 2:
        
        continue
    print(f"Умова не спрацювала а={a}")


while True:
    number = input("number = ")
    number = int(number)
    while True:
        print(number)
        number = number - 1
        if number < 0:
            break





### Исключения
val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")

"""

while True:
    age = input("How old are you? ")
    try:
        age = int(age)
        if age >= 18:
            print("You are adult.")
        else:
            print("You are infant")
    except ValueError:
        print(f"{age} is not a number")
        if age == 'exit':
            break

