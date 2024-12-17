from tkinter import *

class Add_Student:
    def __init__(self, student, frame, func):
        self.clear = func
        self.frame = frame
        self.student_data = student
        self.lbls = ['Name:', 'Age:', 'ID Number:', 'Email Address:', 'Phone Number:']
        self.flds = []
        self.message_label = None

    def write_student_info(self, name, age, id_num, email, phone_num):
        with open('student_data.txt', 'a') as file:
            file.write(f"{name}\t{age}\t{id_num}\t{email}\t{phone_num}\n")

    def add_student(self, name, age, id, email, phone):
        student = [name, age, id, email, phone]
        self.student_data.student_list.append(student)
        self.write_student_info(name, age, id, email, phone)

    def check_if_id_exists(self, student_id):
        for student in self.student_data.student_list:
            if student[2] == student_id:
                return True
        return False

    def display_message(self, message, color):
        if self.message_label:
            self.message_label.destroy()
        self.message_label = Label(self.frame, text=message, font=("Cascadia Code", 14), fg=color, bg="#fafad2")
        self.message_label.place(relx=0.5, rely=0.05, anchor="center")

    def register(self):
        student = []
        missing_fields = []

        for i, fld in enumerate(self.flds):
            if fld.get().strip():
                student.append(fld.get().strip())
            else:
                missing_fields.append(self.lbls[i][:-1])

        if missing_fields:
            error_text = "Missing fields: " + ", ".join(missing_fields)
            self.display_message(error_text, "red")
            return

        if self.check_if_id_exists(student[2]):
            self.display_message("Student ID already exists. Please use a different ID.", "red")
            return

        self.add_student(*student)
        for fld in self.flds:
            fld.delete(0, END)

        self.display_message("Student registered successfully!", "green")

    def register_ui(self):
        self.flds = []

        self.clear(self.frame)

        form_frame = Frame(self.frame, bg="#fafad2", padx=20, pady=20)
        form_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        for i, txt in enumerate(self.lbls):
            Label(form_frame, text=txt, font=("Cascadia Code", 16), bg="#fafad2").grid(row=i, column=0, sticky="w", padx=10, pady=5)
            fld = Entry(form_frame, font=("Cascadia Code", 14), width=30, relief="solid", borderwidth=2)
            fld.grid(row=i, column=1, padx=10, pady=5)
            self.flds.append(fld)

        Button(form_frame, text="Register", font=("Cascadia Code", 16), bg="#90ee90", relief="solid", width=20, 
               command=self.register).grid(row=len(self.lbls), column=0, columnspan=2, pady=20)
