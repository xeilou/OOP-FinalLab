from student import Student_Info
from add_student import Add_Student
from tkinter import *
from functools import partial


stu = Student_Info()
addstud = Add_Student(stu)
stu.read_student_info()

#print(stu.show_list())
#print(stu.student_profile("2067-6-19275"))

win = Tk()
win.geometry(f"1280x800+{(win.winfo_screenwidth() - 1280)//2}+{(win.winfo_screenheight() - 800)//2}")

btns = []

def login_check():
    user_id = id_field.get()
    user_pass = pass_field.get()

    if stu.student_exists(user_id):
        if user_pass == "123":
            main()

login_fr = Frame(win)
login_lbl = Label(login_fr, text="Login to continue")
id_field = Entry(login_fr)
pass_field = Entry(login_fr)
submit_btn = Button(login_fr, text="Login", command=partial(login_check))

def login():
    menu_contain.pack_forget()
    content_contain.pack_forget()

    login_fr.pack(expand=True)
    login_lbl.pack()
    id_field.pack()
    pass_field.pack()
    submit_btn.pack()

def search_for(student_id):
    clean()
    if stu.student_exists(student_id):
        Label(content_contain, text=f"{stu.student_profile(student_id)}").pack()
    else:
        Label(content_contain, text="Student does not exist").pack()

def search_student():
    clean()
    id_entry = Entry(content_contain)
    id_entry.pack()
    Button(content_contain, text="Search", command=lambda: search_for(id_entry.get())).pack()

def add_student(name, age, id, email, phone):
    clean()
    addstud.add_student(name, age, id, email, phone)

def register():
    clean()    
    name = Entry(content_contain)
    age = Entry(content_contain)
    id = Entry(content_contain)
    email = Entry(content_contain)
    phone = Entry(content_contain)
    name.pack()
    age.pack()
    id.pack()
    email.pack()
    phone.pack()
    Button(content_contain, text="Enter", command=lambda: add_student(name.get(), age.get(), id.get(), email.get(), phone.get())).pack()

def func1():
    clean()
    Label(content_contain, text=f"{stu.student_profile(id_field.get())}").pack()

def func2():
    clean()
    search_student()

def func3():
    clean()
    Label(content_contain, text=f"{stu.show_list()}").pack()

def func4():
    clean()
    register()

def func5():
    id_field.delete(0, END)
    pass_field.delete(0, END)
    clean()
    login()

btn_txt = ["View Profile", "View Others' Profiles", "View All Student Profiles", "Add New Student", "Logout"]
func = [func1, func2, func3, func4, func5]

menu_contain = Frame(win, borderwidth = 1, bg = "black", relief = "sunken")
menu_lbl = Label(menu_contain, text = "Main Menu", font = ("Century Gothic", 20), fg = "white", bg = "black", padx = 20)
content_contain = Frame(win)

for i, txt in enumerate(btn_txt):
    btns.append(Button(menu_contain, anchor = "w", width = 20, text = btn_txt[i], font=("Century Gothic", 14), padx=10, pady=15, bg="#FFFFFF"))
for i in range(len(btns)):
    btns[i].config(command=partial(func[i]))

def clean(): 
    for widget in content_contain.winfo_children():
        widget.destroy()

def main():
    login_fr.pack_forget()

    menu_contain.pack(side = "left", fill = "y")
    menu_lbl.pack()
    content_contain.pack(expand=True)
    for i in range(len(btns)):
        btns[i].pack()
    Label(content_contain, text="Welcome, Student!", font=("Century Gothic", 35)).pack(expand=True)
    Label(content_contain, text="This is your central hub for student information management", font=("Century Gothic", 15)).pack(expand=True)

login()
win.mainloop()