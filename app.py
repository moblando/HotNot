#!/usr/bin/env python3

import tkinter as tk
import sqlite3
import threading
import time
import random

# -----------------
# Database Helper Functions
# -----------------

def get_db_connection():
    """Establish a connection to the SQLite database and use Row factory for dict-like access."""
    conn = sqlite3.connect("quiz.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_genre_by_name(genre_name):
    """
    Retrieve a subject (genre) from the database by name (case-insensitive).
    Returns a sqlite3.Row if found, or None if not found.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM subjects WHERE lower(name) = lower(?)", (genre_name,))
    genre = cur.fetchone()
    conn.close()
    return genre

def get_random_question(subject_id):
    """
    Retrieve a random question from the database for the given subject_id.
    Uses SQLite's RANDOM() function.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions WHERE subject_id = ? ORDER BY RANDOM() LIMIT 1", (subject_id,))
    question = cur.fetchone()
    conn.close()
    return question

# -----------------
# Tkinter GUI Functions
# -----------------

# Function to show the genre input screen
def show_genre_input_screen():
    # Create a new window for genre input
    window = tk.Tk()
    window.attributes('-fullscreen', True)  # Make it full screen
    window.configure(bg='black')

    # Disable the close button
    window.protocol("WM_DELETE_WINDOW", lambda: None)

    # White box where the user can interact
    frame = tk.Frame(window, bg='white', width=400, height=300)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Instructions label
    instructions_label = tk.Label(frame, text="Enter Genre (e.g., Math, Science, History):", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Text input for genre
    genre_input = tk.Entry(frame, font=("Arial", 14))
    genre_input.pack(pady=10)

    # Label for feedback
    result_label = tk.Label(frame, text="", font=("Arial", 14), fg='black')
    result_label.pack(pady=10)

    # Button to submit genre and proceed to the question screen
    def submit_genre():
        genre_name = genre_input.get().strip()
        genre = get_genre_by_name(genre_name)
        if genre:
            window.destroy()  # Close the genre input window
            show_question_screen(genre)  # Show the question screen with the selected genre
        else:
            result_label.config(text="Invalid genre. Please try again.", fg="red")

    submit_button = tk.Button(frame, text="Submit", font=("Arial", 14), command=submit_genre)
    submit_button.pack(pady=20)

    window.mainloop()

# Function to show the question screen
def show_question_screen(genre):
    # Create a new window for the question
    window = tk.Tk()
    window.attributes('-fullscreen', True)  # Make it full screen
    window.configure(bg='black')

    # Disable the close button
    window.protocol("WM_DELETE_WINDOW", lambda: None)

    # White box for question interaction
    frame = tk.Frame(window, bg='white', width=400, height=300)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Label to display the question
    question_label = tk.Label(frame, text="Please wait while we get your question...", font=("Arial", 16), wraplength=300)
    question_label.pack(pady=20)

    # Retrieve a random question for the selected genre
    question = get_random_question(genre["subject_id"])
    if question:
        question_label.config(text=f"Question: {question['question_text']}")

        # Input for the answer
        answer_input = tk.Entry(frame, font=("Arial", 14))
        answer_input.pack(pady=10)

        # Label to display feedback
        result_label = tk.Label(frame, text="", font=("Arial", 14), fg='black')
        result_label.pack(pady=10)

        # Button to check the answer
        def check_answer():
            user_answer = answer_input.get().strip()
            if user_answer.lower() == question["answer"].lower():
                result_label.config(text="Correct! You can continue.", fg="green")
                show_exit_button(window)  # Show exit button after correct answer
            else:
                result_label.config(text=f"Incorrect. The correct answer was: {question['answer']}", fg="red")

        submit_button = tk.Button(frame, text="Submit", font=("Arial", 14), command=check_answer)
        submit_button.pack(pady=20)

    window.mainloop()

# Function to display an exit button after the correct answer is given
def show_exit_button(window):
    exit_button = tk.Button(window, text="Exit", font=("Arial", 14), command=window.destroy)
    exit_button.pack(pady=20)

# -----------------
# Main Execution
# -----------------

# Delay the popup window by 10 seconds before starting the quiz
def delayed_popup():
    time.sleep(10)  # Wait for 10 seconds
    show_genre_input_screen()  # Show the genre input screen

# Start the process with a delay
delayed_popup()
