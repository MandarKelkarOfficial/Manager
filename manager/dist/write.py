import json
from os import path
import io
import re
import os
import time
import cv2
import eel
import webbrowser
import pandas as pd
import mysql.connector
from dateutil import parser
from datetime import date
from datetime import datetime
from num2words import num2words
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen.canvas import Canvas

filename = "D:/Programming/Python/Z Way Outer Scrape/datatables/dist/data.json"


listObj = {}

if path.isfile(filename) is False:
    raise Exception("File not found")

with open(filename) as fp:
    listObj = json.load(fp)

print(listObj)
print(type(listObj))


def setData(name, position, office, age, datestart, salary):
    listObj["data"].append(
        {
            "Name": name,
            "Position": position,
            "Office": office,
            "Age": age,
            "StartDate": datestart,
            "Salary": salary,
            "compData": "<i class='fas fa-xmark' ></i></i><span class='tooltip'>Notifying</span>",
        }
    )

    print("called")
    print(listObj)
    with open(filename, "w") as json_file:
        json.dump(listObj, json_file, indent=4, separators=(",", ":"))
    print("Successfully appended to the JSON file")


def close_callback(route, websocket):
    if not websocket:
        print("Bye!")
        exit()


eel.init("Z Way Outer Scrape/datatables/dist")


# # @eel.expose
# # def get_random_name():
# #     eel.prompt_alerts("Demon's God DNA X BB")


@eel.expose
def get_random_enroll(name, position, office, age, datestart, salary):
    # eel.prompt_alerts("Demon's God DNA X BB")
    setData(name, position, office, age, datestart, salary)

    return "Good"


# Instead writing size and position tuples of app separately we can create its dictionary and pass it to the geometry arguments
geometry = {"size": (700, 480), "position": (0.0)}
eel.start(
    "index.html",
    mode="chrome",
    host="localhost",
    port=27000,
    blocking=True,
    geometry=geometry,
    disable_cache=True,
    close_callback=close_callback,
    cmdline_args=["--incognito", "--no-experiment"],
)
