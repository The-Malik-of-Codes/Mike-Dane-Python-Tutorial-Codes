secret_word = "Mus tech"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("You win")

while guess != secret_word:
    guess = input("Enter guess: ")
    guess_count += 1

print("You win")

secret_word = "Mus tech"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

    print("You win")

secret_word = "Mus tech"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE, LOSER.0")
else:
    print("You win")
