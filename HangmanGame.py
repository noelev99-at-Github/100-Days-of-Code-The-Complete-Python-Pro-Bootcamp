print("HangMan Game")

wordToGuess = "tree"

def guessLetter():
    letter = input("Letter: ")
    return letter.lower()

# Initialize the list with underscores for each letter in the word
correctLetters = []
for _ in wordToGuess:
    correctLetters.append("_")

print("Word is: ")
for x in correctLetters:
    print(x)

mistakes = 7
while mistakes > 0:
    letter = guessLetter()

    if letter in wordToGuess:
        for i in range(len(wordToGuess)):
            if wordToGuess[i] == letter:
                correctLetters[i] = letter

        # Print the word with guessed letters revealed
        print(" ".join(correctLetters))  
        print("\n")

        # Check if the word is completely guessed
        if "_" not in correctLetters:
            print("Congratulations, you guessed the word!")
            break
    else:
        mistakes -= 1
        print("Wrong Guess")
        notice = f"You only have {mistakes} mistakes left\n"
        print(notice)

    # Check if the user ran out of mistakes
    if mistakes == 0:
        print("Game Over! The word was:", wordToGuess)
