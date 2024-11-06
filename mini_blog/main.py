class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display_student(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        new_student = Student(student_id, name, age, grade)
        self.students.append(new_student)
        print("Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student in self.students:
                student.display_student()
                print("-" * 20)

    def search_student(self):
        student_id = input("Enter Student ID to search: ")
        for student in self.students:
            if student.student_id == student_id:
                print("Student found:")
                student.display_student()
                return
        print("Student not found.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        for student in self.students:
            if student.student_id == student_id:
                print("Updating details for Student ID:", student_id)
                student.name = input("Enter new Name: ")
                student.age = int(input("Enter new Age: "))
                student.grade = input("Enter new Grade: ")
                print("Student details updated successfully.")
                return
        print("Student not found.")

    def exit_system(self):
        print("Exiting the Student Management System.")
        exit()

def menu():
    system = StudentManagementSystem()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            system.add_student()
        elif choice == 2:
            system.display_students()
        elif choice == 3:
            system.search_student()
        elif choice == 4:
            system.delete_student()
        elif choice == 5:
            system.update_student()
        elif choice == 6:
            system.exit_system()
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    menu()
