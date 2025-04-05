import tkinter as tk
from tkinter import messagebox
import sqlite3
import threading
import time

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('quizflix.db')  # Update with your actual database path
    conn.row_factory = sqlite3.Row
    return conn

# Function to get the genres from the database
def get_genres():
    conn = get_db_connection()
    genres = conn.execute('SELECT * FROM genres').fetchall()
    conn.close()
    return genres

# Function to get a question based on the genre
def get_question(genre_id):
    conn = get_db_connection()
    question = conn.execute('SELECT * FROM questions WHERE genre_id = ? ORDER BY RANDOM() LIMIT 1', (genre_id,)).fetchone()
    conn.close()
    return question

# Function to handle the popup window and ask questions
def show_popup():
    # Create the main window (fullscreen)
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="white")

    # Add a label asking for the genre
    label = tk.Label(root, text="Choose a genre to answer a question:", font=("Arial", 24), bg="white")
    label.pack(pady=20)

    # Get genres from the database and create buttons for each genre
    genres = get_genres()
    buttons_frame = tk.Frame(root, bg="white")
    buttons_frame.pack(pady=20)

    def on_genre_select(genre_id):
        # Get a random question for the selected genre
        question = get_question(genre_id)
        if question:
            ask_question(root, question, genre_id)
        else:
            messagebox.showerror("Error", "No questions found for this genre.")
            root.quit()

    for genre in genres:
        genre_button = tk.Button(buttons_frame, text=genre['name'], font=("Arial", 18), command=lambda g=genre: on_genre_select(g['id']))
        genre_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

# Function to ask the question and validate the answer
def ask_question(root, question, genre_id):
    root.quit()  # Close the genre selection window
    
    # Create new window for the question
    question_window = tk.Tk()
    question_window.attributes("-fullscreen", True)
    question_window.configure(bg="white")

    # Display the question
    question_label = tk.Label(question_window, text=question['question_text'], font=("Arial", 24), bg="white")
    question_label.pack(pady=20)

    # Create a text entry for the user to input the answer
    answer_entry = tk.Entry(question_window, font=("Arial", 18))
    answer_entry.pack(pady=10)

    # Button to submit the answer
    def submit_answer():
        user_answer = answer_entry.get()
        if user_answer.lower() == question['correct_answer'].lower():
            messagebox.showinfo("Correct", "Correct! You can continue.")
            question_window.quit()
        else:
            messagebox.showerror("Incorrect", "Incorrect answer. Try again.")
    
    submit_button = tk.Button(question_window, text="Submit Answer", font=("Arial", 18), command=submit_answer)
    submit_button.pack(pady=20)

    question_window.mainloop()

# Function to run the popup every 10 minutes
def run_popup_every_10_minutes():
    while True:
        time.sleep(600)  # Sleep for 10 minutes (600 seconds)
        show_popup()  # Show the popup when time is up

# Start the popup every 10 minutes in a separate thread
popup_thread = threading.Thread(target=run_popup_every_10_minutes, daemon=True)
popup_thread.start()

# Keep the main program running
input("Press Enter to quit the program.")  # Prevent program from exiting immediately
