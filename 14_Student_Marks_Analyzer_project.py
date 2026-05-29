""" Numpy Project :
    Student Marks Analysis

 A CLI-based data analysis mini project built using Python and NumPy."""

# CODE:

import numpy as np

students = ["Aman", "Riya", "Kunal", "Simran"]
marks = np.array([
    [78, 85, 90],
    [67, 72, 80],
    [88, 91, 95],
    [60, 65, 70]
])

# Total marks for each student
total_marks = np.sum(marks , axis = 1)
print("Total marks for each student : ", total_marks)

# Average marks of each student
average_marks = np.average(marks , axis = 1)
print("\nStudent Performance Summary:")

for i in range(len(students)):
    avg = average_marks[i]

    if avg >= 85:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    else:
        grade = "C"

    print(f"{students[i]} - Total: {total_marks[i]}, Average: {avg:.2f}, Grade: {grade}")

# Subject-wise average
subject_average = np.average(marks , axis = 0)
print("Average marks of each subject : ",subject_average)

# Top scoring student index
top_student_index = np.argmax(total_marks)
print("Top student  : ", students[top_student_index])

# Student with average < 75
low_performers = np.where(average_marks < 75)[0]
print("Students with average < 75 :")
for index in low_performers:
    print(students[index])
