from tkinter import *

class MainMenu:
    def __init__(self, root):
        self.root = root

        #main buttons
        self.borrow_button = Button(self.root, text='Borrow', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command=self.borrow_pressed)
        self.return_button = Button(self.root, text='Return', font=("Arial", 12, "bold"), bg="#4CAF50",fg="white", command=self.return_pressed)
        self.user_info_button = Button(self.root, text='User Information', font=("Arial", 12, "bold"), bg="#4CAF50",fg="white", command=self.user_info_pressed)



        #back buttons
        self.main_back = Button(self.root, text='Back', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command=self.go_to_main)
        self.borrow_back = Button(self.root, text='Back', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command=self.remove_back_buttons)
        self.return_back = Button(self.root, text='Back', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command=self.remove_back_buttons)
        self.user_info_back = Button(self.root, text='Back', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command=self.remove_back_buttons)



        #borrow_buttons
        # first part buttons and labels
        self.borrow_scan_id = Label(self.root, text='Scan your ID')
        self.borrow_scan_entry = Entry(self.root, width=30)
        self.borrow_scan_next = Button(self.root, text='Submit', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command=self.show_borrow_menu)

        # second part main function
        self.borrow_items = Label(self.root, text='Scan the items you want to borrow')
        self.borrow_entry = Entry(self.root, width=30)
        self.borrow_submit = Button(self.root, text='Submit', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command=self.borrow_add_entry)
        self.borrow_continue = Button(self.root, text='Continue', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command=self.borrow_end)
        self.borrow_text = Listbox(self.root, width=40, height=10)

        # End part
        self.borrow_end_text = Label(self.root, text='Thank you!, Please return the items soon')

        self.borrow_entry.bind('<Return>', self.borrow_add_entry)



        #return_buttons
        #first part
        self.return_scan_id = Label(self.root, text='Scan your ID')
        self.return_scan_entry = Entry(self.root, width=30)
        self.return_scan_next = Button(self.root, text='Submit', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command=self.show_return_menu)

        # second part main function
        self.return_items = Label(self.root, text='Return these items')
        self.return_list = Listbox(self.root, width=40, height=10)
        self.return_continue = Button(self.root, text='Continue', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command=self.return_end)

        # End part
        self.return_end_text = Label(self.root, text='Thank you for returning the items!')



        #User Info Buttons
        #first part
        self.user_info_main = Label(self.root, text = 'NCR KeyTool Logging User Information')
        self.user_info_search = Button(self.root, text='Search', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.show_user_info_search_menu)
        self.user_info_register = Button(self.root, text='Register', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",command=self.show_user_info_register_menu)

        #search part
        self.user_info_search_label = Label(self.root, text='Enter your QLID or RFID')
        self.user_info_search_entry = Entry(self.root, width=30)
        self.user_info_search_submit = Button(self.root, text='Submit', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.show_user_info_credentials)

        self.user_info_search_query = Label(self.root, text=f'Name: {"Name"}\n QLID: {"QLID"}\n RFID: {"RFID"}\n Status: {"Status"}')
        self.user_info_toggle_status = Button(self.root, text='Toggle Status', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")#command=add command here

        #register part
        self.user_info_register_label = Label(self.root, text='Register your details below')

        self.user_info_register_first_name_label=Label(self.root,text='First Name:')
        self.user_info_register_first_name_entry = Entry(self.root, width=30)

        self.user_info_register_last_name_label= Label(self.root, text='Last Name: ')
        self.user_info_register_last_name_entry = Entry(self.root, width=30)

        self.user_info_register_qlid_label = Label(self.root, text='Enter your QLID')
        self.user_info_register_qlid_entry = Entry(self.root, width=30)

        self.user_info_register_rfid_label = Label(self.root, text='Enter your RFID')
        self.user_info_register_rfid_entry = Entry(self.root, width=30)

        self.user_info_register_submit_label = Label(self.root, text='User registered!')
        self.user_info_register_submit = Button(self.root, text='Submit', font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.user_registered_end)



        #UI Start program
        self.show_main_buttons()




    #Main menu functions
    def show_main_buttons(self):
        self.show_borrow_button()
        self.show_return_button()
        self.show_user_info_button()

    ##still needs edit
    def borrow_pressed(self):
        for widget in self.root.winfo_children():
            widget.place_forget()

            self.show_main_back()
            self.show_borrow_id_menu()

    def return_pressed(self):
        for widget in self.root.winfo_children():
            widget.place_forget()

            self.show_main_back()
            self.show_return_id_menu()

    def user_info_pressed(self):
        for widget in self.root.winfo_children():
            widget.place_forget()

            self.show_main_back()
            self.show_user_info_menu()

    def show_borrow_button(self):
        self.borrow_button.place(relx=0.5, rely=0.2, anchor="center")  # use this line to change position of button

    def show_return_button(self):
        self.return_button.place(relx=0.5, rely=0.4, anchor="center")  # use this line to change position of button

    def show_user_info_button(self):
        self.user_info_button.place(relx=0.5, rely=0.6, anchor="center")  # use this line to change position of button

    #End of Main menu Functions




    #Back Button functions
    def show_main_back (self):
        self.main_back.place(relx=0.5, rely=0.8, anchor="center") #use this line to change position of button

    def go_to_main(self):
        self.main_back.place_forget()

        for widget in self.root.winfo_children():
            widget.place_forget()

        self.clear_all_entry()

        self.show_main_buttons()

    def remove_back_buttons(self):
        self.main_back.place_forget()
        self.borrow_back.place_forget()
        self.return_back.place_forget()
        self.user_info_back.place_forget()
    #End of Back Button Functions




    #Borrow Section
    def show_borrow_id_menu(self):
        self.borrow_scan_id.place(relx=0.5, rely=0.2, anchor= 'center')
        self.borrow_scan_entry.place (relx=0.5, rely=0.4, anchor= 'center')
        self.borrow_scan_next.place(relx=0.5, rely=0.6, anchor= 'center')

    def show_borrow_menu(self): # use this command to change position of buttons
        self.borrow_scan_next.place_forget()
        self.borrow_scan_entry.place_forget()
        self.borrow_scan_id.place_forget()

        self.borrow_items.place(relx=0.2, rely=0.2, anchor="center")
        self.borrow_entry.place(relx=0.2, rely=0.4, anchor="center")
        self.borrow_submit.place(relx=0.2, rely=0.6, anchor="center")
        self.borrow_text.place(relx=0.7, rely=0.4, anchor="center")
        self.borrow_continue.place(relx=0.7, rely=0.6, anchor='w')

    def borrow_add_entry(self, event=None):
        entry_text = self.borrow_entry.get()
        self.borrow_text.insert('end', entry_text + '\n')
        self.borrow_entry.delete(0,'end')

    def clear_all_entry(self):
        self.borrow_text.delete(0, END)
        self.borrow_scan_entry.delete(0, 'end')
        self.borrow_entry.delete(0, 'end')

        self.return_scan_entry.delete(0, 'end')

        self.user_info_search_entry.delete(0, 'end')
        self.user_info_register_first_name_entry.delete(0, 'end')
        self.user_info_register_last_name_entry.delete(0, 'end')
        self.user_info_register_qlid_entry.delete(0, 'end')
        self.user_info_register_rfid_entry.delete(0, 'end')

    def borrow_end(self):
        self.borrow_items.place_forget()
        self.borrow_entry.place_forget()
        self.borrow_submit.place_forget()
        self.borrow_text.place_forget()
        self.borrow_continue.place_forget()

        self.borrow_end_text.place(relx=0.5, rely=0.4, anchor='center')
    #End of Borrow Section




    #Retun Section
    def show_return_id_menu(self):
        self.return_scan_id.place(relx=0.5, rely=0.2, anchor='center')
        self.return_scan_entry.place(relx=0.5, rely=0.4, anchor='center')
        self.return_scan_next.place(relx=0.5, rely=0.6, anchor='center')

    def show_return_menu(self):
        self.return_scan_id.place_forget()
        self.return_scan_entry.place_forget()
        self.return_scan_next.place_forget()

        self.return_items.place(relx=0.5, rely=0.2, anchor='center')
        self.return_list.place(relx=0.5, rely=0.4, anchor='center')
        self.return_continue.place(relx=0.5, rely=0.6, anchor='center')

    def return_end(self):
        self.return_list.place_forget()
        self.return_items.place_forget()
        self.return_continue.place_forget()

        self.return_end_text.place(relx=0.5, rely=0.4, anchor='center')
    #End of Return Section




    #User Information Section

    def show_user_info_menu(self):
        self.user_info_main.place(relx=0.5, rely=0.2, anchor='center')
        self.user_info_search.place(relx=0.5, rely=0.4, anchor='center')
        self.user_info_register.place(relx=0.5, rely=0.6, anchor='center')

    def show_user_info_search_menu(self):
        self.user_info_main.place_forget()
        self.user_info_search.place_forget()
        self.user_info_register.place_forget()

        self.user_info_search_label.place(relx=0.5, rely=0.2, anchor='center')
        self.user_info_search_entry.place(relx=0.5, rely=0.4, anchor='center')
        self.user_info_search_submit.place(relx=0.5, rely=0.6, anchor='center')



    def show_user_info_credentials(self):
        self.user_info_search_label.place_forget()
        self.user_info_search_entry.place_forget()
        self.user_info_search_submit.place_forget()

        self.user_info_search_query.place(relx=0.5, rely=0.2, anchor='center')
        self.user_info_toggle_status.place(relx=0.5, rely=0.4, anchor='center')
    def show_user_info_register_menu(self):
        self.user_info_main.place_forget()
        self.user_info_search.place_forget()
        self.user_info_register.place_forget()

        self.user_info_register_label.place(relx=0.5, rely=0.2, anchor='center')
        self.user_info_register_first_name_label.place(relx=0.5, rely=0.3, anchor='center')
        self.user_info_register_first_name_entry.place(relx=0.5, rely=0.34, anchor='center')

        self.user_info_register_label.place(relx=0.5, rely=0.2, anchor='center')
        self.user_info_register_last_name_label.place(relx=0.5, rely=0.4, anchor='center')
        self.user_info_register_last_name_entry.place(relx=0.5, rely=0.44, anchor='center')

        self.user_info_register_qlid_label.place(relx=0.5, rely=0.5, anchor='center')
        self.user_info_register_qlid_entry.place(relx=0.5, rely=0.54, anchor='center')

        self.user_info_register_rfid_label.place(relx=0.5, rely=0.6, anchor='center')
        self.user_info_register_rfid_entry.place(relx=0.5, rely=0.64, anchor='center')

        self.user_info_register_submit.place(relx=0.5, rely=0.7, anchor= 'center')

    def user_registered_end(self):
        self.user_info_register_label.place_forget()
        self.user_info_register_first_name_label.place_forget()
        self.user_info_register_first_name_entry.place_forget()

        self.user_info_register_label.place_forget()
        self.user_info_register_last_name_label.place_forget()
        self.user_info_register_last_name_entry.place_forget()

        self.user_info_register_qlid_label.place_forget()
        self.user_info_register_qlid_entry.place_forget()

        self.user_info_register_rfid_label.place_forget()
        self.user_info_register_rfid_entry.place_forget()

        self.user_info_register_submit.place_forget()

        self.user_info_register_submit_label.place(relx=0.5, rely=0.3, anchor='center')







