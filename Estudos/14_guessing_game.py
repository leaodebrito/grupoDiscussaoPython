
correct_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess a number from 1 to 10: "))
    guess_count += 1
    if guess == correct_number:
        print("That's right")
        break
    else: 
        print("Try again")
else:
    print("sorry, you failed")
    