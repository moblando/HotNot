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
    window.attributes('-fullscreen', True)
    window.configure(bg='black')
    window.bind('<F3>', on_f3)
    window.protocol("WM_DELETE_WINDOW", lambda: None)

    frame = tk.Frame(window, bg='white', width=400, height=300)
    frame.place(relx=0.5, rely=0.5, anchor="center")

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

def start_quiz_loop(genre_name, int_time):
    global keep_running
    keep_running = True

    genre = get_genre_by_name(genre_name)
    if not genre:
        print(f"Genre '{genre_name}' not found.")
        return

    print(f"Starting quiz loop with genre '{genre_name}' and interval {int_time} seconds.")

    def loop():
        while keep_running:
            time.sleep(int_time)
            if not keep_running:
                break
            pyautogui.press('space')
            show_question_screen(genre)

    threading.Thread(target=loop).start()
