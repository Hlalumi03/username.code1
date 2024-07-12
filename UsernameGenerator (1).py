from xml.dom import UserDataHandler
from datetime import datetime
current_year = datetime.now().year

def user_details():
    firstname = input("Enter your name: ")
    if not firstname.isalpha():
        print("invalid first name")
    while True:
        if firstname.isalpha():
            print(firstname)
            break

        name = input("Enter a name: ")
        if not name.isalpha():
            print("invalid name")
        elif name.isalpha():
            print(name)
            break

    surname = input("Enter your last name: ")
    if not surname.isalpha():
        print("invalid last name")

    while True:
        if surname.isalpha():
            print(surname)
            break

        lastname = input("Enter last name: ")
        if not lastname.isalpha():
            print("invalid name")
        elif lastname.isalpha():
            print(lastname)
            break

    cohort = current_year
    cohort = int(input("insert your cohort: "))

    if cohort != current_year:
        print("invalid cohort")
        
    while True:
        if cohort == current_year:
            print(cohort)
            break
        
        year = int(input("Enter cohort: "))
        if year != current_year:
            print("invalid year")
        
        elif year == current_year:
            print(year)
            break

user_details()

def campuses():
    campus = {
        "johannesburg" : "JHB",
        "cape town" : "CPT",
        "durban" : "DBN",
        "phokeng" : "PHO"
    }

    campus = input("Enter campus you will be attending in: ")

    while True:
        if campus == "johannesburg":
            print(campus)
            break

        elif campus == "cape town":
            print(campus)
            break
        
        else:
            return ("invalid campus")
