import tkinter as tk
from tkinter import messagebox
import sqlite3
import threading
import time
import pyautogui


#testing
#-----

import random


# Mock data to replace database interaction
genres = [
    {"id": 1, "name": "Math"},
    {"id": 2, "name": "Science"},
    {"id": 3, "name": "History"},
]

questions = [
    {"genre_id": 1, "question_text": "What is 2+2?", "correct_answer": "4"},
    {"genre_id": 2, "question_text": "What is H2O?", "correct_answer": "Water"},
    {"genre_id": 3, "question_text": "Who was the first president of the United States?", "correct_answer": "George Washington"},
]

# Function to get a random genre based on user input
def get_genre_by_name(genre_name):
    for genre in genres:
        if genre_name.lower() == genre['name'].lower():
            return genre
    return None

# Function to get a random question based on genre
def get_random_question(genre_id):
    filtered_questions = [q for q in questions if q["genre_id"] == genre_id]
    return random.choice(filtered_questions) if filtered_questions else None

# Function to show the genre input screen
def show_genre_input_screen():
    # Create a new window for genre input
    window = tk.Tk()
    window.attributes('-fullscreen', True)  # Make it full screen
    window.configure(bg='black')

    # Make it so the window can't be closed
    window.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button

    # White box where the user can interact
    frame = tk.Frame(window, bg='white', width=400, height=300)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Instructions label inside the white box
    instructions_label = tk.Label(frame, text="Enter Genre (e.g., Math, Science, History):", font=("Arial", 14))
    instructions_label.pack(pady=10)

    # Text input for genre
    genre_input = tk.Entry(frame, font=("Arial", 14))
    genre_input.pack(pady=10)

    # Result label for showing feedback
    result_label = tk.Label(frame, text="", font=("Arial", 14), fg='black')
    result_label.pack(pady=10)

    # Button to submit genre and go to question screen
    def submit_genre():
        genre_name = genre_input.get().strip()
        genre = get_genre_by_name(genre_name)

        if genre:
            window.destroy()  # Close genre input window
            show_question_screen(genre)  # Show the question screen
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

    # Make it so the window can't be closed
    window.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button

    # White box where the user can interact
    frame = tk.Frame(window, bg='white', width=400, height=300)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Instructions label inside the white box
    question_label = tk.Label(frame, text="Please wait while we get your question...", font=("Arial", 16), wraplength=300)
    question_label.pack(pady=20)

    # Get a random question for the selected genre
    question = get_random_question(genre["id"])

    if question:
        question_label.config(text=f"Question: {question['question_text']}")

        # Text input for answer
        answer_input = tk.Entry(frame, font=("Arial", 14))
        answer_input.pack(pady=10)

        # Result label for showing feedback
        result_label = tk.Label(frame, text="", font=("Arial", 14), fg='black')
        result_label.pack(pady=10)

        # Button to check the answer
        def check_answer():
            user_answer = answer_input.get().strip()

            if user_answer.lower() == question["correct_answer"].lower():
                result_label.config(text="Correct! You can continue.", fg="green")
                show_exit_button(window)  # Show the exit button
            else:
                result_label.config(text=f"Incorrect. The correct answer was: {question['correct_answer']}", fg="red")

        submit_button = tk.Button(frame, text="Submit", font=("Arial", 14), command=check_answer)
        submit_button.pack(pady=20)

    window.mainloop()

# Function to display an exit button after the correct answer is given
def show_exit_button(window):
    # Create an exit button
    exit_button = tk.Button(window, text="Exit", font=("Arial", 14), command=window.destroy)
    exit_button.pack(pady=20)

# Delay the popup window by 10 seconds
def delayed_popup():
    time.sleep(10)  # Wait for 10 seconds before showing the popup
    show_genre_input_screen()  # Show the genre input screen

# Start the process by delaying the popup
delayed_popup()


#------------