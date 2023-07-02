from tokenize import Name
import mysql.connector

# user = int(input("Enter your ID: "))
NameID = []
ix = []
idx = []
connection2 = mysql.connector.connect(host='localhost',
                                            database='absensi',
                                            user='root',
                                            password='')

# if connection2.is_connected():
#     print("berhasil konek")
cursor = connection2.cursor()
cursor.execute("SELECT * FROM python_employee")
record = cursor.fetchall()
for row in record:
    # print("Id = ", row[0], )
    # print(row[1])
    NameID = row[0]
    idx.append(NameID)
    ix=NameID
    # print(ix)
    # get last index of id
def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

class getData:
    global NameID
    di = NameID

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def readBLOB(emp_id):
    print("Reading BLOB data from python_employee table")

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='absensi',
                                             user='root',
                                             password='')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from python_employee where id = %s"""
        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )
            NameID = row[0]
            print("Name = ", row[1])
            print(row[2])
            nama = row[1]
            image = row[2]
            file = row[3]
            print("Storing employee image and bio-data on disk \n")
            write_file(image, "path folder\{}".format(nama)) 

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
# store image and bio-data on disk
def insertBLOB(name, photo, biodataFile):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='absensi',
                                             user='root',
                                             password='')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO python_employee
                          (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(biodataFile)
        # Convert data into tuple format
        nm = NameID.append
        insert_blob_tuple = (nm, name, empPicture, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# update bio-data
def updateBLOB(name, photo, biodataFile):
    print("Updating BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='absensi',
                                             user='root',
                                             password='')

        cursor = connection.cursor()
        sql_update_blob_query = """ UPDATE python_employee SET name = %s, photo = %s, biodata = %s WHERE id = %s """

        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(biodataFile)
        # Convert data into tuple format
        update_blob_tuple = (name, empPicture, file, 1)
        result = cursor.execute(sql_update_blob_query, update_blob_tuple)
        connection.commit()
        print("Image and file updated successfully in python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed updating BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# updateBLOB("Eric", "John.png", "absensi.csv")



# readBLOB(1, "D:\python project\Object-Detection-With-python-main\Koboserveroutputs",
#         "D:\python project\Object-Detection-With-python-main\Koboserveroutputs\\absensi.csv")
