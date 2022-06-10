"""
Ситуация простая, вам необходимо высчитать количество SMS, которые надо отправлять в одном пакете рассылки потенциальным покупателям. 
Всего в день выделяется 1000 платных SMS для кампании маркетинга pool = 1000. 
Сотрудник отдела маркетинга вводит количество рассылок quantity и 
вы высчитываете размер пакет chunk = pool // quantity. Обработайте ошибку деления на ноль.
"""

pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
except ZeroDivisionError:
    print('Divide by zero completed!')
else:
    print(f"Quantity of packages - {chunk}")
finally:
    print("Goodbay!")

