students_data = {
    "Student1": [85, 90, 78, 92, 88],
    "student2": [75, 88, 92, 80, 87],
    "student3": [90, 95, 89, 78, 93],
    "student4": [80, 85, 88, 92, 87],
    "student5": [92, 88, 95, 90, 85],
}

highest_marks = 0
highest_student_name = " "

for name, marks in students_data.items():
    total = sum(marks)
    if total > highest_marks:
        highest_marks = total
        highest_student_name = name

print(highest_student_name)
print(highest_marks)
