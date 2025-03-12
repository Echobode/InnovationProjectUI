import customtkinter as ctk


def resize_buttons(event=None):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate button size as a percentage of screen size
    button_width = int(screen_width * 0.1)  # 10% of screen width
    button_height = int(screen_height * 0.05)  # 5% of screen height

    # Update button size
    button.configure(width=button_width, height=button_height)


# Create the main window
root = ctk.CTk()

# Create a button
button = ctk.CTkButton(root, text="Dynamic Button")
button.place(relx=0.5, rely=0.5, anchor='center')

# Bind the resize event to the resize_buttons function
root.bind('<Return>', resize_buttons)

# Run the application
root.mainloop()