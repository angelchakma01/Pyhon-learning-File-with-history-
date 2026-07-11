

number = int(input("Enter Your Number :"))

if number >=80:
    print("you got A+")
    if number <= 70:
        print('you got A')
        if number <= 50:
            print("You Got C")
        else:
            print("You Not got c")
    else:
        print("You not got A")

else:
    print("You Not got A+")


# 
age = 22
student = True
cgpa = 3.20
has_id = False

if age >= 18:#Alowed this statment
    if student:     
        if cgpa >= 3.50:# this stetment not allowed
            print("Scholarship")
        else:
            if has_id: # This statment not allowed
                print("Exam Allowed") 
            else: # it's work
                print("Bring ID")
    else:
        print("Not a Student")
else:
    print("Minor")

print("End")
