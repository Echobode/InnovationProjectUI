import tkinter as tk                                                                                                                          
from main_menu import MainMenu
import mariadb
import RPi.GPIO as GPIO
import mariadb 
import HardwareOperations as Hardware 
import sys

try:
	conn = mariadb.connect(
	user = "root",
	password = "1234",
	host = "127.0.0.1",
	port = 3306,
	database = "ncrinnovationproject"
	)
except mariadb.Error as e:
	print(f"Error connecting to MariaDB Platform: {e}")
	sys.exit(1)


root = tk.Tk()
root.title("Laboratory Inventory")
root.geometry("800x600")

cur = conn.cursor()

hardware_actions = Hardware.HardwareActions()
main_menu = MainMenu(root, hardware_actions, cur, conn)

root.mainloop()
hardware_actions.gpio_clean_all()
conn.close()
