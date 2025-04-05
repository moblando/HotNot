#!/usr/bin/env python3
import sqlite3

def main():
    # Connect to (or create) the SQLite database file named "quizDB"
    conn = sqlite3.connect("quizDB")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Enable foreign key constraints in SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Drop existing tables (drop 'questions' first due to foreign key dependency)
    cursor.execute("DROP TABLE IF EXISTS questions;")
    cursor.execute("DROP TABLE IF EXISTS subjects;")

    # Create the subjects table
    cursor.execute("""
    CREATE TABLE subjects (
        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );
    """)

    # Create the questions table with a foreign key to subjects
    cursor.execute("""
    CREATE TABLE questions (
        question_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id INTEGER NOT NULL,
        question_text TEXT NOT NULL,
        answer TEXT,
        FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
    );
    """)

    # Insert subjects into the subjects table
    subjects = ['Math', 'Science', 'History', 'Geography']
    for subject in subjects:
        cursor.execute("INSERT INTO subjects (name) VALUES (?)", (subject,))

    # Insert sample questions for each subject
    # Math questions (subject_id assumed to be 1)
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (1, 'What is 2+2?', '4')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (1, 'What is the square root of 16?', '4')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (1, 'Solve for x: 2x = 10', '5')")

    # Science questions (subject_id assumed to be 2)
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What planet is known as the Red Planet?', 'Mars')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What is the chemical symbol for water?', 'H2O')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What gas do plants absorb from the atmosphere?', 'Carbon Dioxide')")

    # History questions (subject_id assumed to be 3)
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'Who was the first President of the United States?', 'George Washington')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'In which year did World War II end?', '1945')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'Who was the primary author of the Declaration of Independence?', 'Thomas Jefferson')")

    # Geography questions (subject_id assumed to be 4)
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'What is the capital of France?', 'Paris')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'Which is the largest continent by land area?', 'Asia')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'Which ocean lies on the west coast of the United States?', 'Pacific Ocean')")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Database 'quizDB' initialized successfully.")

if __name__ == '__main__':
    main()
