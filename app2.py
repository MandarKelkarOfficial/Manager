from flask import Flask, render_template, request

# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)


# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     email = db.Column(db.String(50))


# db.create_all()


# @app.route("/")
# def index():
#     return render_template("god.html")


# @app.route("/add_student", methods=["POST"])
# def add_student():
#     name = request.form["name"]
#     email = request.form["email"]
#     student = Student(name=name, email=email)
#     db.session.add(student)
#     db.session.commit()
#     return "Student added to the database"


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
with app.app_context():
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
    db = SQLAlchemy(app)

    class Student(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50))
        email = db.Column(db.String(50))

    db.create_all()  # create tables in database

    @app.route("/")
    def god():
        return render_template("god.html")

    @app.route("/add-student")
    def add_student():
        student = Student(name="Divya Acharekar", email="acharekardna7@gmail.com")
        db.session.add(student)
        db.session.commit()
        return "Student added successfully!"

    # add_student()

if __name__ == "__main__":
    app.run(debug=True)
