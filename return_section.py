from tkinter import *

class ReturnSection:
    def __init__(self, root, main_menu_class, main_back_button):
        self.root = root
        self.main_menu_class = main_menu_class
        self.main_back_button = main_back_button

         #first part buttons and labels
        self.return_scan_id = Label(self.root, text= 'Scan your ID')
        self.return_scan_entry = Entry(self.root, width=30)
        self.return_scan_next = Button(self.root, text='Submit', font=("Arial", 12, "bold"), bg="#4CAF50",fg="white", command=self.show_return_menu)

        #second part main function
        self.return_items = Label(self.root, text='Return these items')
        self.return_list = Listbox(self.root, width=40, height=10)
        self.return_continue = Button(self.root, text='Continue', font=("Arial", 12, "bold"), bg="#4CAF50",fg="white", command=self.return_end)

        #End part
        self.return_end_text = Label(self.root, text='Thank you for returning the items!')

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


