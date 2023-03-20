import json
from flask_cors import CORS
import os
import smtplib
import pandas as pd
from sqlalchemy import func
from waitress import serve
import csv
import time
import io
import re
from io import BytesIO
import os
import cv2
import webbrowser
import pandas as pd
from dateutil import parser
from datetime import date
from datetime import datetime
from num2words import num2words
from normword_dna import dna as me
from flask_sqlalchemy import SQLAlchemy
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen.canvas import Canvas
from sqlalchemy.exc import IntegrityError
from flask import (
    Flask,
    make_response,
    render_template,
    render_template_string,
    request,
    redirect,
    send_file,
    url_for,
    jsonify,
    Response,
)


app = Flask(__name__)
CORS(app)
db = SQLAlchemy()

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://student_08mv_user:LW1vDrthH1iSsOCPjDfVQK0pOulPDKrG@dpg-cfo5ro94rebfdav246og-a.oregon-postgres.render.com/student_08mv"

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
    std_department = db.Column(db.Integer, nullable=True)
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


class co_students(db.Model):
    std_enrollment_no = db.Column(db.Integer, primary_key=True)
    registration_no = db.Column(db.String(100), nullable=False)
    std_Sub_caste = db.Column(db.String(100), nullable=False)
    std_place_of_birth = db.Column(db.String(100), nullable=False)
    std_dob_db_co = db.Column(db.Date, nullable=False)
    std_nationality = db.Column(db.String(40), nullable=False)
    std_institution_last_attained = db.Column(db.String(250), nullable=False)
    std_Date_of_Admission = db.Column(db.String(250), nullable=False)
    std_leaving_date = db.Column(db.String(20), nullable=False)
    std_lc_no = db.Column(db.String(50), nullable=False)
    std_flag = db.Column(db.Integer, nullable=False)


class std_collage_manager(db.Model):
    std_enrollment_no = db.Column(db.Integer, primary_key=True)
    collage_name_2 = db.Column(db.String(100), nullable=False)
    std_leavingtemp = db.Column(db.LargeBinary)


class user_login(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class leavingpages(db.Model):
    std_enrollment_no = db.Column(db.Integer, primary_key=True)
    std_leaving = db.Column(db.LargeBinary)


clear = lambda: os.system("cls")  # to clear previous output from the terminal


def generate_certificate(
    std_enrollment_no, conduct, progress, col_since, reason, remark
):
    """Getting Student all data at ones and store it to student_data"""
    student_data = co_students.query.filter_by(
        std_enrollment_no=std_enrollment_no
    ).first()

    """Student registration number"""
    std_registration_no = f"{student_data.registration_no}"

    """Student L.C No."""
    total_rows = leavingpages.query.count()
    std_lc_no = total_rows + 1
    student_data.std_lc_no = str(std_lc_no)
    db.session.commit()

    """* Student name (last_name first_name middle_name) *"""
    student = co_std_name_sfm.query.filter_by(
        std_enrollment_no=std_enrollment_no
    ).first()
    std_firstname = f"{student.std_firstname}"
    std_middlename = f"{student.std_middlename}"
    std_surname = f"{student.std_surname}"

    """Student Race-Caste (Sub-caste)"""
    stu_sub_caste = f"{student_data.std_Sub_caste}"

    """Student Place of Birth"""
    std_place_of_birth = f"{student_data.std_place_of_birth}"

    '''Student Birth-Date Date of birth according to the Christian era in words "+std_enrollment_no+"'''
    try:
        std_born_date = f"{student_data.std_dob_db_co}"
        d = parser.parse(std_born_date)
        year = int(d.strftime("%Y"))  # year in number (ex. 2004)
        year_n = str(year)
        month = d.strftime("%B")  # month in word (ex. October)
        month_int = d.strftime("%m")  # month in number (ex. 10)
        day = d.strftime("%A")  # date in word (ex. Monday )
        day_int = d.strftime("%d")  # date in number (ex. 25 )
        day_in_word = me.from_user(day_int)

        """here converting int year to words and then ignoring 'and' word from it"""
        year = num2words(year)
        year_re = year.split(" ")
        ignore = ["and"]
        year_in_word = " ".join([t for t in year_re if not t in ignore])
    except Exception:
        pass
        # print("No date found")

    """Student Nationality"""
    std_nationality = f"{student_data.std_nationality}"

    """Student Institution last attained"""
    std_last = f"{student_data.std_institution_last_attained}"
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

    """Student Date of Admission"""
    std_Date_of_Admission = f"{student_data.std_Date_of_Admission}"

    """Student Enrollment No"""
    std_enrollment_no = str(f"{student_data.std_enrollment_no}")

    """Student Date of Leaving institute"""
    today = date.today()
    std_leaving_date = today.strftime("%B %d, %Y")
    student_data.std_leaving_date = str(std_leaving_date)
    db.session.commit()

    """Student Flag"""
    flag_no = "1"
    student_data.std_flag = str(flag_no)
    db.session.commit()

    """dna&beastBoi1025"""
    on_ref = std_collage_manager.query.filter_by(std_enrollment_no=1025).first()
    pdf_temp = BytesIO(on_ref.std_leavingtemp)
    page_to_merge = 0  # Refers to the First page of PDF
    input_pdf = PdfFileReader(pdf_temp)
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
    std_lc_no = str(std_lc_no)

    # Here i am writing the certificate pdf
    c.drawString(173, 683, std_registration_no)  # registration no.
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

    pdf_Bytes = io.BytesIO()
    output.write(pdf_Bytes)
    sl = leavingpages(
        std_enrollment_no=std_enrollment_no,
        std_leaving=pdf_Bytes.getvalue(),
    )
    db.session.add(sl)
    db.session.commit()


def check_for_flag(std_enrollment_no, conduct, progress, col_since, reason, remark):
    checker_cursor = co_students.query.filter_by(
        std_enrollment_no=std_enrollment_no
    ).first()
    if checker_cursor is not None:
        std_final_flag = str(f"{checker_cursor.std_flag}")
        if std_final_flag == "0":
            check_for_validation(
                std_enrollment_no, conduct, progress, col_since, reason, remark
            )
        else:
            pass
    else:
        pass


def check_for_validation(
    std_enrollment_no, conduct, progress, col_since, reason, remark
):
    checker_cursor = co_students.query.filter_by(
        std_enrollment_no=std_enrollment_no.replace(" ", "")
    ).first()
    if checker_cursor is not None:
        """From here pointer is going to the *generate_certificate()* function which is responsible for retrieving and writing a new leaving paper and coming back.# From here pointer is going to the *generate_certificate()* function which is responsible for retrieving and writing a new leaving paper and coming back."""
        generate_certificate(
            std_enrollment_no, conduct, progress, col_since, reason, remark
        )


def get_random_enroll(std_enrollment_no, conduct, progress, col_since, reason, remark):
    # eel.prompt_alerts("Demon's God DNA X BB")
    check_for_flag(std_enrollment_no, conduct, progress, col_since, reason, remark)
    # return bb


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
    std_department = request.form["department"]

    """result = print(enrollment.replace(" ", ""),register_num,email,sname,fname,mname,mo_no,country,postcode,address,state,sub_dist,district,allotment,man_entry,marry,gender,age,school_Last_2,birth_date,sub_cast,birth_place,collage_name_2,st_admission,)"""

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
        std_department=std_department,
        state=state,
        sub_dist=sub_dist,
        district=district,
        allotment=allotment,
        man_entry=man_entry,
        marry=marry,
        age=age,
        postal_code=postcode.replace(" ", ""),
    )

    leaving_data = co_students(
        std_enrollment_no=int(enrollment.replace(" ", "")),
        registration_no=register_num,
        std_Sub_caste=sub_cast,
        std_place_of_birth=birth_place,
        std_dob_db_co=birth_date,
        std_nationality=country,
        std_institution_last_attained=school_Last_2,
        std_Date_of_Admission=st_admission,
        std_flag=0,
    )

    data_name = co_std_name_sfm(
        std_enrollment_no=int(enrollment.replace(" ", "")),
        std_surname=sname,
        std_firstname=fname,
        std_middlename=mname,
    )

    db.session.add(data)
    db.session.add(data_name)
    db.session.add(leaving_data)
    # try:
    db.session.commit()
    # except IntegrityError as e:
    #     pass

    """redirect the user back to the previous page"""
    return "", 204


