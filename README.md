Perfect Guess Game
Overview: The Perfect Guess game is a simple yet engaging number-guessing game developed in Python. The objective is to guess a randomly generated number between 1 and 100. Players receive feedback on their guesses, which helps them refine their attempts.

Code Description:

Random Number Generation:

The game utilizes the random module to generate a random integer 
𝑋
X between 1 and 100.
User Input:

Players are prompted to guess the number. The program checks if the guess matches the randomly generated number.
Feedback Mechanism:

If the player's guess is correct, the program celebrates their success with a playful message using the cowsay library.
If the guess is too high, a "too high" message is displayed using a dragon character from the cowsay library.
If the guess is too low, a "too low" message is shown using a cow character from the cowsay library.
Attempts Tracking:

The game keeps track of the number of attempts the player makes before guessing the correct number. After the player successfully guesses the number, the total number of attempts is displayed.
Loop Until Correct Guess:

The game continues to prompt the player for guesses until they successfully guess the correct number.
Gameplay Experience: The Perfect Guess game is designed to be intuitive and fun, allowing players to enjoy the thrill of guessing while receiving playful feedback. The attempts tracking feature adds an extra layer of challenge, encouraging players to improve their guessing strategy with each attempt.

