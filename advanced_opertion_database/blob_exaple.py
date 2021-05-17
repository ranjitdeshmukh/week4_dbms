"""
@author : ranjit
Created Date : 17/3/2021
Updated date : 17/3/2021
Title : Store the file using the blob
"""

import mysql.connector as mysql


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(emp_id, name, photo, biodataFile):
    print("Inserting BLOB into python_employee table")
    try:
        mydb = mysql.connect(
        port=3306,
        user="root",
        password="root",
        host='127.0.0.1',
        db='hospitalmanagment',
        auth_plugin='mysql_native_password'
        )
        cursor = mydb.cursor()
        sql_insert_blob_query = " INSERT INTO python_employee (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"
        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(biodataFile)
        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, empPicture, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.DatabaseError as e:
        print("Failed inserting BLOB data into MySQL table {}",str(e))


insertBLOB(1, "ram", r"C:\Users\Ranjit deshmukh\Desktop\degree.jpeg",
           r"C:\Users\Ranjit deshmukh\Desktop\Daily use full cammand for python.txt")
