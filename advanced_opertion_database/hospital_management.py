from hospital import Hospital
from datetime import timedelta
import datetime
from logger import Logger
import mysql.connector as mysql
logger = Logger('logfile').get()

"""
@author : Ranjit
created Date : 13/03/2021
updated Date : 13/03/2021
title : Hospital managment
"""


def add_doctor(hospital):
    #ADDING PROMPT AND ERROR CHECKING
    while True:
        try:
            new_name = input('Enter the name of the doctor: ').lower()
            assert new_name.isalpha(), "Only letters are allowed!"
            specialization = input("Enter the specialition of doctor: ")
            date_entry = input('Enter a date in YYYY-MM-DD format')
            year, month, day = map(int, date_entry.split('-'))
            date = datetime.date(year, month, day)
            hospital.add(new_name, specialization, date)
            break
        except Exception as e:
            Logger.error(str(e))


def addAppointment(hospital):
    #ADDING PROMPT AND ERROR CHECKING
    while True:
        try:
            docname = input("Please Enter the doc name : ")
            date_entry = input('Enter a date in YYYY-MM-DD format')
            year, month, day = map(int, date_entry.split('-'))
            date = datetime.date(year, month, day)
            if hospital.check_doc(docname, date):
                print("This date Doctor Appointment is full try another day")
                continue
            new_name = input('Enter the name of the patient: ').lower()
            assert new_name.isalpha(), "Only letters are allowed!"
            mobile = int(input("Enter the mobile number of patient: "))
            age = int(input("Enter the age number of patient: "))
            hospital.add_appointment(new_name, mobile, age)
            break
        except Exception as e:
            print("Invalid choice! try again! " + str(e))


def search_doctor(hospital):
    #SEARCHING PROMPT AND ERROR CHECKING
    print('Searching Doctor')
    print('===================')
    search = (input("Enter name of doctor: "))
    result = hospital.search_doctor(search)
    # print(result)
    if result is None:
        print("doctor not in hospital")
    else:
        ID, name, specialization, name_doc = result
        print('ID Number: ', ID)
        print('NAme:     ', name)
        print('Specialization', specialization)
        print('----------')


def search_patient(hospital):
    #SEARCHING PROMPT AND ERROR CHECKING
    print('Searching Patient')
    print('===================')
    search = (input("Enter patient name: "))
    result = hospital.search_patient(search)
    if result is None:
        print("patient not in hospital")
    else:
        ID, name, mobile,age ,doc= result
        print('ID Number: ', ID)
        print('Name:     ', name)
        print('Age', age)
        print('----------')

def menuDisplay():
    #MENU FOR PROGRAM
    """Display the menu"""
    print('=============================')
    print('= Hospital Management Menu =')
    print('=============================')
    print('(1) Add New Doctor to Hospital')
    print('(2) Add New Appointment to Hospital')
    print('(3) Search doctor')
    print('(4) Search patinet in hopital')
    print('(5) Show all patinet in day order')
    print('(0) Quit')


def show_allPatinet(hospital):
    #SEARCHING PROMPT AND ERROR CHECKING
    print('Searching Patient')
    print('===================')
    result = hospital.show_allPatinet()

    if result is None:
        print("patient not in hospital")
    else:
        for data in result:
            ID, name, mobile, age, doc = data
            print('ID Number: ', ID)
            print('Name :     ', name)
            print('Age :  ', age)
            print('----------')




def main():
    #PROGRAM RUNNING COMMAND AND ERROR CHECKING
    hospital = Hospital()
    print(hospital)
    while True:
        try:
            menuDisplay()
            CHOICE = int(input("Enter choice: "))
            if CHOICE in [1, 2, 3, 4, 5, 0]:
                if CHOICE == 1:
                    add_doctor(hospital)
                elif CHOICE == 2:
                    addAppointment(hospital)
                elif CHOICE == 3:
                    search_doctor(hospital)
                elif CHOICE == 4:
                    search_patient(hospital)
                elif CHOICE == 5:
                    show_allPatinet(hospital)
                elif CHOICE == 0:
                    break
        except Exception as e:
            logger.error(e)

        # If the user pick an invalid choice,
        # the program will come to here and
        # then loop back.


#driver code
if __name__ == '__main__':
    main()
