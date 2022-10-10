
students = [] #List of students

# This Welcome function will run at the start of the program
def welcome():
  print("\n-----------------------------")
  print("\t\t✨ Welcome ✨")
  print("-----------------------------\n")

# =========== Create Student Function ============
def createStudent():
 
  print("\nAdd student details\n")
  name = input("Enter student's name: ")
  email = input("Enter student's E-mail: ")
  contact = input("Enter student's contact number: ")
  address = input("Enter student's Address: ")

  # Dictionary of student
  student = {
    "Name": name,
    "E-mail": email,
    "Contact": contact,
    "Address": address
  }
 
  students.append(student) # Enter student dictionary in students list
 
  print("\n---------------------------------")
  print("  Student Created Successfully 🎉")
  print("----------------------------------\n")

# =========== Update Student Function ============
def updateStudent():
  print("Student Update...\n")
 
  studentList() # Show the list of students
 
  try:
    index = int(input("Enter Sr no. you want update: "))
    index = index - 1
    x = len(students)
    if index < x and index >= 0 :
      name = input("\nEnter student's new name: ")
      email = input("Enter student's new E-mail: ")
      contact = input("Enter student's new contact number: ")
      address = input("Enter student's new Address: ")
 
      student = {
        "Name": name,
        "E-mail": email,
        "Contact": contact,
        "Address": address
      }
     
      student.update({"Name": name})
      student.update({"E-mail": email})
      student.update({"Contact": contact})
      student.update({"Address": address})

      # The update function will first remove the student and then insert new details
      students.remove(students[index])
      students.insert(index,student)

      print("\n----------------------------------")
      print("  Student Updated Successfully 🎉")
      print("----------------------------------\n")
    else:
      print("\n!!!!!!!!!!!!!!!!!!!!!! Update Unsuccessful !!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!  Sr no. does not exist !!!!!!!!!!!!!!!!!!!\n")
     
  except:
    print("\n!!!!!!!!!!!!!!!! Invalid Input! !!!!!!!!!!!!!!!!\n")

# =========== Delete Student Function ============
def deleteStudent():
 
  studentList() #show Student List
  try:
    index = int(input("Enter Sr no. you want delete: "))
    index = index - 1
    x = len(students) # Return number of dictionaries in the list
    if index < x and index >= 0:
      students.remove(students[index])
     
      print("\n------------------------------------------")
      print("\t💢 Student successfully deleted 💢")
      print("------------------------------------------\n")
   
    else:
       print("\n!!!!!!!!!!!!!!!!!!!!!! Delete Unsuccessful !!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!! Sr no. does not exist !!!!!!!!!!!!!!!!!!!!!\n")
  except:
    print("\n!!!!!!!!!!!!!!!! Invalid Input! !!!!!!!!!!!!!!!!\n")
     
# =========== Student List Function ============
def studentList():
  try:
    for x in range(0, 100):
      Y = str(students[x].items())
      index = students.index(students[x])
      index = index + 1
      print("Sr no.",index ,"\n"+ Y[10:],"\n")
     
  except:
    print("--------------------")

# =========== Student List All Function ============
def listAllStudent():
 
  x = len(students)
  if x == 0:
    print("List is empty")
  else:
    print("\n--------------------")
    print("List of all Students")
    print("--------------------\n")
    studentList()
 
# =========== Exit Function ============
def exit():
  print("\n---------------------------------------------")
  print("\tThanks for using My application...❤")
  print("---------------------------------------------\n")

welcome()
choice = 0

# The loop will execute continuously until user input 5
while choice != 5:
  print("-----------------------------------------------------------")
  print("Operations:\n")
  print("1. Create student")
  print("2. Update student")
  print("3. Delete student")
  print("4. List all students")
  print("5. Exit Application")

  try:
    print("\n-----------------------")
    choice = int(input("  Enter Operation: "))
    print("-----------------------\n")
   
    if choice == 1:
      createStudent()
 
    elif choice == 2:
      updateStudent()
 
    elif choice == 3:
      deleteStudent()
 
    elif choice == 4:
      listAllStudent()
 
    elif choice == 5:
      exit()
     
    else:
      print("xxxxxxxxxxxxx Invalid Operation xxxxxxxxxxxxx\n")
  except:
    print("\n!!!!!!!!!!! Invalid input! Enter Operation Number !!!!!!!!!!!\n")
# The Program ends Here !!!!!!!!