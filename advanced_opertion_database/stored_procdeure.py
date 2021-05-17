"""
@author : ranjit
Created Date :16/03/2021
Updated Date :17/03/2021
Title : stored Procdure function 
"""
from logger import Logger
import mysql.connector as mysql

logger = Logger('logfile').get()
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
    cursor.callproc('show_data')
    # print results
    print("Print patient details")
    for result in cursor.stored_results():
        print(result.fetchall())
except mysql.errors.DatabaseError as e:
    logger.error(str(e))
    print("Function is not availabel in the data base")
finally:
    mydb.close()
