from tkinter import *
from tkinter import messagebox

class Student:
    def __init__(self, roll_no, name, course, contact , email):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.contact = contact
        self. email= email

class StudentManagementSystem:
    def __init__(self, root):
        self.students = []
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x600")

        self.label_roll_no = Label(root, text="Roll No:")
        self.label_roll_no.grid(row=1, column=0, padx=10, pady=10)
        self.entry_roll_no = Entry(root)
        self.entry_roll_no.grid(row=1, column=1, padx=10, pady=10)

        self.label_name = Label(root, text="Name:")
        self.label_name.grid(row=1, column=2, padx=10, pady=10)
        self.entry_name = Entry(root)
        self.entry_name.grid(row=1, column=3, padx=10, pady=10)

        self.label_course = Label(root, text="Course:")
        self.label_course.grid(row=1, column=4, padx=10, pady=10)
        self.entry_course = Entry(root)
        self.entry_course.grid(row=1, column=5, padx=10, pady=10)

        self.label_contact = Label(root, text="Mobile No:")
        self.label_contact.grid(row=2, column=0, padx=10, pady=10)
        self.entry_contact = Entry(root)
        self.entry_contact.grid(row=2, column=1, padx=10, pady=10)

        self.label_email = Label(root, text="Email:")
        self.label_email.grid(row=2, column=2, padx=10, pady=10)
        self.entry_email = Entry(root)
        self.entry_email.grid(row=2, column=3, padx=10, pady=10)

        button_style = {'bg': 'navy', 'fg': 'white', 'padx': 10, 'pady': 5} 
        self.button_add = Button(root, text="Add Student", command=self.add_student, **button_style)
        self.button_add.grid(row=1, column=8, padx=10, pady=10)

        self.button_display = Button(root, text="Display All", command=self.display_students, **button_style)
        self.button_display.grid(row=2, column=5, padx=10, pady=10)

        self.button_search = Button(root, text="Search Student", command=self.search_student, **button_style)
        self.button_search.grid(row=2, column=8, padx=10, pady=10)

        self.button_delete = Button(root, text="Delete Student", command=self.delete_student, **button_style)
        self.button_delete.grid(row=3, column=3, padx=10, pady=10)

        self.button_update = Button(root, text="Update Student", command=self.update_student, **button_style )
        self.button_update.grid(row=3, column=5, padx=10, pady=10)

        self.button_exit = Button(root, text="Exit", command=root.quit, **button_style)
        self.button_exit.grid(row=3, column=8, padx=10, pady=10)

        self.text_area = Text(root, width=60, height=10)
        self.text_area.grid(row=5, columnspan=10, padx=10, pady=10)

    def add_student(self):
        roll_no = self.entry_roll_no.get()
        name = self.entry_name.get()
        course = self.entry_course.get()
        contact = self.entry_contact.get()
        email = self.entry_course.get()

        if roll_no and name and course and contact and email:
            student = Student(roll_no, name, course,contact, email)
            self.students.append(student)
            messagebox.showinfo("Success", "Student added successfully")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "All fields are required")

    
    def display_students(self):
        self.text_area.delete(1.0, END)
        if self.students:
            for student in self.students:
                self.text_area.insert(END, f"Roll No: {student.roll_no}, Name: {student.name}, Course: {student.course}, Mobile No: {student.contact}, Email: {student.email}\n")
        else:
            self.text_area.insert(END, "No students to display")

   
    def search_student(self):
        roll_no = self.entry_roll_no.get()
        if roll_no:
            for student in self.students:
                if student.roll_no == roll_no:
                    self.text_area.delete(1.0, END)
                    self.text_area.insert(END, f"Found: Roll No: {student.roll_no}, Name: {student.name}, Course: {student.course},  Mobile No: {student.contact}, Email: {student.email}\n")
                    return
            messagebox.showerror("Error", "Student not found")
        else:
            messagebox.showerror("Error", "Please enter Roll No to search")

  
    def delete_student(self):
        roll_no = self.entry_roll_no.get()
        if roll_no:
            for student in self.students:
                if student.roll_no == roll_no:
                    self.students.remove(student)
                    messagebox.showinfo("Success", "Student deleted successfully")
                    self.clear_entries()
                    return
            messagebox.showerror("Error", "Student not found")
        else:
            messagebox.showerror("Error", "Please enter Roll No to delete")


    def update_student(self):
        roll_no = self.entry_roll_no.get()
        name = self.entry_name.get()
        course = self.entry_course.get()
        contact= self.entry_contact.get()
        email = self.entry_email.get()

        if roll_no and name and course and contact and email:
            for student in self.students:
                if student.roll_no == roll_no:
                    student.name = name
                    student.course = course
                    student.contact = contact
                    student.email = email
                    messagebox.showinfo("Success", "Student updated successfully")
                    self.clear_entries()
                    return
            messagebox.showerror("Error", "Student not found")
        else:
            messagebox.showerror("Error", "All fields are required")

    def clear_entries(self):
        self.entry_roll_no.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_course.delete(0, END)
        self.entry_contact.delete(0, END)
        self.entry_email.delete(0, END)


if __name__ == "__main__":
    root = Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
