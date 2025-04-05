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
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (1, 'What is 7 * 8?', '56')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (1, 'What is 10^2?', '100')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (1, 'What is 45 / 9?', '5')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (1, 'What is the value of pi rounded to 2 decimal places?', '3.14')")


    # Science questions (subject_id = 2)
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What planet is known as the Red Planet?', 'Mars')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What is the chemical symbol for water?', 'H2O')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What gas do plants absorb from the atmosphere?', 'Carbon Dioxide')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'Is pluto a planet?', 'No')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What is the first element on the periodic table?', 'Hydrogen')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What is the powerhouse of the cell?', 'Mitochondria')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What is the chemical formula for methane?', 'CH4')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'Which planet is closest to the Sun?', 'Mercury')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What is the symbol for the element Oxygen?', 'O')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (2, 'What organ is responsible for pumping blood?', 'Heart')")
    
    # History questions (subject_id = 3)
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'Who was the first President of the United States?', 'George Washington')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'In which year did World War II end?', '1945')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'Who was the primary author of the Declaration of Independence?', 'Thomas Jefferson')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'What year was the United States founded?', '1776')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'Fill in the blank: The 19th Amendment guarantees ____ the right to vote.', 'Women')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'Who was the first woman to fly solo across the Atlantic?', 'Amelia Earhart')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'What was the name of the ship that carried the Pilgrims to America?', 'Mayflower')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'Who was the 16th President of the United States?', 'Abraham Lincoln')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (3, 'In what year was the Declaration of Independence signed?', '1776')")

    # Geography questions (subject_id = 4)
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'What is the capital of France?', 'Paris')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'Which is the largest continent by land area?', 'Asia')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'Which ocean lies on the west coast of the United States?', 'Pacific Ocean')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'What state was Walmart founded?', 'Arkansas')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'What is the capital of Arkasnas?', 'Little Rock')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'What is the largest country by area?', 'Russia')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'What is the longest river in the world?', 'Nile River')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'Which country has the most population?', 'China')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'Which country has the most number of islands?', 'Sweden')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (4, 'What is the highest mountain in the world?', 'Mount Everest')")

    # Sports questions (subject_id = 5)
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'Who is the second best basketball player of all time', 'Michael Jordan')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'In which sport is the term \"love\" used?', 'Tennis')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'What sport is known as the \"king of sports\" in many countries?', 'Soccer')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'Who is the greatest basketball player of all time?', 'Lebron James')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'Who is the all time scoring leader in the NBA?', 'Lebron James')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'Which country won the 2018 FIFA World Cup?', 'France')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'In which year was the first Super Bowl played?', '1967')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'Who holds the record for most home runs in a single MLB season?', 'Barry Bonds')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'Who is the most decorated Olympian of all time?', 'Michael Phelps')")
    cursor.execute("INSERT INTO questions (subject_id, question_text, answer) VALUES (5, 'Which NBA player is known as the \"Black Mamba\"?', 'Kobe Bryant')")


    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Database 'quizDB' initialized successfully")

if __name__ == '__main__':
    main()