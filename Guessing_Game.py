import random


def guess_number_function(guess_number,answer):
    
    if (0<guess_number<10):
        if guess_number == answer:
            print("You Guessed Correctly")
            return True
        elif guess_number>answer:
            print("Your getting away from anwser")
        elif guess_number>answer:
            print("Your getting away from anwser")
    else:
        print("I said guess number should be 0~9")
        return True
        

answer = random.randint(0, 9)
while True:
    try:
        guess_number = int(input("Enter a Guessing_number(0~9): "))
        if guess_number_function(guess_number,answer):
            break

    except Exception as e:
        print(f'You got an {e} error.')
            
