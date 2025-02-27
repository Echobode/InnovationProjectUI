from tkinter import Label, Entry, Button

class ButtonManager:
    def __init__(self, root):
        self.root = root
        self.create_main_buttons()

    def create_borrow_button(self):
        self.borrow_button = Button(self.root, text='Borrow', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.br_button_conf)
        self.borrow_button.place(relx=0.5, rely=0.2, anchor="center") #use this line to change position of button

    def create_return_button(self):
        self.return_button = Button(self.root, text='Return', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.ret_button_conf)
        self.return_button.place(relx=0.5, rely=0.4, anchor="center") #use this line to change position of button

    def create_user_info_button(self):
        self.user_info_button = Button(self.root, text='User Information', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",  command=self.remove_main_buttons)
        self.user_info_button.place(relx=0.5, rely=0.6, anchor="center") #use this line to change position of button



    def create_main_buttons(self):
        self.create_borrow_button()
        self.create_return_button()
        self.create_user_info_button()

    def remove_main_buttons(self):
        self.borrow_button.place_forget()
        self.return_button.place_forget()
        self.user_info_button.place_forget()



    def main_back_button (self):
        self.back_button = Button(self.root, text='Back', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",  command=self.restore_main_buttons)
        self.back_button.place(relx=0.5, rely=0.8, anchor="center") #use this line to change position of button

    def restore_main_buttons(self):
        self.back_button.place_forget()

        for widget in self.root.winfo_children():
            widget.place_forget()

        self.create_main_buttons()


    def br_button_conf(self):
        self.borrow_button.place_forget()
        self.return_button.place_forget()
        self.user_info_button.place_forget()

        self.main_back_button()

        self.br_id_scan = Label(self.root, text='Scan your ID')
        self.br_id_scan.place(relx=0.5, rely=0.2, anchor="center")

        self.br_entry = Entry(self.root, width=30)
        self.br_entry.place(relx=0.5, rely=0.4, anchor="center")

        self.br_id_submit_button = Button(self.root, text="Submit", command=self.br_display_input)
        self.br_id_submit_button.place(relx=0.5, rely=0.5, anchor="center")

        self.br_display_label = Label(self.root, text="", font=("Arial", 14))
        self.br_display_label.place(relx=0.5, rely=0.7, anchor="center")

    def br_display_input(self):
        user_input = self.br_entry.get()
        self.br_display_label.config(text=user_input) #could scan the DB here, display is a placeholder




    def ret_button_conf(self):
        self.borrow_button.place_forget()
        self.return_button.place_forget()
        self.user_info_button.place_forget()

        self.main_back_button()

        self.ret_item_scan = Label(self.root, text='Scan the items you would like to return')
        self.ret_item_scan.place(relx=0.5, rely=0.2, anchor="center")

        self.ret_entry = Entry(self.root, width=30)
        self.ret_entry.place(relx=0.5, rely=0.4, anchor="center")

        self.ret_id_submit_button = Button(self.root, text="Submit", command=self.ret_display_input)
        self.ret_id_submit_button.place(relx=0.5, rely=0.5, anchor="center")

        self.ret_display_label = Label(self.root, text="", font=("Arial", 14))
        self.ret_display_label.place(relx=0.5, rely=0.7, anchor="center")

    def ret_display_input(self):
        user_input = self.ret_entry.get()
        self.ret_display_label.config(text=user_input) #same with this one


    #def usr_inf_button_conf (self):
    #   self.

