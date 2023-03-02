import json
from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy
import smtplib
import pandas as pd
from waitress import serve
import csv
import urllib.request
import io
import re
import os
import time
import sqlite3
import cv2
import webbrowser
import pandas as pd
import mysql.connector
from dateutil import parser
from datetime import date
from datetime import datetime
from num2words import num2words
from normword_dna import dna as me
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen.canvas import Canvas

app = Flask(__name__)
CORS(app)
db = SQLAlchemy()
# db.init_app(app)
mydb = mysql.connector.connect(
    host="localhost",
    port="6681",
    user="BeastBoi",
    password="@beastboi7DemonGOD@dna7",
    database="newer",
)


# app.config["SQLALCHEMY_BINDS"] = True


# app.config["SQLALCHEMY_DATABASE_URI"] = mydb
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://student_08mv_user:LW1vDrthH1iSsOCPjDfVQK0pOulPDKrG@dpg-cfo5ro94rebfdav246og-a.oregon-postgres.render.com/student_08mv"
# app.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = "mysql://username:password@hostname:port/database_name?charset=utf8mb4&collation=utf8mb4_unicode_ci"


# conn = sqlite3.connect("D:\Manger\instance\manager.db")
# cursor = conn.cursor()
# cursor.execute("DELETE FROM co_std_name_sfm WHERE std_enrollment_no = ?", (2001170266,))
# conn.commit()

db.init_app(app)


