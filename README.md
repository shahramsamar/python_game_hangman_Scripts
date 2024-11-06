# Python Hangman Game

A Python implementation of the classic Hangman game. The player tries to guess a word by suggesting letters, and the game continues until the player guesses the word or runs out of attempts.

## Features

- **Word Guessing**: The player guesses letters to form a word.
- **Limited Attempts**: The player has a fixed number of attempts before the game ends.
- **Interactive Interface**: A simple terminal interface that provides feedback on guesses.

## Requirements

- **Python 3.x**

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/python_game_hangman_Scripts.git
    cd python_game_hangman_Scripts
    ```

2. **Run the Game:**

    ```bash
    python hangman.py
    ```

### How to Play

- The game selects a random word from a list.
- The player is prompted to guess one letter at a time.
- After each guess, the program shows the current progress of the word with underscores for unguessed letters.
- The player has a limited number of incorrect guesses before the game is lost.
- The game ends when the word is guessed or the player runs out of attempts.

### Project Structure

- `hangman.py`: The main script containing the logic for the Hangman game.
- `requirements.txt`: A list of any additional dependencies if required.

## Contributing

Feel free to fork the project and submit pull requests for new features, bug fixes, or improvements.

## License

This project is open-source and available for educational purposes.
