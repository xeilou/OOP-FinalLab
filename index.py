from student import Student_Info
from search_student import Search_Student
from view_all import View_All_Students
from add_student import Add_Student
from main_menu import Main_Menu
from login import Login
from tkinter import *

win = Tk()
win.geometry(f"1280x800+{(win.winfo_screenwidth() - 1280)//2}+{(win.winfo_screenheight() - 800)//2}")
win.title("Student Information System")

def clear(frame): 
    for widget in frame.winfo_children():
        widget.destroy()

main = Main_Menu(win)
stu = Student_Info()
addstud = Add_Student(stu, main.content_contain, clear)
search = Search_Student(stu.student_list, clear, main.content_contain)
view = View_All_Students(stu.student_list, main.content_contain, clear)
login = Login(win, search.student_exists, main.main_screen)

stu.read_student_info()

def view_profile():
    clear(main.content_contain)
    search.profile_ui(login.stu_id.get())

def search_student():
    clear(main.content_contain)
    search.search_student()

def view_all():
    clear(main.content_contain)
    view.show_list()

def add_student():
    clear(main.content_contain)
    addstud.register_ui()

def logout():
    clear(main.content_contain)
    login.strikes = 4
    login.strikes_lbl.config(text="Invalid Student ID. You have 4 attempt/s remaining.",
                             font=("Cascadia Code", 14), bg="#fafad2", fg="#fafad2")
    login.stu_id.delete(0, END)
    main.menu_contain.pack_forget()
    main.content_contain.pack_forget()
    login.login()

main.funcs.extend([view_profile, search_student, view_all, add_student, logout])

main.make_btns()

login.login()

win.mainloop()
