import sqlite3

def create_sutdents_table():
    with sqlite3.connect("Students.db") as s:
        c = s.cursor()

        c.execute("""
        CREATE TABLE IF NOT EXISTS students(
        student_id INTEGER PRIMARY KEY,
        firstname TEXT,
        lastname TEXT);
        """)

        c.execute("""
        INSERT INTO students (student_id, firstname, lastname)
        VALUES (1, 'Wei', 'Huang');
        """)

        s.commit()


def create_quizzes_table():
    with sqlite3.connect("Quizzes.db") as q:
        c = q.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS quizzes(
        quiz_id INTEGER PRIMARY KEY,
        subject TEXT);
        """)

        c.execute("""
        INSERT INTO quizzes (quiz_id, subject)
        VALUES (1, 'Python');
        """)
        q.commit()


def create_result_table():
    with sqlite3.connect("Results.db") as r:
        c = r.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS results(
        result_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        quiz_id INTEGER,
        score INTEGER,
        FOREIGN KEY (student_id) REFERENCES students (student_id),
        FOREIGN KEY (quiz_id) REFERENCES quizzes (quiz_id))
        """)

        c.execute("""
        INSERT INTO results (result_id, student_id, quiz_id, score)
        VALUES (1, 1, 1, 100);
        """)

        r.commit()


def main():
    create_sutdents_table()
    create_quizzes_table()
    create_result_table()

if __name__ == '__main__':
    main()