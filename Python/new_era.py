import io
import re
import os
import time
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


mydb = mysql.connector.connect(
    host="localhost",
    port="6681",
    user="BeastBoi",
    password="@beastboi7DemonGOD@dna7",
    database="snow_crystals",
)
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
