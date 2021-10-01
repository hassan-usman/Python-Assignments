number = 6
guess_count = 0
guess_limit = 3
while guess_count < guess_limit :
    guess_number = int(input("Guess: "))
    guess_count += 1
    if guess_number == number:
        print("You won!")
        break
else:
    print("Sorry you fail")






























































































