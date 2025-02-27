import json
from data_check import *
json_data_student=[]
json_data_teacher=[]
def create_student_file():
        namestd=input("Enter the name of student.")
        rollstd=int(input("Enter the roll of the student."))
        addressstd=input("Enter the address of the student.")
        marksstd=[]
        for i in range(0,5,1):
            value=float(input("Enter the marks of the student."))
            marksstd.append(value)
        phonestd=int(input("Enter the phone no of the student."))
        number_check(phonestd)
        emailstd=input("Enter the email of the student.")
        email_validation(emailstd)
        json_data_student.append({
            "Name":namestd,
                "Address":addressstd,
                "Email":emailstd,
                "Marks":marksstd,
                "Roll":rollstd,
                "Phone":phonestd 
            
        })
        
        with open("student.json","w") as file:
            json.dump(json_data_student,file,indent=3)
            print("Successfully added data in file.\n")
    
def append_in_student_file():
    n=int(input("Enter the no of data you want to insert."))
    for i in range(0,n,1):
        namestd=input("Enter the name of student.")
        rollstd=int(input("Enter the roll of the student."))
        addressstd=input("Enter the address of the student.")
        phonestd=int(input("Enter the phone no of the student."))
        number_check(phonestd)
        emailstd=input("Enter the email of the student.")
        email_validation(emailstd)
        marksstd=[]
        for i in range(0,5,1):
            value=float(input("Enter the marks of the student."))
            marksstd.append(value)
        
        with open("student.json","r") as file:
            json_data_student=json.load(file)
        json_data_student.append({
            "Name":namestd,
                "Address":addressstd,
                "Email":emailstd,
                "Marks":marksstd,
                "Roll":rollstd,
                "Phone":phonestd 
            
        })
        with open("student.json","w") as file:
            json.dump(json_data_student,file,indent=3)
            print("Successfully written data in file.\n")
    
def view_contents_of_student_file():
    with open("student.json","r") as file:
        content=json.load(file)
        return(content)

def create_teacher_file():
        nametea=input("Enter the name of teacher.")
        subjecttea=input("Enter the subject of the teacher.")
        addresstea=input("Enter the address of the teacher.")
        phonetea=int(input("Enter the phone no of the teacher."))
        number_check(phonetea)
        emailtea=input("Enter the email of the teacher.")
        email_validation(emailtea)
        idtea=int(input("Enter the id no of teacher."))
        json_data_teacher.append({
                "Name":nametea,
                "Address":addresstea,
                "Email":emailtea,
                "Subject":subjecttea,
                "ID":idtea,
                "Phone":phonetea
            
        })
        
        with open("teacher.json","w") as file:
            json.dump(json_data_teacher,file,indent=3)
            print("Successfully added data in file.\n")
            
def append_in_teacher_file():
    n=int(input("Enter the no of data you want to insert."))
    for i in range(0,n,1):
        nametea=input("Enter the name of teacher.")
        subjecttea=input("Enter the subject of the teacher.")
        addresstea=input("Enter the address of the teacher.")
        phonetea=int(input("Enter the phone no of the teacher."))
        number_check(phonetea)
        emailtea=input("Enter the email of the teacher.")
        email_validation(emailtea)
        idtea=int(input("Enter the id no of teacher."))
        with open("teacher.json","r") as file:
            json_data_teacher=json.load(file)
        json_data_teacher.append({
                "Name":nametea,
                "Address":addresstea,
                "Email":emailtea,
                "Subject":subjecttea,
                "ID":idtea,
                "Phone":phonetea
            
        }) 
        with open("teacher.json","w") as file:
            json.dump(json_data_teacher,file,indent=3)
            print("Successfully added data in file.\n")
    
    

def view_contents_of_teacher_file():
    with open("teacher.json","r") as file:
        content=json.load(file)
        return(content)

if __name__=="__main__":
    print("From the json manager file.")
