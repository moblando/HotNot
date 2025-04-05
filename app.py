#!/usr/bin/env python3

import tkinter as tk
import sqlite3
import time
import random
import pyautogui

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

def show_genre_input_screen():
    window = tk.Tk()
    window.attributes('-fullscreen', True)
    window.configure(bg='black')
    window.protocol("WM_DELETE_WINDOW", lambda: None)
    frame = tk.Frame(window, bg='white', width=400, height=300)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    tk.Label(frame, text="Enter Genre (Geography, Math, Science, History):", font=("Arial", 14)).pack(pady=10)
    genre_input = tk.Entry(frame, font=("Arial", 14))
    genre_input.pack(pady=10)
    result_label = tk.Label(frame, text="", font=("Arial", 14), fg='black')
    result_label.pack(pady=10)

    def submit_genre():
        genre_name = genre_input.get().strip()
        genre = get_genre_by_name(genre_name)
        if genre:
            window.destroy()
            show_question_screen(genre)
        else:
            result_label.config(text="Invalid genre. Please try again.", fg="red")

    tk.Button(frame, text="Submit", font=("Arial", 14), command=submit_genre).pack(pady=20)
    window.mainloop()

def show_question_screen(genre):
    window = tk.Tk()
    window.attributes('-fullscreen', True)
    window.configure(bg='black')
    window.protocol("WM_DELETE_WINDOW", lambda: None)
    frame = tk.Frame(window, bg='white', width=400, height=300)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    question_label = tk.Label(frame, text="Please wait while we get your question...", font=("Arial", 16), wraplength=300)
    question_label.pack(pady=20)
    question = get_random_question(genre["subject_id"])
    if question:
        question_label.config(text=f"Question: {question['question_text']}")
        answer_input = tk.Entry(frame, font=("Arial", 14))
        answer_input.pack(pady=10)
        result_label = tk.Label(frame, text="", font=("Arial", 14), fg='black')
        result_label.pack(pady=10)

        def check_answer():
            user_answer = answer_input.get().strip()
            if user_answer.lower() == question["answer"].lower():
                result_label.config(text="Correct! You can continue.", fg="green")
                show_exit_button(window)
            else:
                result_label.config(text=f"Incorrect. The correct answer was: {question['answer']}", fg="red")

        tk.Button(frame, text="Submit", font=("Arial", 14), command=check_answer).pack(pady=20)
    window.mainloop()

def show_exit_button(window):
    tk.Button(window, text="Exit", font=("Arial", 14), command=window.destroy).pack(pady=20)

def delayed_popup():
    time.sleep(10)
    pyautogui.press('space')
    show_genre_input_screen()

delayed_popup()
