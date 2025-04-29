from course import Course
from student import Student

def main():
    course = Course()
    print("\nEnter student information (FirstName LastName GPA), or type 'done' to finish:")

    while True:
        user_input = input("Enter student info: ")
        if user_input.lower() == "done":
            break

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input. Please follow the instruction: FirstName LastName GPA")
            continue

        first_name = parts[0]
        last_name = parts[1]
        try:
            gpa = float(parts[2])
        except ValueError:
            print("Invalid GPA. Please enter a number.")
            continue

        student = Student(first_name, last_name, gpa)
        course.add_student(student)

    print("Dean's List:")
    deans_list = course.getDeansList()
    if deans_list:
        for student in deans_list:
            print(f"- {student.first_name} {student.last_name}, GPA: {student.getGPA()}")
    else:
        print("No students qualified for the Dean's List.")

if __name__ == "__main__":
    main()

