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

-- Drop the tables if they exist (drop 'questions' first because of the foreign key)
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
INSERT INTO questions (subject_id, question_text, answer) VALUES 
  ((SELECT subject_id FROM subjects WHERE name = 'Math'), 'What is 2+2?', '4'),
  ((SELECT subject_id FROM subjects WHERE name = 'Science'), 'What planet is known as the Red Planet?', 'Mars'),
  ((SELECT subject_id FROM subjects WHERE name = 'History'), 'Who was the first President of the United States?', 'George Washington'),
  ((SELECT subject_id FROM subjects WHERE name = 'Geography'), 'What is the capital of France?', 'Paris');
EOFMYSQL
