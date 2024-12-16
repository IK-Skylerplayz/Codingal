student_name = input("Enter the student's name: ")
total_classes = int(input("Enter the total number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))
marks = float(input("Enter the student's average marks: "))

attendance_percentage = (classes_attended / total_classes) * 100
required_attendance = 75
required_marks = 40

if attendance_percentage >= required_attendance and marks >= required_marks:
    print(f"{student_name} is eligible to take the exam.")
else:
    print(f"{student_name} is not eligible to take the exam.")
    if attendance_percentage < required_attendance:
        print(f"Reason: Attendance percentage is too low ({attendance_percentage:.2f}%).")
    if marks < required_marks:
        print(f"Reason: Marks are below the required average ({marks:.2f}).")
