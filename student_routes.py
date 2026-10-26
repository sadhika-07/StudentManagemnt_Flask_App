from flask import Blueprint, render_template
from extensions import mysql
 
student_bp = Blueprint("students", __name__)
 
 
@student_bp.route("/")
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    cur.close()
    total_students = len(students)
    return render_template(
        "index.html",
        students=students,
        total_students=total_students
    )
 
 
@student_bp.route("/db-test")
def db_test():
    cur = mysql.connection.cursor()
    cur.execute("SELECT DATABASE()")
    database_name = cur.fetchone()[0]
    cur.close()
 
    return render_template("db_test.html", database_name=database_name)