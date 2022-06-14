import random

while True:
    random_number = random.randint (1,3)
    users_bet = input("Enter your bet: Red, Black or Zero")

    if users_bet == random_number:
        print('Well Done! You won!')
        break
    else:
        print('Sorry Gay! You lost! Try again!')