M1 = int(input("Enter marks of Subject 1: "))
M2 = int(input("Enter marks of Subject 2: "))
M3 = int(input("Enter marks of Subject 3: "))
M4 = int(input("Enter marks of Subject 4: "))
M5 = int(input("Enter marks of Subject 5: "))
TotalMarks =  (M1+M2+M3+M4+M5)
print("Total Marks:", TotalMarks)
percentage = (TotalMarks / 500) * 100
print("Percentage:",percentage)
if 90 <= percentage <= 100:
    print("Grade: A+")

elif 80 <= percentage < 90:
    print("Grade: A")

elif 70 <= percentage < 80:
    print("Grade: B")

elif 60 <= percentage < 70:
    print("Grade: C")

elif 0 <= percentage < 60:
    print("Grade: Fail")

else:
    print("Invalid Percentage")