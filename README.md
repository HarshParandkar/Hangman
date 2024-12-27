# Hangman

## Description:
This is a Python-based Hangman game where users guess movie titles as the hidden words. The game dynamically loads movie titles from a dataset of movies for a more engaging experience. The game is implemented using Tkinter for the graphical user interface.

## Features
- Dynamic Word Pool: Loads movie titles from a Kaggle dataset.
- Graphical Interface: Built using Tkinter for an intuitive and user-friendly experience.
- Custom Messages: Provides feedback on guesses, warnings for invalid inputs, and end-game notifications.
- Automatic Restart: Starts a new game after a win or loss.
- Randomized Movies: Ensures unique and engaging gameplay every time.

### Dataset File: top_movies.csv

## How to Run the Project
### Clone the Repository:
```
git clone https://github.com/yourusername/hangman-movie-game.git
cd hangman-movie-game
```
### Install Required Libraries: Ensure pandas is installed:
```
pip install pandas
```
### Add the Dataset:
- Place the Kaggle dataset given in the repository in the project folder and name it top_movies.csv. You can modify the filename in the code if your dataset has a different name.

### Run the Program:
- Execute the Python script:
```
python hangman_game.py
```
### Play the Game:
- Click "Start New Game" to begin.
- Enter guesses in the input box and click "Guess".
- Win by correctly guessing the movie or lose when you run out of attempts.

## How It Works
### Loading the Dataset:
- The pandas library reads the top_movies.csv file.
- Movie titles are extracted from the Title column and cleaned.
### Game Logic:
- A random movie is chosen for each round.
- The player guesses letters to reveal the movie title.
- Feedback is provided for correct and incorrect guesses.
### Restart:
- The game restarts automatically after a win or loss.
