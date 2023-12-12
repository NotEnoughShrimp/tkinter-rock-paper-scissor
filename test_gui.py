import random
from tkinter import Tk, Button, Label
import time


def button_click():
    x = random.randint(1, 10)
    if x == 5:
        countdown(5)
    else:
        label.config(text=f"{x}")

def countdown(seconds):
    label.config(text=f"Uh oh, {seconds} seconds left")
    if seconds > 0:
        window.after(1000, countdown, seconds - 1)  # Schedule the next countdown after 1000 milliseconds (1 second)
    else:
        label.config(text="Yeah that's about it")


window = Tk()
window.title("Hello")

window.configure(bg="blue")
window.minsize(640,360)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.maxsize(screen_width,screen_height)
window_x = (screen_width - 720) // 2  # window_x & window_y are referenced in geometry for default window.
window_y = (screen_height - 480) // 2

window.geometry(f"720x480+{window_x}+{window_y}")  # Set the window position; string is desired initial window size.

# Create a button and associate it with the button_click function
button = Button(window, text="Click me", command=button_click, width=10, font=("courier", 15))
button.pack(pady=10)

# create a label to display
label = Label(window, text="Welcome", width=20)
label.pack(side="bottom", padx=10, pady=10)



window.mainloop()

