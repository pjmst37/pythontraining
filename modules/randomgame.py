import sys
from random import randint

start_range = int(sys.argv[1])
end_range = int(sys.argv[2])

# start_range = 1
# end_range = 10


random_num = randint(start_range, end_range)

print(random_num)
TRIES = 0

while True:
    try:
        user_guess = int(
            input(f"Pick a number between {start_range} and {end_range}! ")
        )

        if start_range <= user_guess <= end_range:
            if user_guess == random_num:
                print(f"Congrats! You guessed it!  It took you {TRIES} tries")
                break
            print("Sorry, you'll have to try again :-(")
            TRIES += 1
        else:
            print(
                f"You need to enter a number between {start_range} and {end_range}"
            )
    except ValueError:
        print('Please enter a valid number')
