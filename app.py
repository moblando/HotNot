#!/usr/bin/env python3

import tkinter as tk
import sqlite3
import time
import pyautogui
import threading

keep_running = True

def on_f3(event):
    global keep_running
    print("F3 pressed — exiting loop.")
    keep_running = False

def get_db_connection():
    conn = sqlite3.connect("quizDB")
    conn.row_factory = sqlite3.Row
    return conn

def get_genre_by_name(genre_name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM subjects WHERE lower(name) = lower(?)", (genre_name,))
    genre = cur.fetchone()
    conn.close()
    return genre

def get_random_question(subject_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions WHERE subject_id = ? ORDER BY RANDOM() LIMIT 1", (subject_id,))
    question = cur.fetchone()
    conn.close()
    return question

def show_question_screen(genre):
    window = tk.Tk()
    window.attributes('-fullscreen', True)  # Fullscreen mode
    window.configure(bg='black')  # Black background for the quiz screen
    window.bind('<F3>', on_f3)  # Bind the F3 key to exit the loop
    window.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable the close button

    # Ensure the window stays on top of other windows (e.g., video)
    window.attributes("-topmost", True)

    # Create the quiz frame centered on the screen
    frame = tk.Frame(window, bg='white', width=400, height=300)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Get the random question for the genre
    question = get_random_question(genre["subject_id"])
    if question:
        question_label = tk.Label(frame, text=f"Question: {question['question_text']}", font=("Arial", 16), wraplength=300)
        question_label.pack(pady=20)

        answer_input = tk.Entry(frame, font=("Arial", 14))
        answer_input.pack(pady=10)

        result_label = tk.Label(frame, text="", font=("Arial", 14))
        result_label.pack(pady=10)

        def check_answer():
            user_answer = answer_input.get().strip()
            if user_answer.lower() == question["answer"].lower():
                result_label.config(text="Correct! You can continue.", fg="green")
            else:
                result_label.config(text=f"Incorrect. The correct answer was: {question['answer']}", fg="red")
            show_exit_button(window)

        tk.Button(frame, text="Submit", font=("Arial", 14), command=check_answer).pack(pady=20)

    window.mainloop()
    
def show_exit_button(window):
    tk.Button(window, text="Exit", font=("Arial", 14), command=window.destroy).pack(pady=20)

def start_quiz_loop(genre_name, interval_seconds, total_duration_seconds):
    global keep_running
    keep_running = True

    genre = get_genre_by_name(genre_name)
    if not genre:
        print(f"Genre '{genre_name}' not found.")
        return

    print(f"Starting quiz loop with interval {interval_seconds}s, and total duration {total_duration_seconds}s.")

    def loop():
        start_time = time.time()
        while keep_running:
            current_time = time.time()
            elapsed = current_time - start_time

            if elapsed >= total_duration_seconds:
                print("Total time reached. Ending quiz.")
                break

            time.sleep(interval_seconds)

            if not keep_running:
                break

            pyautogui.press('space')
            show_question_screen(genre)

    threading.Thread(target=loop).start()

if __name__ == "__main__":
    # Example usage
    start_quiz_loop("Math", 0, 0)