@app.route("/check-username/<username>")
def check_username(username):
    result = std_manager.query.filter_by(
        std_enrollment_no=username.replace(" ", "")
    ).first()
    result1 = co_std_name_sfm.query.filter_by(
        std_enrollment_no=username.replace(" ", "")
    ).first()

    result2 = co_students.query.filter_by(
        std_enrollment_no=username.replace(" ", "")
    ).first()

    if result and result1 and result2 is not None:
        return jsonify({"exists": True})
    else:
        return jsonify({"exists": False})


@app.route("/check-enroll/<enroll>")
def check_enroll(enroll):
    cl_page = leavingpages.query.get(enroll.replace(" ", ""))
    if cl_page is not None:
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
    regenerating = None
    regenerating = request.form.get("regenerating")

    if regenerating == "yes":
        flagger_ex = co_students.query.filter_by(
            std_enrollment_no=enrollment.replace(" ", "")
        ).first()
        flagger_ex.std_flag = str(0)
        cl_page = leavingpages.query.get(enrollment.replace(" ", ""))
        if cl_page:
            db.session.delete(cl_page)
        db.session.commit()

    """Call your Python function here, passing in the form data"""
    get_random_enroll(
        enrollment.replace(" ", ""), conduct, prog, col_since, reason, remark
    )
    """Return the nothing in the response object"""
    leaving_ref = leavingpages.query.filter_by(
        std_enrollment_no=enrollment.replace(" ", "")
    ).first()

    leaving_pdf = BytesIO(leaving_ref.std_leaving)
    response = make_response(leaving_pdf.getvalue())
    response.headers.set("Content-Type", "application/pdf")
    response.headers.set(
        "Content-Disposition",
        "attachment",
        filename="lc_of" + enrollment.replace(" ", "") + ".pdf",
    )
    return response


@app.route("/data")
def get_data():
    # Load data from a JSON file
    with open("static/dtstatic/data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)


@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = user_login.query.filter_by(username=username, password=password).first()
        if user is not None:
            total_stu_ = std_manager.query.count()
            print("Here ", total_stu_)
            return render_template("index.html", total_stu_=total_stu_)
        else:
            error = "Invalid Credentials. Please try again."
    return render_template("login.html")


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/datatable")
def datatable():
    return render_template("datatable.html")


@app.before_first_request
def create_table():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
