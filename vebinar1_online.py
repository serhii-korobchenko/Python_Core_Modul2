""" name = ''
while True:
    name = input("Who are you? ")
    if name != "Jack":
        continue
    print("Hello Jack. What is the password?")
    password = input("Plase set password")
    if password == "secret":
        break
print("Ok") """


""" i = 0
while i<5:
    print(f'Itration: {i}')
    i+=1 """

""" for item in range (16, 0, -2):
    print(f'Itration: {item}') """



for index, value in enumerate("test", 1):   # Як працює?
    print(f'Index: {index} - Value {value}')