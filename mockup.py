import tkinter as tk
import random
from PIL import Image, ImageTk

def player_choice():
    # Get the player's choice from the entry field
    choice = entry.get().lower()
    if choice in choices:
        print(f"Player chose: {choice}")
        computer_choice()
    else:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def computer_choice():
    # Randomly select the computer's choice
    computer_pick = random.choice(choices)
    print(f"Computer chose: {computer_pick}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Load images
rock_image = ImageTk.PhotoImage(Image.open('rock.jpeg').resize((300,300)))
paper_image = ImageTk.PhotoImage(Image.open('paper.jpeg').resize((300,300)))
scissors_image = ImageTk.PhotoImage(Image.open('scissor.jpeg').resize((300,300)))

# Create buttons with images
rock_button = tk.Button(root, image=rock_image, command=lambda: player_choice('rock'))
paper_button = tk.Button(root, image=paper_image, command=lambda: player_choice('paper'))
scissors_button = tk.Button(root, image=scissors_image, command=lambda: player_choice('scissors'))

# Grid layout for buttons
rock_button.grid(row=0, column=0, padx=10)
paper_button.grid(row=0, column=1, padx=10)
scissors_button.grid(row=0, column=2, padx=10)

# Entry field for player's choice
entry = tk.Entry(root, width=20)
entry.grid(row=1, columnspan=3, pady=10)

# List of valid choices
choices = ['rock', 'paper', 'scissors']

# Start the Tkinter event loop
root.mainloop()
