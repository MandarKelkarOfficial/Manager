import mysql.connector

# establish connection
mydb = mysql.connector.connect(
    host="localhost",
    port="6681",
    user="BeastBoi",
    password="@beastboi7DemonGOD@dna7",
    database="snow_crystals",
)

# create cursor object
mycursor = mydb.cursor()

# execute SELECT statement
mycursor.execute("SELECT * FROM co_students WHERE std_enrollment_no = 2001170266")

# fetch all rows from the table
result = mycursor.fetchall()

# iterate over the result set
for row in result:
    enroll = row[0]
    email = row[1]
    registration_no = row[2]
    std_sub_cate = row[3]
    std_birthplace = row[4]
    std_birthdate = row[5]
    std_nationality = row[6]
    std_institution_last_attended = row[7]
    std_admission_date = row[8]
    std_leaving_date = row[9]
    std_lc_no = row[10]

mycursor.execute("SELECT * FROM co_std_name_sfm WHERE std_enrollment_no = 2001170266")

# fetch all rows from the table
result = mycursor.fetchall()

# iterate over the result set
for row in result:
    surname = row[1]
    fname = row[2]
    mname = row[3]

print(
    type(enroll),
    type(email),
    registration_no,
    std_sub_cate,
    std_birthplace,
    std_birthdate,
    std_nationality,
    std_institution_last_attended,
    std_admission_date,
    std_leaving_date,
    std_lc_no,
)
print(fname)
print(mname)
print(surname)
