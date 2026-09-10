# # Topic: Custom Modules, Lists, Tuples, and Sets
# # Task 1
# def Welcome():
#     print("Welcome to Student Management")
#     #Displays all student names.
# def display_students(student_list):
#     print("Student List:")
#     for std in student_list:
#         print(std)
#     # Returns the total number of students.
# def total_students(student_list):
#     print("Total Students:")
#     return len(student_list)


print("Topic: Custom Modules, Lists, Tuples, and Sets")
# #Task 2:
print("Lists")
import college
college.Welcome()
print("Display all student.")
std = ["Taiba","Eman","Bisma","Noor","Aisha"]
college.display_students(std)
print("Add new student Aneela")
std.append("Aneela")
print("Remove one student Taiba")
std.remove("Taiba")
print("Update one student's name Fatima")
std[2] = "Fatima"
print("Display the updated list")
college.display_students(std)
print(" Display the total number of students using the custom module")
print(college.total_students(std))
# Task 3:

print("Tuples")
student = (15,"ComputerScience","5th smester")
print( "Roll no:",student[0],"\nDepartnment:",student[1],"\nSmester:",student[2])
#student[1] = "English"
print("'tuple' object does not support item assignment")
# Task 4:
print("Sets")
clubs = {"Sports","Drama","Sports","Debate","Cricket","Drama"}
print("Display the set")
print("Club Names:")
print(clubs)
print("Add one new club Science")
clubs.add("Science")
print("Remove one club Drama")
clubs.remove("Drama")
print(clubs)
# #Check whether a club exists using the in operator.
print("Check a club")
print("Drama" in clubs)
