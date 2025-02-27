import tkinter as tk
from main_menu import MainMenu

root = tk.Tk()
root.title("Laboratory Inventory")
root.geometry("800x600")


main_menu = MainMenu(root)

root.mainloop()