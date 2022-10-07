import sys

def add_student(student):
    f = open("students.txt", "a")
    f.write(student+"\n")

def show_students():
    f = open("students.txt", "r")
    for line in f:
        print(line)

def delete_student(student):
    f = open("students.txt", "r")
    list = []
    for line in f:
        list.append(line)

    list.remove(student+"\n")
    metin = ""
    for i in list:
        metin += i
    f = open("students.txt", "w")
    f.write(metin)

    
if sys.argv[1] == "add":
    student = sys.argv[2]
    for i in range(3,len(sys.argv)):
        student += " " + sys.argv[i]

    add_student(student)

elif sys.argv[1] == "show":
    show_students()

elif sys.argv[1] == "delete":
    student = sys.argv[2]
    for i in range(3,len(sys.argv)):
        student += " " + sys.argv[i]
    delete_student(student)
