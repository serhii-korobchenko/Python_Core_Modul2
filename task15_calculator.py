"""Напишите программу, которая будет выполнять простейшие математические операции с числами последовательно, 
принимая от пользователя операнды (числа) и оператор.

Условия приёмки
Приложение работает с целыми и дробными числами.
Приложение умеет выполнять такие математические операции:
СЛОЖЕНИЕ (+)
ВЫЧИТАНИЕ (-)
УМНОЖЕНИЕ (*)
ДЕЛЕНИЕ (/)
Приложение принимает один операнд или один оператор за один цикл запрос-ответ.
Все операции приложение выполняет по мере поступления — одну за одной.
Приложение выводит результат вычислений, когда получает от пользователя =.
Приложение заканчивает свою работу после того, как выведет результат вычисления.
Пользователь по очереди вводит числа и операторы.
Если пользователь вводит оператор два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
Если пользователь вводит число два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
Приложение корректно обрабатывает ситуацию некорректного ввода (exception).

result — сюда помещаем итоговый результат 
operand — всегда хранит текущее число 
operator — строковый параметр, может содержать четыре значения, "+", "-", "*", "/" 
wait_for_number — флаг, который указывает, что ожидают на вводе, оператор (operator) или операнд (operand)

Тестовые последовательности:

Первая: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "="], результат 18.0
Вторая: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0

Очикуємо:
=> 10
=> +
=> 5
=> 6
6 is not '+' or '-' or '/' or '*'. Try again
=> /
=> 3
=> -
=> a
'a' is not a number. Try again.
=> 2
=> *
=> 6
=> =
Result: 18.0
"""




result = None # сюда помещаем итоговый результат 
operand = None # всегда хранит текущее число 
operator = None #строковый параметр, может содержать четыре значения, "+", "-", "*", "/" 
wait_for_number = True # флаг, который указывает, что ожидают на вводе, оператор (operator) или операнд (operand)

while True:
    try:
        input_kursor = input(">>> ")
        input_kursor_int = int(input_kursor)
        if wait_for_number == False:
            print(f"'{input_kursor_int}' is not '+' or '-' or '/' or '*'. Try again")
        
        operand = input_kursor_int

        if operator == '+' and wait_for_number == True:
            result = result + operand
        elif operator == '-' and wait_for_number == True:
            result = result - operand
        elif operator == '*' and wait_for_number == True:
            result = result * operand
        elif operator == '/' and wait_for_number == True:
            result = result / operand
        elif wait_for_number == True:
            result = operand
        
            
        wait_for_number = False
       
        #print (wait_for_number)
    except ValueError:
        if input_kursor == '+' and wait_for_number == False :
            operator = "+"
            #result = result + operand
        elif input_kursor == '-' and wait_for_number == False:
            operator = "-"
            #result = result - operand
        elif input_kursor == '*' and wait_for_number == False:
            operator = "*"
            #result = result * operand
        elif input_kursor == '/' and wait_for_number == False:
            operator = "/"
            #result = result / operand
        elif input_kursor == '=' and wait_for_number == False:
            print(f"Result: {result}")
            break
        else:
            print(f"'{input_kursor}' is not a number. Try again.")
        
        wait_for_number = True
        #print (wait_for_number)
        
    
    finally:
        None
        #print(f"operand - {operand} operator - {operator}")
        #print(f"result: {result}")
        

    

    
    
  
