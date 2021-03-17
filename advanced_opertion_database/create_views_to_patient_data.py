

"""
@author : ranjit
Created Date :12/03/2021
Updated Date :12/03/2021
Title : making the connection of with database and creation the database
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
        auth_plugin='mysql_native_password',
        database="hospitalmanagment"
    )
    mycursor = mydb.cursor()
    sql = 'select * from new_patient'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if myresult:
        for data in myresult:
            print(data)
    else:
        print("Data is not present ,Thank you")
except mysql.errors.DatabaseError as e:
    logger.error(str(e))
    print("somethings went to wrong please tyr again")
finally:
    mydb.close()


