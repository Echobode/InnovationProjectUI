from tkinter import *

class BackButton:
    def __init__(self, root, main_menu_class, borrow_section, return_section):
        self.root = root
        self.main_menu_class = main_menu_class
        self.borrow_section = borrow_section
        self.return_section = return_section

        self.main_back = Button(self.root, text='Back', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command= self.go_to_main)
        self.borrow_back = Button(self.root, text='Back', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command= self.remove_back_buttons)
        self.return_back = Button(self.root, text='Back', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command= self.remove_back_buttons)
        self.user_info_back = Button(self.root, text='Back', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command= self.remove_back_buttons)

    def show_main_back (self):
        self.main_back.place(relx=0.5, rely=0.8, anchor="center") #use this line to change position of button

    def go_to_main(self):
        self.main_back.place_forget()

        for widget in self.root.winfo_children():
            widget.place_forget()

        self.borrow_section.clear_borrow_entry()

        self.main_menu_class(self.root, self, self.borrow_section, self.return_section)

    def remove_back_buttons(self):
        self.main_back.place_forget()
        self.borrow_back.place_forget()
        self.return_back.place_forget()
        self.user_info_back.place_forget()














