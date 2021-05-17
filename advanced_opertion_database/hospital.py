from dotenv import load_dotenv
import os
from datetime import timedelta
import datetime
from logger import Logger
import mysql.connector as mysql
logger = Logger('logfile').get()

user = os.environ.get("USER")
password = os.environ.get("password")


class Hospital:
    """this used the manage the all operations of hospital"""

    def __init__(self):
        self.mydb = mysql.connect(
            port=3306,
            user="root",
            password='root',
            # host='127.0.0.1',
            auth_plugin='mysql_native_password',
            database="hospitalmanagment"
        )
        self.mycursor = self.mydb.cursor()
        print(self.mycursor, "1234")

    def remove(self, ID):
        #REMOVING ITEMS FOR LISTS AND OUTPUT DOCUMENT
        del self.items[ID]
        self.save()

    def add(self, name, specialization, time):
        #adding the doctor in the data base
        sql = 'INSERT INTO docotor(name_doc , specialization,date_time) VALUES(%s,%s,%s)'
        val = (name, specialization, time)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("Data inserted succesfully")

    def add_appointment(self, patient, mobile, age):
        try:
            #ADDING ITEMS FOR LISTS AND OUTPUT DOCUMENT
            sql = 'INSERT INTO patient(patient , mobile,age,docotr_id) VALUES(%s,%s,%s)'
            val = (patient, mobile, age)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print("Data inserted succesfully")
        except Exception as e:
            print('sometings went to wrong  '+str(e))

    def check_doc(self, name_doc, date):
        try:
            self.mycursor.execute(
                " SELECT * FROM docotor WHERE name_doc=name_doc "
            )
            myresult = self.mycursor.fetchall()
            if myresult:
                docotr_id = myresult[0]
                self.mycursor.execute("SELECT * FROM hospitalmanagment.patient WHERE docotr_id = docotr_id"
                                    )
                self.mycursor.fetchall()
                print(self.mycursor.fetchall())
                rc = self.mycursor.rowcount
            if rc == 5:
                return True
            elif myresult[0]:
                return myresult[0]
            else:
                return False
        except Exception as e:
            print(e) 

    def search_patient(self, patient):
        try:
            self.mycursor.execute(
                " SELECT * FROM patient WHERE patient=patient "
            )
            myresult = self.mycursor.fetchone()
            return myresult
        except Exception as e:
            print(e)

    def search_doctor(self, name_doc):
        try:
            self.mycursor.execute(
                " SELECT * FROM docotor WHERE name_doc=name_doc "
            )
            myresult = self.mycursor.fetchone()
            return myresult
        except Exception as e:
            print(e)
    
    def show_allPatinet(self):
        try:
            self.mycursor.execute(
                "SELECT * FROM patient ORDER BY patient"
            )
            myresult = self.mycursor.fetchall()
            return myresult
        except Exception as e:
            print(e)


