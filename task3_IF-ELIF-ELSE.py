"""
Как известно, обычно разработчиков принято делить на три категории: Джун (Junior) — младший специалист, 
Мидл ( Middle) — основной разработчик в компании и Сеньйор (Senior) — старший разработчик. 
Ориентировочно можно считать, что до 1 года работы включительно — это Джуниор, больше 5 лет — это Сеньйор разработчик, 
а с одного года до 5 включительно — мидл.
Есть переменная work_experience, определяющая стаж работы программиста. 
В зависимости от стажа работы, присвоить переменной developer_type значение "Junior", 
"Middle" или "Senior". Используйте, если необходимо, булевы операторы ** or** и and при проверке.
"""
### Endless cycle, stop: -1
while True:
      

    work_experience = int(input("Enter your full work experience in years: "))

    if work_experience > 1 and work_experience <=5 :
        developer_type = "Middle"
    elif work_experience <=1 :
        developer_type = "Junior"
    else:
        developer_type = "Senior"
    print(developer_type)

    if work_experience < 0:
            break


