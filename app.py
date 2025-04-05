import tkinter as tk
from tkinter import messagebox
import sqlite3
import threading
import time

#testing


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
                window.after(1000, window.destroy)  # Wait for 1 second before closing the window
            else:
                result_label.config(text=f"Incorrect. The correct answer was: {question['correct_answer']}", fg="red")

        submit_button = tk.Button(frame, text="Submit", font=("Arial", 14), command=check_answer)
        submit_button.pack(pady=20)

    window.mainloop()

# Start the process by showing the genre input screen
show_genre_input_screen()


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
            else:
                result_label.config(text=f"Incorrect. The correct answer was: {question['correct_answer']}", fg="red")

        submit_button = tk.Button(frame, text="Submit", font=("Arial", 14), command=check_answer)
        submit_button.pack(pady=20)

    window.mainloop()

# Start the process by showing the genre input screen
show_genre_input_screen()



#

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('quizDB')
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
