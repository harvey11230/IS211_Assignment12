import sqlite3

conn = sqlite3.connect("Results.db")

c = conn.cursor()

c.execute("SELECT * FROM results INNER JOIN students USING (student_id)"
          "INNER JOIN quizzes USING (quiz_id)")

print(c.fetchall())