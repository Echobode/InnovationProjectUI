from tkinter import *

class BorrowSection:
    def __init__(self, root, main_menu_class, main_back_button):
        self.root = root
        self.main_menu_class = main_menu_class
        self.main_back_button= main_back_button


        #first part buttons and labels
        self.borrow_scan_id = Label(self.root, text='Scan your ID')
        self.borrow_scan_entry = Entry(self.root, width=30)
        self.borrow_scan_next = Button(self.root, text='Submit', font=("Arial", 12, "bold"), bg="#4CAF50",fg="white", command=self.show_borrow_menu)

        #second part main function
        self.borrow_items = Label(self.root, text='Scan the items you want to borrow')
        self.borrow_entry = Entry(self.root, width=30)
        self.borrow_submit = Button(self.root, text='Submit', font=("Arial", 12, "bold"), bg="#4CAF50",fg="white", command=self.borrow_add_entry)
        self.borrow_continue = Button(self.root, text='Continue', font=("Arial", 12, "bold"), bg="#4CAF50",fg="white", command=self.borrow_end)
        self.borrow_text = Listbox(self.root, width=40, height=10)

        #End part
        self.borrow_end_text = Label(self.root, text='Thank you!, Please return the items soon')


        self.borrow_entry.bind('<Return>', self.borrow_add_entry)

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

    def clear_borrow_entry(self):
        self.borrow_text.delete(0, END)
        self.borrow_scan_entry.delete(0, 'end')
        self.borrow_entry.delete(0, 'end')

    def borrow_end(self):
        self.borrow_items.place_forget()
        self.borrow_entry.place_forget()
        self.borrow_submit.place_forget()
        self.borrow_text.place_forget()
        self.borrow_continue.place_forget()

        self.borrow_end_text.place(relx=0.5, rely=0.4, anchor='center')



