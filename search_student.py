from tkinter import *
from functools import partial

class Search_Student:
    def __init__(self, student_list, clear, frame):
        self.frame = frame
        self.student_list = student_list
        self.clear = clear
    
    def student_profile(self, id):    
        for student in self.student_list:
            if student[2] == id:
                return f"\n{'Name:':<15}\t{student[0]}\n{'Age:':<15}\t{student[1]}\n{'ID Number:':<15}\t{student[2]}\n{'Email Address:':<15}\t{student[3]}\n{'Phone Number:':<15}\t{student[4]}"
        return f"Student with ID {id} not found."

    def student_exists(self, id):
        for student in self.student_list:
            if student[2] == id:
                return True
        return False
    
    def search_for(self, frame, student_id):
        
        self.clear(self.frame)

        profile_fr = Frame(self.frame, bg="#fafad2")
        profile_fr.pack(expand=True)

        btn = Button(profile_fr, text="", command=self.search_student,
                font=('Cascadia Code', 14), relief='solid', bg='#90ee90')

        if self.student_exists(student_id):
            Label(profile_fr, text="Associated Student Profile:", font=("Cascadia Code", 18), bg="#fafad2").pack(pady=5)
            Label(profile_fr, text=f"{self.student_profile(student_id)}", font=("Cascadia Code", 14), justify=LEFT, bg="#fafad2").pack(pady=10)

        elif student_id == "":
            Label(profile_fr, text="Please Input a Student ID", font=("Cascadia Code", 20), fg="red", bg="#fafad2").pack(pady=10)
            btn.config(text="Try Again")
            btn.pack(pady=20)
            
        else:
            Label(profile_fr, text="Student does not exist", font=("Cascadia Code", 20), fg="red", bg="#fafad2").pack(pady=10)
            btn.config(text="Try Again")
            btn.pack(pady=20)
    def search_handler(self, frame, entry):
        self.search_for(frame, entry.get())

    def search_student(self):

        self.clear(self.frame)

        search_fr = Frame(self.frame, bg="#fafad2")
        search_fr.pack(expand=True)

        Label(search_fr, text="Enter Student ID to Search:", font=("Cascadia Code", 20), bg='#fafad2').pack(pady=10)

        id_entry = Entry(search_fr, width=25, font=("Cascadia Code", 15), relief='solid', borderwidth=2)
        id_entry.pack(pady=5)

        Button(search_fr, text="Search", command=partial(self.search_handler, search_fr, id_entry),
            font=('Cascadia Code', 14), relief='solid', bg='#90ee90').pack(pady=10)
    
    def profile_ui(self, id):
        self.clear(self.frame)

        profile_fr = Frame(self.frame, bg="#fafad2")
        profile_fr.pack(expand=True)

        Label(profile_fr, text="Your Student Profile:", font=("Cascadia Code", 18), bg="#fafad2").pack(pady=10, padx=20)
        Label(profile_fr, text=f"{self.student_profile(id)}", font=("Cascadia Code", 14), justify=LEFT,  bg="#fafad2").pack()
