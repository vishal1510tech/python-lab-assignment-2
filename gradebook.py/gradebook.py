# GRADEBOOK ANALYZER
# NAME = VISHAL SINGH
# date =5-11-2025
# TITLE = Analyzing and Reporting Student grades
# HI, welcome to this program reads student grades from a file, calculates averages, and generates a report.
number_of_student =int(input("Enter number of students: "))
marks={}
for number_of_student in range(number_of_student):
    student_name = input("Enter student name: ")
    student_mark = float(input("Enter student mark: "))
    marks[student_name]=student_mark
print(marks)

def calculate_average(marks):
    total=sum(marks.values())
    average=total/len(marks)
    return average
average=calculate_average(marks)
print("Average mark:", average)

def calculate_median(marks):
    sorted_marks=sorted(marks.values())
    l=len(sorted_marks)
    if l%2==0:
        median=(sorted_marks[l//2-1]+sorted_marks[l//2])/2
    else:
        median=sorted_marks[l//2]
    return median
median=calculate_median(marks)
print("Median mark:", median)

def calculate_highest_mark(marks):
    calculate_highest_mark=max(marks.values())
    return calculate_highest_mark
highest=calculate_highest_mark(marks)
print("Highest mark:", highest)

def calculate_lowest_mark(marks):
    calculate_lowest_mark=min(marks.values())
    return calculate_lowest_mark
lowest=calculate_lowest_mark(marks)
print("Lowest mark:", lowest)

grades={}
grades_counts={"A":0,"B":0,"C":0,"D":0,"F":0}
for student,mark in marks.items():
    if mark>=90:
        grades[student]="A"
        grades_counts["A"]+=1
    elif mark>=80:
        grades[student]="B"
        grades_counts["B"]+=1
    elif mark>=70:
        grades[student]="C"
        grades_counts["C"]+=1
    elif mark>=60:
        grades[student]="D"
        grades_counts["D"]+=1
    else:
        grades[student]="F"
        grades_counts["F"]+=1
print("Grades:", grades)
print("Grade distribution:", grades_counts)

passed_students=[student for student,mark in marks.items() if mark>=60]
print("Passed students:",passed_students)
print(len(passed_students),"students passed the exam.")
failed_students=[student for student,mark in marks.items() if mark<60]
print("Failed students:",failed_students)
print(len(failed_students),"students failed the exam.")

print(f"{'Name':<12} {'Marks':<8} {'Grade':<6}")
print("-" * 28)

for student, mark in marks.items():
    grade = grades[student]
    print(f"{student:<12} {mark:<8} {grade:<6}")

print("\nGrade Distribution:")
print(f"{'Grade':<6} {'Count'}")
print("-" * 14)
for grade, count in grades_counts.items():
    print(f"{grade:<6} {count}")

print("\nPassed Students:")
for student in passed_students:
    print(student)
print(f"Total Passed: {len(passed_students)}")

print("\nFailed Students:")
for student in failed_students:
    print(student)
print(f"Total Failed: {len(failed_students)}")




