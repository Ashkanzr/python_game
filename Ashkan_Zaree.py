# Query:
# ContextLines: 1

import random  # Import the random library for generating a random number
import time  # Import the time library for measuring the time taken to play the game

# Generate a random number between 1 and 100


def generated_number():
    return random.randint(1, 100)

# Play the guessing game


def play_game():
    # Generate a random number
    number = generated_number()
    # Initialize the guesses counter to 0
    guesses = 0
    while True:
        # Prompt the user to enter a guess
        guess = input("Guess the number between 1 and 100 (or q to quit): ")
        # Check if the user wants to quit the game
        if guess.lower() == "q":
            print("Quitting game...")
            break
        try:
            # Convert the user's input to an integer
            guess = int(guess)
        except ValueError:
            # Handle any errors if the input cannot be converted to an integer
            print(
                "Invalid input. Please enter a number between 1 and 100 (or q to quit).")
            continue

        # Increment the guesses counter
        guesses += 1
        if guess == number:
            # If the user guesses the number correctly, print a congratulatory message and exit the loop
            print("Congratulations! You guessed the number in", guesses, "guesses!")
            break
        elif guess < number:
            # If the user's guess is too low, print a message to try again
            print("Your guess was too low. Try again!")
        else:
            # If the user's guess is too high, print a message to try again
            print("Your guess was too high. Try again!")


# Start the timer and play the game
start_time = time.time()
play_game()
# Stop the timer and display the time taken to play the game
end_time = time.time()
print("Time taken to play the game: {:.2f} seconds".format(
    end_time - start_time))
