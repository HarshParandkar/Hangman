import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

# Load dataset
def load_movies():
    try:
        data = pd.read_csv("top_movies.csv")  # Replace with your dataset's filename
        titles = data['Title'].dropna().tolist()  # Extract movie titles
        return [title.strip() for title in titles if isinstance(title, str)]
    except FileNotFoundError:
        messagebox.showerror("Error", "Dataset file not found!")
        return []

# Function to display the word with guessed letters
def display_word(movie, guessed_letters):
    display = ""
    for letter in movie:
        if letter.lower() in guessed_letters or not letter.isalpha():
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Initialize game variables
def start_game():
    global selected_movie, guessed_letters, attempts
    guessed_letters = []
    attempts = 6
    selected_movie = random.choice(movie_list).lower()
    update_display()

# Update display labels
def update_display():
    word_label.config(text=display_word(selected_movie, guessed_letters))
    attempts_label.config(text=f"Attempts Left: {attempts}")
    guessed_label.config(text=f"Guessed Letters: {', '.join(guessed_letters)}")

# Handle guesses
def make_guess():
    global attempts
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if not guess or len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single alphabetic character!")
        return

    if guess in guessed_letters:
        messagebox.showinfo("Already Guessed", "You already guessed that letter!")
        return

    guessed_letters.append(guess)

    if guess not in selected_movie:
        attempts -= 1

    if all(letter in guessed_letters or not letter.isalpha() for letter in selected_movie):
        messagebox.showinfo("Congratulations", f"You guessed the movie! {selected_movie}")
        start_game()
    elif attempts <= 0:
        messagebox.showinfo("Game Over", f"You lost! The movie was: {selected_movie}")
        start_game()
    else:
        update_display()

# GUI setup
app = tk.Tk()
app.title("Hangman Game")

# Load movies
movie_list = load_movies()
if not movie_list:
    app.destroy()

selected_movie = ""
guessed_letters = []
attempts = 6

# UI Elements
title_label = tk.Label(app, text="Hangman Game", font=("Arial", 24))
title_label.pack()

word_label = tk.Label(app, text="", font=("Arial", 20))
word_label.pack()

attempts_label = tk.Label(app, text="", font=("Arial", 14))
attempts_label.pack()

guessed_label = tk.Label(app, text="", font=("Arial", 14))
guessed_label.pack()

guess_entry = tk.Entry(app, font=("Arial", 14))
guess_entry.pack()

guess_button = tk.Button(app, text="Guess", font=("Arial", 14), command=make_guess)
guess_button.pack()

start_game_button = tk.Button(app, text="Start New Game", font=("Arial", 14), command=start_game)
start_game_button.pack()

start_game()

app.mainloop()
