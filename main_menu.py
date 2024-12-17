from tkinter import *
from functools import partial

class Main_Menu:
    def __init__(self, window):
        self.win = window

        self.menu_contain = Frame(self.win, bg="#90ee90", borderwidth=2, relief='solid')
        self.menu_lbl = Label(self.menu_contain, text="Main Menu", font=("Cascadia Code", 20), 
                              bg="#90ee90", pady=20, padx=40)
        self.btns = []
        self.btn_txt = ["View Profile", "View Others' Profiles", "View All Profiles", "Register Student", "Logout"]
        self.funcs = []

        self.content_contain = Frame(self.win, bg="#fafad2", borderwidth=2, relief='solid')

    def make_btns(self):
        for i, txt in enumerate(self.btn_txt):
            if txt == "Logout":
                btn = Button(self.menu_contain, anchor="w", width=25, text=f">> {txt}", 
                    font=("Cascadia Code", 14), padx=10, pady=15, bg="#90ee90", fg="red", relief='solid')
            else:
                btn = Button(
                    self.menu_contain, anchor="w", width=25, text=f">> {txt}", 
                    font=("Cascadia Code", 14), padx=10, pady=15, bg="#90ee90", relief='solid')
            
            btn.config(command=partial(self.funcs[i]))
            self.btns.append(btn)


    def main_screen(self, frame):
        frame.pack_forget()
        welcome_fr = Frame(self.content_contain, bg='#fafad2')
        self.menu_contain.pack(side=LEFT, anchor='w', fill=Y)
        self.menu_lbl.pack()
        for btn in self.btns:
            btn.pack(fill=X, padx=15, pady=5)
        self.content_contain.pack(expand=True, side=LEFT, anchor='w', fill=BOTH)
        welcome_fr.pack(expand=True)
        Label(welcome_fr, text="Welcome to Your Central Hub for\n Student information Management!",
              font=("Cascadia Code", 18), bg="#fafad2").pack(anchor='center')
        Label(welcome_fr, text="Begin exploring by clicking a button on the side bar.",
              font=("Cascadia Code", 10), bg="#fafad2").pack(anchor='center', pady=15)