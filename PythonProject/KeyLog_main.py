from customtkinter import *

from main_menu import MainMenu

root = CTk()
root.title("Laboratory Inventory")
root.geometry("640x480")


set_appearance_mode("light")


main_menu = MainMenu(root)


root.mainloop()