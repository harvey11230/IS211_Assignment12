import sqlite3
from flask import Flask, render_template, request, redirect, url_for

def main():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""SELECT students.student_id, firstname, lastname, subject, score FROM results 
            INNER JOIN students USING (student_id)
            INNER JOIN quizzes USING (quiz_id)""")
    result_list = c.fetchall()
    return result_list

result_list = main()

app = Flask(__name__)

@app.route('/')
def dashboard():

    return render_template('dashboard.html', result=result_list)

@app.route('/refresh', methods= ['GET'])
def refresh():
    refresh = main()
    return render_template('dashboard.html', result=refresh)

@app.route('/submit', methods=["POST"])
def submit():

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    Student_ID = request.form['Student_ID']
    First_Name = request.form['First_Name']
    Last_Name = request.form['Last_Name']
    Quiz_ID = request.form['Subject']
    Score = request.form['Score']

    sql = "INSERT INTO students (student_id, firstname, lastname) VALUES (?, ?, ?)"
    val = (Student_ID, First_Name, Last_Name)
    c.execute(sql, val)

    sql = "INSERT INTO results (student_id, quiz_id, score) VALUES (?, ?, ?)"
    val = (Student_ID, Quiz_ID, Score)
    c.execute(sql, val)

    conn.commit()

    return redirect(url_for('refresh'))


if __name__ == '__main__':
    app.run(debug=True)
    main()