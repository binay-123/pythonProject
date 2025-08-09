import random
words = ["python", "computer", "Laptop", "developer", "programming"]
word = random.choice(words)
word_letters = list(word)
blanks = ["_"] * len(word)
lives = 6
print("Welcome to the Word Guessing Game!")
print(" ".join(blanks))

while True:
    guess = input("Guess a letter: ").lower()
    if guess in word_letters:
        # Replace blanks with the letter
        for i, letter in enumerate(word_letters):
            if letter == guess:
                blanks[i] = guess
        print("You win!")
    else:
        lives -= 1
        print(f"Wrong! Lives remaining: {lives}")

    print(" ".join(blanks))
    if "_" not in blanks:
        print("🎉 You guessed the word! You win!")
        break
    if lives == 0:
        print(f"💀 You ran out of lives! The word was '{word}'.")
        break


