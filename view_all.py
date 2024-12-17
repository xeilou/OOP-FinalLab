from tkinter import *

class View_All_Students:
    def __init__(self, student_list, frame, func):
        self.student_list = student_list
        self.frame = frame
        self.clear = func
    
    def show_list(self):        
        v = Scrollbar(self.frame, orient='vertical')
        v.pack(side=RIGHT, fill=Y)
        
        t = Text(self.frame, width=50, height=15, wrap=NONE, yscrollcommand=v.set, bg="#fafad2", relief="flat",
                 font=("Cascadia Code", 14))
        
        for student in self.student_list:
            t.insert(END, f"\n{'Name:'.ljust(15)} {student[0]}\n")
            t.insert(END, f"{'Age:'.ljust(15)} {student[1]}\n")
            t.insert(END, f"{'ID Number:'.ljust(15)} {student[2]}\n")
            t.insert(END, f"{'Email Address:'.ljust(15)} {student[3]}\n")
            t.insert(END, f"{'Phone Number:'.ljust(15)} {student[4]}\n")
            t.insert(END, "___________________________________________________\n")
        
        t.pack(side=LEFT, fill=Y, expand=True)
        v.config(command=t.yview)