class std_manager(db.Model):
    std_enrollment_no = db.Column(db.Integer, primary_key=True)
    std_email = db.Column(db.String(100), nullable=False)
    registration_no = db.Column(db.String(100), nullable=False)
    std_Sub_caste = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.Integer, nullable=False)
    std_place_of_birth = db.Column(db.String(100), nullable=False)
    std_dob_db_co = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(21), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    std_nationality = db.Column(db.String(40), nullable=False)
    std_institution_last_attained = db.Column(db.String(250), nullable=False)
    std_Date_of_Admission = db.Column(db.String(250), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    sub_dist = db.Column(db.String(50), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    allotment = db.Column(db.String(50), nullable=False)
    man_entry = db.Column(db.String(50), nullable=False)
    marry = db.Column(db.String(50), nullable=False)
    age = db.Column(db.String(10), nullable=False)
    postal_code = db.Column(db.Integer, nullable=False)


class co_std_name_sfm(db.Model):
    std_enrollment_no = db.Column(db.Integer, primary_key=True)
    std_surname = db.Column(db.String(100), nullable=False)
    std_firstname = db.Column(db.String(100), nullable=False)
    std_middlename = db.Column(db.String(100), nullable=False)


# class co_students(db.Model):
#     std_enrollment_no = db.Column(db.Integer, foreign=True)
#     std_surname = db.Column(db.String(100), nullable=False)
#     std_firstname = db.Column(db.String(100), nullable=False)
#     std_middlename = db.Column(db.String(100), nullable=False)


class std_collage_manager(db.Model):
    std_enrollment_no = db.Column(db.Integer, primary_key=True)
    collage_name_2 = db.Column(db.String(100), nullable=False)


class user_login(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


mycursor = mydb.cursor()


clear = lambda: os.system("cls")  # to clear previous output from the terminal


def generate_certificate(
    std_enrollment_no, conduct, progress, col_since, reason, remark
):
    # Student registration number
    registration_no = mydb.cursor()
    registration_no.execute(
        "SELECT registration_no FROM co_students WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )
    for std_regis in registration_no:
        std_registration_no = ""
        std_registration_no = std_registration_no.join(std_regis)

    # Student L.C No.
    lc_no_count = []
    lc_no_count.append(len(os.listdir("D:\@BB\Working\Leaving_Certificates")))
    for std_lc_no in lc_no_count:
        std_lc_no_c = int(std_lc_no) + 1
        str(std_lc_no_c)
        std_lc_no = str(std_lc_no_c)
        lc_no = mydb.cursor()
        lc_no.execute(
            "UPDATE co_students SET std_lc_no = '"
            + std_lc_no
            + "' WHERE std_enrollment_no = "
            + std_enrollment_no
            + ""
        )
        mydb.commit()

    # Student name (last_name first_name middle_name)
    make_name = mydb.cursor()
    make_name.execute(
        "SELECT std_surname, std_firstname, std_middlename FROM co_std_name_sfm WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )

    for make_name in make_name:
        this_name = {
            "Surname": make_name[0],
            "FirstName": make_name[1],
            "MiddleName": make_name[2],
        }
        std_surname = this_name["Surname"]
        std_firstname = this_name["FirstName"]
        std_middlename = this_name["MiddleName"]

    # Student Race-Caste (Sub-caste)
    sub_caste = mydb.cursor()
    sub_caste.execute(
        "SELECT std_Sub_caste FROM co_students WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )
    for sub_cast in sub_caste:
        stu_sub_caste = ""
        stu_sub_caste = stu_sub_caste.join(sub_cast)

    # Student Place of Birth
    birth_place = mydb.cursor()
    birth_place.execute(
        "SELECT std_place_of_birth FROM co_students WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )
    for place_of_birth in birth_place:
        std_place_of_birth = ""
        std_place_of_birth = std_place_of_birth.join(place_of_birth)
    # updating birth date od student
    # dna_dob = input("Enter birth date")
    # dna_enroll = input("Enter enrollment")
    # d = parser.parse(dna_dob)
    # dob=(d.strftime("%Y-%m-%d"))
    # leaving_date = mydb.cursor()
    # leaving_date.execute("UPDATE co_students SET std_dob_db_co = '"+dob+"' WHERE std_enrollment_no = "+dna_enroll+"")
    # mydb.commit()

    # Student Birth-Date Date of birth according to the Christian era in words "+std_enrollment_no+"
    birth_of = mydb.cursor()
    birth_of.execute(
        "SELECT DATE_FORMAT(std_dob_db_co, '%Y-%m-%d')  FROM co_students WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )
    try:
        for of_birth in birth_of:
            str_for = ""
            std_born_date = str_for.join(of_birth)
            d = parser.parse(std_born_date)
            year = int(d.strftime("%Y"))  # year in number (ex. 2004)
            year_n = str(year)
            month = d.strftime("%B")  # month in word (ex. October)
            month_int = d.strftime("%m")  # month in number (ex. 10)
            day = d.strftime("%A")  # date in word (ex. Monday )
            day_int = d.strftime("%d")  # date in number (ex. 25 )

            # word_day = num2words(int(d.strftime("%d"))) # date in word (ex. 25 = Twenty Five )
            # ignore_ = re.compile(r"(-)")
            # day_in_word = re.sub(ignore_, ' ',word_day)
            day_in_word = me.from_user(day_int)

            # here converting int year to words and then ignoring 'and' word from it
            year = num2words(year)
            year_re = year.split(" ")
            ignore = ["and"]
            year_in_word = " ".join([t for t in year_re if not t in ignore])
    except Exception:
        print("No date found")

    # Student Nationality
    nationality = mydb.cursor()
    nationality.execute(
        "SELECT std_nationality FROM co_students WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )
    for nationality_of_std in nationality:
        std_nationality = ""
        std_nationality = std_nationality.join(nationality_of_std)

    # Student Institution last attained
    last_institution = mydb.cursor()
    last_institution.execute(
        "SELECT std_institution_last_attained FROM co_students WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )
    for last_institution_of_std in last_institution:
        std_last = ""
        std_last = std_last.join(last_institution_of_std)
    i = 40
    std_line_next = ""
    std_line_on = ""
    j = 0
    n = 53
    for i in range(i - 1):
        while j <= 52:
            std_line_on += std_last[j]
            j = j + 1
        try:
            std_line_next += std_last[n]
            n = n + 1
        except:
            pass

    # Student Date of Admission
    admission_date = mydb.cursor()
    admission_date.execute(
        "SELECT std_Date_of_Admission FROM co_students WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )
    for admission_date_of_std in admission_date:
        std_Date_of_Admission = ""
        std_Date_of_Admission = std_Date_of_Admission.join(admission_date_of_std)

    # Student Enrollment No
    enrollment_no = mydb.cursor()
    enrollment_no.execute(
        "SELECT std_enrollment_no FROM co_students WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )
    enrollment_no_of_std = [
        tuple(map(str, enrollment_no_of_std)) for enrollment_no_of_std in enrollment_no
    ]
    for std_enrollment_no in enrollment_no_of_std:
        std_enrollment_no = "".join(std_enrollment_no)

    # Student Date of Leaving institute
    today = date.today()
    std_leaving_date = today.strftime("%B %d, %Y")

    leaving_date = mydb.cursor()
    leaving_date.execute(
        "UPDATE co_students SET std_leaving_date = '"
        + std_leaving_date
        + "' WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )
    mydb.commit()

    # # Student Flag
    flag_no = "1"

    flag_check_mate = mydb.cursor()
    flag_check_mate.execute(
        "UPDATE co_students SET std_flag = "
        + flag_no
        + " WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )
    mydb.commit()

    page_to_merge = 0  # Refers to the First page of PDF
    input_pdf = PdfFileReader(
        open(
            "D:\\Manger\\static\\pdf\\pagetemp.pdf",
            "rb",
        )
    )
    page_count = input_pdf.getNumPages()
    inputpdf_page_to_be_merged = input_pdf.getPage(page_to_merge)

    packet = io.BytesIO()
    c = Canvas(
        packet,
        pagesize=(
            inputpdf_page_to_be_merged.mediaBox.getWidth(),
            inputpdf_page_to_be_merged.mediaBox.getHeight(),
        ),
    )

    # Here i am writing the certificate pdf
    c.drawString(173, 683, "Registration no.")  # registration no.
    c.drawString(450, 683, std_lc_no)  # l.c. no.

    c.drawString(270, 640, std_surname)  # Surname
    c.drawString(360, 640, std_firstname)  # Firstname
    c.drawString(470, 640, std_middlename)  # Middlename

    c.drawString(264, 597, stu_sub_caste)  # sub_caste of student
    c.drawString(264, 575, std_place_of_birth)  # Student Place of Birth

    c.drawString(296, 555, day_int)  # Date of birth in number
    c.drawString(400, 555, month_int)  # month of birth in number
    c.drawString(505, 555, year_n)  # year of birth in number
    c.drawString(264, 510, day_in_word)  # Date of birth
    c.drawString(385, 510, month)  # month of birth
    c.drawString(460, 510, year_in_word)  # year of birth

    c.drawString(264, 487, std_nationality)  # Student Nationality
    c.drawString(264, 467, std_line_on)  # Student Institution last attained
    c.drawString(264, 445, std_line_next)  # Student Institution last attained
    c.drawString(264, 423, std_Date_of_Admission)  # Date of admission
    c.drawString(264, 402, std_enrollment_no)  # student enrollment no
    c.drawString(264, 380, progress)  # progress of student
    c.drawString(264, 358, conduct)  # conduct of student
    c.drawString(264, 336, std_leaving_date)  # institute leaving date
    c.drawString(
        264, 313, col_since
    )  # course and year in which studying and since when
    c.drawString(
        264, 293, std_Date_of_Admission + ""
    )  # course and year in which studying and since when
    c.drawString(264, 270, reason)  # reason
    c.drawString(264, 250, "--")  # reason
    c.drawString(264, 227, remark)  # Remark
    c.drawString(93, 140, std_leaving_date)  # institute leaving date at

    c.save()
    packet.seek(0)

    overlay_pdf = PdfFileReader(packet)
    overlay = overlay_pdf.getPage(0)

    output = PdfFileWriter()

    for PAGE in range(page_count):
        if PAGE == page_to_merge:
            inputpdf_page_to_be_merged.mergeRotatedTranslatedPage(
                overlay,
                inputpdf_page_to_be_merged.get("/Rotate") or 0,
                overlay.mediaBox.getWidth() / 2,
                overlay.mediaBox.getWidth() / 2,
            )
            output.addPage(inputpdf_page_to_be_merged)

        else:
            Page_in_pdf = input_pdf.getPage(PAGE)
            output.addPage(Page_in_pdf)

    outputStream = open(
        "D:\\@BB\\Working\\Leaving_Certificates\\lc_of_" + std_enrollment_no + ".pdf",
        "wb",
    )
    output.write(outputStream)
    outputStream.close()


def check_for_flag(std_enrollment_no, conduct, progress, col_since, reason, remark):
    checker_cursor = mydb.cursor()
    checker_cursor.execute(
        "SELECT std_enrollment_no FROM co_students WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )
    if len(checker_cursor.fetchall()) > 0:
        flag_checker_cursor = mydb.cursor()
        flag_checker_cursor.execute(
            "SELECT std_flag FROM co_students WHERE std_enrollment_no = "
            + std_enrollment_no
            + ""
        )
        flag_checker_of_std = [
            tuple(map(str, enrollment_no_of_std))
            for enrollment_no_of_std in flag_checker_cursor
        ]
        for std_flag_no in flag_checker_of_std:
            std_final_flag = "".join(std_flag_no)
            if std_final_flag == "0":
                check_for_validation(
                    std_enrollment_no, conduct, progress, col_since, reason, remark
                )
            else:
                already()
    else:
        print("Entered Enroll no. is Invalid")
        no_no()


def check_for_validation(
    std_enrollment_no, conduct, progress, col_since, reason, remark
):
    checker_cursor = mydb.cursor()
    checker_cursor.execute(
        "SELECT std_enrollment_no FROM co_students WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )
    if len(checker_cursor.fetchall()) > 0:
        generate_certificate(
            std_enrollment_no, conduct, progress, col_since, reason, remark
        )  # From here pointer is going to the *generate_certificate()* function which is responsible for retrieving and writing a new leaving paper and coming back.

        print("\rL.C Generated Successfully")

        time.sleep(1)
        url = (
            "file:///D:/@BB/Working/Leaving_Certificates/lc_of_"
            + std_enrollment_no
            + ".pdf"
        )  # specifying file path

        try:
            chrome_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"  # specifying webbrowser
            bb_x_dna_wb = webbrowser.get(chrome_path)
            # bb_x_dna_wb.open(url)
            dna = bb_x_dna_wb.open(url)
            if dna == False:
                # print('Error opening browser')
                chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # specifying another webbrowser
                bb_x_dna_wb = webbrowser.get(chrome_path)
                bb = bb_x_dna_wb.open(url)
                if bb == True:
                    pass
                else:
                    print(
                        "Error in opening your browser. But don't worry your paper has already saved to your local disk. if you want you may go and open it manually."
                    )

        except Exception:
            pass

        done()

    else:
        print("\rEntered Enroll no. is Invalid")

        cant()


# For recreating a lc
def reset_flag_to_0_for_new(std_enrollment_no):
    my_db_flag_reset_q = mydb.cursor()
    my_db_flag_reset_q.execute(
        "UPDATE co_students SET std_flag = 0 WHERE std_enrollment_no = "
        + std_enrollment_no
        + ""
    )
    mydb.commit()
    print("\rYou can generate new LC for : " + std_enrollment_no + "", end="")
    time.sleep(1)
    clear()
    do()
    return bb


def done():
    our_son("done")


def js_alert():
    our_son("js_alert")


def already():
    our_son("already")


def do():
    our_son("do_enter_again")


def cant():
    our_son("invalid_check_for_val")


def no_no():
    our_son("invalid_flag")


def our_son(dna):
    global bb
    bb = dna
    print(bb)
    return bb


# @eel.expose
# def main():
# std_enrollment_no = input("Enter student Enroll no. : ")
# check_for_flag(std_enrollment_no)
# me = my_finally
# return  me

# main()
# @eel.expose
# def main(my_finally):
# std_enrollment_no = input("Enter student Enroll no. : ")
# check_for_flag(std_enrollment_no)
# me = my_finally
# return  me

# main()


def get_random_enroll(std_enrollment_no, conduct, progress, col_since, reason, remark):
    # eel.prompt_alerts("Demon's God DNA X BB")
    check_for_flag(std_enrollment_no, conduct, progress, col_since, reason, remark)
    return bb


# @app.route("/form", methods=["GET", "POST"])
# def form():
#     if request.method == "POST":
#         name = request.form["name"]
#         email = request.form["email"]
#         phone_no = request.form["phone_no"]
#         birth_date = request.form["birth_date"]
#         enrollment_no = request.form["enrollment_no"]
#         gender = request.form["gender"]
#         address = request.form["address"]
#         country = request.form["country"]
#         city = request.form["city"]

#         postal_code = request.form["postal_code"]

#         data = std_manager(
#             name=name,
#             email=email,
#             phone_no=phone_no,
#             birth_date=birth_date,
#             enrollment_no=enrollment_no,
#             gender=gender,
#             address=address,
#             country=country,
#             city=city,
#
#             postal_code=postal_code,
#         )
#         db.session.add(data)
#         db.session.commit()

#     return render_template("forms.html")


@app.route("/process-entry-form", methods=["POST"])
def process_entry_form():
    enrollment = request.form["enroll-number-2"]
    sname = request.form["sname-2"]
    fname = request.form["fname-2"]
    mname = request.form["mname-2"]

    st_admission = (
        request.form["s-admission-month"]
        + " "
        + str(request.form["s-admission-day"])
        + ", "
        + str(request.form["s-admission-year"])
    )

    email = request.form["email-2"]
    mo_no = request.form["mobile-num-2"]
    country = request.form["country"]
    postcode = request.form["postcode"]
    address = request.form["address"]
    state = request.form["state"]
    sub_dist = request.form["sub-district"]
    district = request.form["district"]
    message = request.form["message"]
    allotment = request.form["s-allotment"]
    man_entry = request.form["entered-by-m-2"]
    marry = request.form["marry"]
    age = request.form["age"]
    gender = request.form["gender"]
    message = request.form["message"]

    register_num = request.form["register-number-2"]
    school_Last_2 = request.form["school-Last-2"]
    collage_name_2 = "Government Polytechnic, Malvan"
    sub_cast = request.form["sub-cast"]
    birth_place = request.form["birth-place"]
    birth_date = request.form["birth-date"]

    # Call your Python function here, passing in the form data
    # result = get_random_enroll(enrollment, conduct, prog, col_since, reason, remark)

    # Call your Python function here, passing in the form data

    # result = print(
    #     enrollment.replace(" ", ""),
    #     register_num,
    #     email,
    #     sname,
    #     fname,
    #     mname,
    #     mo_no,
    #     country,
    #     postcode,
    #     address,
    #     state,
    #     sub_dist,
    #     district,
    #     allotment,
    #     man_entry,
    #     marry,
    #     gender,
    #     age,
    #     school_Last_2,
    #     birth_date,
    #     sub_cast,
    #     birth_place,
    #     collage_name_2,
    #     st_admission,
    # )

    data = std_manager(
        std_enrollment_no=int(enrollment.replace(" ", "")),
        std_email=email,
        registration_no=register_num,
        std_Sub_caste=sub_cast,
        phone_no=mo_no.replace(" ", ""),
        std_place_of_birth=birth_place,
        std_dob_db_co=birth_date,
        gender=gender,
        address=address,
        std_nationality=country,
        std_institution_last_attained=school_Last_2,
        std_Date_of_Admission=st_admission,
        state=state,
        sub_dist=sub_dist,
        district=district,
        allotment=allotment,
        man_entry=man_entry,
        marry=marry,
        age=age,
        postal_code=postcode.replace(" ", ""),
    )

    data_name = co_std_name_sfm(
        std_enrollment_no=int(enrollment.replace(" ", "")),
        std_surname=sname,
        std_firstname=fname,
        std_middlename=mname,
    )
    db.session.add(data)
    db.session.add(data_name)

    db.session.commit()

    # Create a response object with the result
    # response = jsonify({"result": result})

    # # # Return the response object
    # # return render_template("index.html")

    # redirect the user back to the previous page
    return "", 204


@app.route("/check-username/<username>")
def check_username(username):
    # conn = sqlite3.connect("D:\Manger\instance\manager.db")
    # cursor = conn.cursor()
    # cursor.execute(
    #     "SELECT * FROM std_manager WHERE std_enrollment_no = ?",
    #     (int(username.replace(" ", "")),),
    # )
    result = std_manager.query.filter_by(
        std_enrollment_no=username.replace(" ", "")
    ).first()
    # conn.close()

    if result is not None:
        return jsonify({"exists": True})
    else:
        return jsonify({"exists": False})


@app.route("/process-form", methods=["POST"])
def process_form():
    enrollment = request.form["enroll-number"]
    prog = request.form["prog"]
    conduct = request.form["s-conduct"]
    col_since = request.form["s-studying-since"]
    reason = request.form["s-leaving-reason"]
    remark = request.form["s-remark"]
    message = request.form["message"]
    # Call your Python function here, passing in the form data
    # result = get_random_enroll(enrollment, conduct, prog, col_since, reason, remark)

    # Call your Python function here, passing in the form data
    result = get_random_enroll(
        enrollment.replace(" ", ""), conduct, prog, col_since, reason, remark
    )

    # Create a response object with the result
    response = jsonify({"result": result})

    # Return the response object
    return "", 204


@app.route("/data")
def get_data():
    # Load data from a JSON file
    with open("static/dtstatic/data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)


# Define a route for the index page
@app.route("/index")
def index():
    return render_template("index.html")


# Define a route for the login page
@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = user_login.query.filter_by(username=username, password=password).first()
        if user is not None:
            return redirect(url_for("index"))
        else:
            error = "Invalid Credentials. Please try again."

    return render_template("login.html")


def my_function(enrollment, conduct, prog, col_since, reason, remark, message):
    print(
        type(enrollment.replace(" ", "")),
        conduct,
        prog,
        col_since,
        reason,
        remark,
        message,
    )


@app.route("/datatable")
def datatable():
    return render_template("datatable.html")


@app.before_first_request
def create_table():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
