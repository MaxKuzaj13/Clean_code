import random

RANGE_OF_TRIES = range(0, 10)
MIN_RANGE_TO_GUESS = 1
guess = 0


def draw_numbers_to_guess(RANGE_OF_TRIES, MIN_RANGE_TO_GUESS, max_range_to_guess):
    a_list_of_numbers_to_guess = []
    for round_number in RANGE_OF_TRIES:
        a_list_of_numbers_to_guess.append(random.randint(MIN_RANGE_TO_GUESS, max_range_to_guess))

    return a_list_of_numbers_to_guess


def ask_for_guess(MAX_RANGE_TO_GUESS):
    exit_value = False
    while exit_value != True:
        try:
            guess = int(input(f"Enter an integer from {MIN_RANGE_TO_GUESS} to {MAX_RANGE_TO_GUESS}: "))
            exit_value = True
        except ValueError:
            print('Pleas enter correct integer')

    return guess


def game_initiation(RANGE_OF_TRIES, a_list_of_numbers_to_guess, guess, max_range_to_guess):
    for number_shots in RANGE_OF_TRIES:
        while a_list_of_numbers_to_guess[number_shots] != guess:
            guess = ask_for_guess(max_range_to_guess)
            if guess < a_list_of_numbers_to_guess[number_shots]:
                print("guess is low")
            elif guess > a_list_of_numbers_to_guess[number_shots]:
                print("guess is high")
            else:
                break
            # if next number is the same we have to change it
            guess = 0
        print("you guessed it!")


def main():
    max_range_to_guess = 99
    a_list_of_numbers_to_guess = draw_numbers_to_guess(RANGE_OF_TRIES, MIN_RANGE_TO_GUESS, max_range_to_guess)
    print(a_list_of_numbers_to_guess)
    game_initiation(RANGE_OF_TRIES, a_list_of_numbers_to_guess, guess, max_range_to_guess)
    # changing max of range to second game
    max_range_to_guess = 49
    a_list_of_numbers_to_guess = draw_numbers_to_guess(RANGE_OF_TRIES, MIN_RANGE_TO_GUESS, max_range_to_guess)
    print(a_list_of_numbers_to_guess)
    game_initiation(RANGE_OF_TRIES, a_list_of_numbers_to_guess, guess, max_range_to_guess)


if __name__ == '__main__':
    main()


