from tkinter import *
import tkinter.messagebox

class Login:
    def __init__(self, win, func, frame):
        self.func = func
        self.win = win
        self.frame = frame
        self.login_fr = Frame(win, bg="#fafad2", padx=20, pady=20, relief="solid", borderwidth=2)
        self.login_lbl = Label(self.login_fr, text="Welcome! Login to Continue.", font=("Cascadia Code", 20), bg="#fafad2")
        self.id = id
        self.stu_id = Entry(self.login_fr, font=("Cascadia Code", 14), width=30, relief="solid", borderwidth=2)
        self.login_btn = Button(self.login_fr, text="Login", command=self.login_check, font=("Cascadia Code", 16), bg="#90ee90", relief="solid")
        self.strikes_lbl = Label(self.login_fr, text="Invalid Student ID. You have 4 attempt/s remaining.", font=("Cascadia Code", 14), bg="#fafad2", fg="#fafad2")
        self.strikes = 4

    def login_check(self):
        if self.func(self.stu_id.get()):
            self.frame(self.login_fr)
        else:
            self.strikes -= 1
            self.strikes_lbl.config(text=f"Invalid Student ID. You have {self.strikes} attempt/s remaining.", fg='red')
        if self.strikes == 0:
            self.info_win()
            self.win.destroy()

    def login(self):
        self.login_fr.pack(padx=20, pady=20, expand=True)
        self.login_lbl.pack(pady=10)
        self.stu_id.pack(pady=10)
        self.login_btn.pack(pady=5)
        self.strikes_lbl.pack(pady=10)

    def info_win(self): 
        tkinter.messagebox.showerror("Oh no!",  "You have exceeded the allowed number of attempts to provide a valid student ID.\n\nThe program will shut down now.") 
    