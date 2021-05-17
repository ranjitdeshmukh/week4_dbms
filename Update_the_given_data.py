"""
@author : ranjit
Created Date :12/03/2021
Updated Date :12/03/2021
Title : Updated Data sucess Fully
"""
from logger import Logger
import mysql.connector as mysql
logger = Logger('logfile').get()

try:
    mydb = mysql.connect(
        port=3306,
        user="root",
        password="root",
        # host='127.0.0.1',
        auth_plugin='mysql_native_password',
        database="mydatabase"
    )
    mycursor = mydb.cursor()
    mycursor.execute(
       "UPDATE student SET marks = '35' WHERE name = 'John' ")
    mydb.commit()
    print("Data Updated Sucess Fully")
except mysql.errors.DatabaseError as e:
    logger.error(str(e))
    print("Please provide the proper data")
finally:
    mydb.close()
