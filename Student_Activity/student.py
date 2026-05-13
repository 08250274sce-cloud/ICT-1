file = open('Students.xlsx', 'w')
file.write("Name, ID\n")
file.write("Rinchen, 08250274\n")
file.write("Zam, 08250275\n")
file.write("Pem, 08250276\n")
file.write("Tashi, 08250277\n")
file.write("kinga, 08250278\n")
file.close()
file = open('Students.xlsx', 'r')
students = file.read()
print(students)
file.close()
searchN = input("Enter name to search: ")
found = False
with open('Students.xlsx', 'r') as file:
    for student in file:
        if searchN.lower() in student.lower():
            print(student)
            found = True
            break
if not found:
    print("Name not found in the file.")
print()