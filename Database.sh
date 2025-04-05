#!/bin/bash
<<COMMENT
This script creates a SQL database for a quiz application.
It sets up two tables:
- subjects: Contains the subjects (Math, Science, History, Geography)
- questions: Contains questions and answers linked to the subjects.
If the tables already exist, they will be dropped and recreated.
COMMENT

mysql -u root -p <<EOFMYSQL
-- Create the database if it does not exist and switch to it
CREATE DATABASE IF NOT EXISTS quizDB;
USE quizDB;

-- Drop the tables if they exist (drop 'questions' first because of the foreign key dependency)
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS subjects;

-- Create the subjects table
CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- Create the questions table with a foreign key reference to subjects
CREATE TABLE questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_id INT NOT NULL,
    question_text TEXT NOT NULL,
    answer TEXT,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- Insert subjects into the subjects table
INSERT INTO subjects (name) VALUES ('Math'), ('Science'), ('History'), ('Geography');

-- Insert sample questions for each subject

-- Math questions
INSERT INTO questions (subject_id, question_text, answer) VALUES 
  ((SELECT subject_id FROM subjects WHERE name = 'Math'), 'What is 2+2?', '4'),
  ((SELECT subject_id FROM subjects WHERE name = 'Math'), 'What is the square root of 16?', '4'),
  ((SELECT subject_id FROM subjects WHERE name = 'Math'), 'Solve for x: 2x = 10', '5');

-- Science questions
INSERT INTO questions (subject_id, question_text, answer) VALUES 
  ((SELECT subject_id FROM subjects WHERE name = 'Science'), 'What planet is known as the Red Planet?', 'Mars'),
  ((SELECT subject_id FROM subjects WHERE name = 'Science'), 'What is the chemical symbol for water?', 'H2O'),
  ((SELECT subject_id FROM subjects WHERE name = 'Science'), 'What gas do plants absorb from the atmosphere?', 'Carbon Dioxide');

-- History questions
INSERT INTO questions (subject_id, question_text, answer) VALUES 
  ((SELECT subject_id FROM subjects WHERE name = 'History'), 'Who was the first President of the United States?', 'George Washington'),
  ((SELECT subject_id FROM subjects WHERE name = 'History'), 'In which year did World War II end?', '1945'),
  ((SELECT subject_id FROM subjects WHERE name = 'History'), 'Who was the primary author of the Declaration of Independence?', 'Thomas Jefferson');

-- Geography questions
INSERT INTO questions (subject_id, question_text, answer) VALUES 
  ((SELECT subject_id FROM subjects WHERE name = 'Geography'), 'What is the capital of France?', 'Paris'),
  ((SELECT subject_id FROM subjects WHERE name = 'Geography'), 'Which is the largest continent by land area?', 'Asia'),
  ((SELECT subject_id FROM subjects WHERE name = 'Geography'), 'Which ocean lies on the west coast of the United States?', 'Pacific Ocean');
EOFMYSQL
