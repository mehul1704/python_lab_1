subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))
subject4 = float(input("Enter marks for Subject 4: "))
subject5 = float(input("Enter marks for Subject 5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5

average_marks = total_marks / 5

if average_marks >= 90:
    grade = "A"
elif average_marks >= 80:
    grade = "B"
elif average_marks >= 70:
    grade = "C"
elif average_marks >= 60:
    grade = "D"
else:
    grade = "F"

print("Marksheet:")
print("-----------")
print("Subject 1: ", subject1)
print("Subject 2: ", subject2)
print("Subject 3: ", subject3)
print("Subject 4: ", subject4)
print("Subject 5: ", subject5)
print("-----------")
print("Total Marks: ", total_marks)
print("Average Marks: ", average_marks)
print("Grade: ", grade)