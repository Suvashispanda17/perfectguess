#Perfect Guess Game in Python
Overview:

The Perfect Guess game is a simple yet fun number-guessing game built using Python. The objective is to guess a randomly generated number between 1 and 100. Players receive feedback on their guesses, helping them to refine their attempts.

Code Description:

Random Number Generation: The game utilizes the random module to generate a random integer 
𝑋
X between 1 and 100.

User Input: Players are prompted to guess the number. The program checks if the guess matches the randomly generated number.

Feedback Mechanism:

If the player's guess is correct, the program celebrates their success with a playful message using the cowsay library.
If the guess is too high, a "too high" message is displayed using a dragon character.
If the guess is too low, a "too low" message is shown using a cow character.
Loop Until Correct Guess: The game continues to prompt the player for guesses until they successfully guess the correct number.
