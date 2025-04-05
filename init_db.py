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

    # Insert subjects into the subjects table (adding Sports as a new category)
    subjects = ['Math', 'Science', 'History', 'Geography', 'Sports']
    for subject in subjects:
        cursor.execute("INSERT INTO subjects (name) VALUES (?)", (subject,))

    # Insert sample questions for each subject

    # Math questions (subject_id = 1)
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (1, 'What is 2+2?', '4')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (1, 'What is the square root of 16?', '4')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (1, 'Solve for x: 2x = 10', '5')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (1, 'What is the derivative of 3x?', '3')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (1, 'what is 8/2?', '4')")


    # Science questions (subject_id = 2)
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What planet is known as the Red Planet?', 'Mars')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What is the chemical symbol for water?', 'H2O')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What gas do plants absorb from the atmosphere?', 'Carbon Dioxide')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'Is pluto a planet?', 'No')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What is the first element on the periodic table?', 'Hydrogen')")
    
    # History questions (subject_id = 3)
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'Who was the first President of the United States?', 'George Washington')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'In which year did World War II end?', '1945')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'Who was the primary author of the Declaration of Independence?', 'Thomas Jefferson')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'What year was the United States founded?', '1776')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'Fill in the blank: The 19th Amendment guarantees ____ the right to vote.', 'Women')")

    # Geography questions (subject_id = 4)
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'What is the capital of France?', 'Paris')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'Which is the largest continent by land area?', 'Asia')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'Which ocean lies on the west coast of the United States?', 'Pacific Ocean')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'What state was Walmart founded?', 'Arkansas')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'What is the capital of Arkasnas?', 'Little Rock')")

    # Sports questions (subject_id = 5)
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'Who is the second best basketball player of all time', 'Michael Jordan')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'In which sport is the term \"love\" used?', 'Tennis')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'What sport is known as the \"king of sports\" in many countries?', 'Soccer')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'Who is the greatest basketball player of all time?', 'Lebron James')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'Who is the all time scoring leader in the NBA?', 'Lebron James')")
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Database 'quizDB' initialized successfully with Sports category.")

if __name__ == '__main__':
    main()
