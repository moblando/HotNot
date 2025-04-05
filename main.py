import sys
import init_db
import quizFlix

def initialize_db():
    # run the init_db.py file to initialize the database
    init_db.main()
    print("Database initialized.")

def run_quiz_flix():
    quizFlix.show_settings_screen()
    print("Program started.")
    

if __name__ == '__main__':
    # Initialize the database
    initialize_db()

    # Run quizFlix
    run_quiz_flix()
