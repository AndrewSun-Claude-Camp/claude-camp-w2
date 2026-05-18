# Student Roster

import re
from datetime import datetime

def get_valid_choice():
    while True:
        choice = input("Select your choice (1 - 4): ")
        if choice in ["1","2","3","4"]:
            return choice
        else:
            print("Invalid selection. Please choose 1 - 4.")

def get_valid_name():
    while True:
        name = input("Enter student's name: ").strip()
        if not name:
            print("Name cannot be empty. Please try again.")
        elif len(name) > 50:
            print("Name cannot exeed 50 characters. Please try again.")
        elif not re.match(r"^[A-Za-z\s\-']+$", name):
            print("Name can only contain letters, space, hyphens, or apostrophes. Please try again.")
        else:
            return name
        
def get_valid_email():
    while True:
        email = input("Enter student's email: ").strip()
        if not email:
            print("Email cannot be empty. Please try again.")
        elif len(email) > 50:
            print("Email cannot exeed 50 characters. Please try again.")
        elif not re.fullmatch(r"^[A-Za-z0-9._%+-]+@[A-za-z0-9.-]+\.[A-za-z]{2,}$", email):
            print("Invalid email address. Please try again.")
        else:
            return email
        
def get_valid_date():
    while True:
        date_str = input("Enter Student's registration date in dd/MM/YYYY format:").strip()
        
        try:
            return datetime.strptime(date_str, "%d/%M/%Y")
        except ValueError:
            print("Invalid date. Please try again.")


students = {}

while True:
    print("Student Roster\n1. Add new student\n2. Remove a student\n3. Search a student\n4. Exit")
    choice = get_valid_choice()

    if choice == "1":
        Name = get_valid_name()
        Email = get_valid_email()
        RegDate = get_valid_date()

        if Name not in students:
            students[Name] = {
                "Email":Email,
                "Registration_Date":RegDate
            }
            print("Student added successfully.\n")
        else:
            print("Student has already registered.\n")
            
    elif choice == "2":
        Name = get_valid_name()
        
        if Name in students:
            del students[Name]
            print("Student has been removed.\n")
        else:
            print("Student not found.\n")

    elif choice == "3":
        Name = get_valid_name()

        if Name in students:
            print("Name: ",Name)
            print("Email: ",students[Name]["Email"])
            print("Registration Date: ",students[Name]["Registration_Date"],"\n")
        else:
            print("Student not found.\n")
    elif choice == "4":
        print("Exit\n") 
        break
    
        
