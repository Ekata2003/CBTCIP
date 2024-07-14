import random

def generate_secret_number(length):
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:length]))

def get_feedback(secret, guess):
    correct_position = sum(1 for s, g in zip(secret, guess) if s == g)
    correct_digits = sum(min(secret.count(x), guess.count(x)) for x in set(guess)) - correct_position
    return correct_position, correct_digits

def play_mastermind():
    length = 2  # You can change the length of the secret number here
    player1_secret = generate_secret_number(length)
    attempts_player2 = 0

    print("Player 1 has set the secret number.")

    # Player 2 guesses
    while True:
        guess = input(f"Player 2, enter your {length}-digit guess: ")
        attempts_player2 += 1
        if guess == player1_secret:
            print(f"Player 2 guessed the number in {attempts_player2} attempts!")
            break
        correct_position, correct_digits = get_feedback(player1_secret, guess)
        print(f"Feedback: {correct_position} digits are correct and in the correct position, {correct_digits} correct "
              f"digits in the wrong position.")

    # Switch roles
    player2_secret = generate_secret_number(length)
    attempts_player1 = 0

    print("Player 2 has set the secret number.")

    # Player 1 guesses
    while True:
        guess = input(f"Player 1, enter your {length}-digit guess: ")
        attempts_player1 += 1
        if guess == player2_secret:
            print(f"Player 1 guessed the number in {attempts_player1} attempts!")
            break
        correct_position, correct_digits = get_feedback(player2_secret, guess)
        print(f"Feedback: {correct_position} digits are correct and in the correct position, {correct_digits} correct digits in the wrong position.")

    # Determine winner
    if attempts_player1 < attempts_player2:
        print("Player 1 wins and is crowned Mastermind!")
    elif attempts_player1 > attempts_player2:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_mastermind()

