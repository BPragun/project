from student import *
from teacher import *
from json_file_manager import *
choice=int(input("Press 1 to quick view student details and result.\nPress 2 for other operations.\n"))
if choice==1:
    std1=Student
    t1=Teacher
    roll=int(input("Enter your roll to view your details and result."))
    std1.single_student_rank(roll)

if choice==2:
    t2=Teacher
    std2=Student
    print(f"We need your teacher id to verify you are a teacher:")
    teacherid=int(input("Enter your teacher ID::"))
    y_n=t2.validate_teacher(teacherid)
    if y_n==True:
        print("Welcome::")
        option=int(input("Press 1 for Student data manipulation.\nPress 2 for Teacher data manipulation.\n"))
        if option==1:
            option1=int(input("Enter your decision :\nPress 1 for creating file.\nPress 2 for appending student data in file.\nPress 3 for deletion of student data.\nPress 4 for displaying all students details.\nPress 5 for viewing highest and lowest marks in class.\nPress 6 for viewing all the students results i.e either pass or fail.\nPress 7 for viewing percentage and details of a specified student.\n"))
            
            if option1==1:
                std2.create_file()
                
            elif option1==2:
                std2.append_file()
                
            elif option1==3:
                eroll=int(input("Enter the roll no of student whose data you want to delete."))
                std2.delete_contents_of_student_file(eroll)
                print("Successfully deleted from students file.")
                
            elif option1==4:
                std2.all_students_info()
            
            elif option1==5:
                std2.highest_and_lowest_marks_class()
            
            elif option1==6:
                std2.pass_and_fail_students()
            
            elif option1==7:
                proll=int(input("Enter the roll no of student whose details you want to view."))
                std2.single_student_rank(proll)
            
            else:
                print("Enter valid information.")
        
        elif option==2:
            option2=int(input("Press 1 to add data in teacher file.\nPress 2 to delete data from teacher file.\nPress 3 to display details of teacher.\n"))
            if option2==1:
                t2.append_file()
            
            elif option2==2:
                idt=int(input("Enter the teacher id to delete data."))
                t2.delete_contents_of_teacher_file(idt)
                print("Successfully deleted data from teacher file.")
            
            elif option2==3:
                t2.all_teachers_info()
                
            else:
                print(f"Enter a valid option.")
                
    else:
        print("The entered teacher id is wrong.")
     