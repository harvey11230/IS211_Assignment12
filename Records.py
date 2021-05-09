import sqlite3
from flask import Flask, render_template

conn = sqlite3.connect("database.db")

c = conn.cursor()

c.execute("""SELECT students.student_id, firstname, lastname, subject, score FROM results 
            INNER JOIN students USING (student_id)
            INNER JOIN quizzes USING (quiz_id)""")

result = c.fetchall()


app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template('dashboard.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)