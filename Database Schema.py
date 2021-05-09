import sqlite3

def main():
    with sqlite3.connect("database.db") as d:

        c = d.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS students(
        student_id INTEGER PRIMARY KEY,
        firstname TEXT,
        lastname TEXT)
        """)

        c.execute("""
        INSERT INTO students (student_id, firstname, lastname)
        VALUES (1, 'Wei', 'Huang');
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS quizzes(
        quiz_id INTEGER PRIMARY KEY,
        subject TEXT);
        """)

        c.execute("""
        INSERT INTO quizzes (quiz_id, subject)
        VALUES (1, 'Python');
        """)

        c.execute("""
        CREATE TABLE IF NOT EXISTS results(
        result_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        quiz_id INTEGER,
        score INTEGER)
        """)

        c.execute("""
        INSERT INTO results (result_id, student_id, quiz_id, score)
        VALUES (1, 1, 1, 100);
        """)

        d.commit()

if __name__ == '__main__':
    main()