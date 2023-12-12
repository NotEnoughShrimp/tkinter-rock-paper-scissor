""" https://www.geeksforgeeks.org/rock-paper-scissor-game-python-project/ """
import tkinter 
from PIL import Image, ImageTk, ImageOps
import random


""" Part 2: Game Implementation"""
def game_function(player_choice):
    values = [1,2,3]
    computer_choice = random.choice(values)
    
    canvas.delete("all")  # this just cleares everything out
    
    if player_choice == 1:
        canvas.create_image(0,100, anchor=tkinter.NW, image=rock_p)
    elif player_choice == 2:
        canvas.create_image(0,100, anchor=tkinter.NW, image=paper_p)
    elif player_choice == 3:
        canvas.create_image(0,100, anchor=tkinter.NW, image=scissor_p)

    if computer_choice == 1:
        canvas.create_image(800,100, anchor=tkinter.NE, image=rock_c)
    elif computer_choice == 2:
        canvas.create_image(800,100, anchor=tkinter.NE, image=paper_c)
    elif computer_choice == 3:
        canvas.create_image(800,100, anchor=tkinter.NE, image=scissor_c)

root = tkinter.Tk()  # initializes tkinter
root.title("Rock Paper Scissors")  # sets what appears on window
root.geometry("800x680")  # sets window dimensions
canvas = tkinter.Canvas(root, width=800, height=680)
canvas.pack()

""" labels for the gui"""
player_label = tkinter.Label(root, text="Player", font=("Algerian",25))
computer_label = tkinter.Label(root, text="Computer", font=("Algerian",25))
versus_label = tkinter.Label(root, text="VS", font=("Algerian", 40))

""" placing the labels"""
player_label.place(x=80,y=20)
computer_label.place(x=560,y=20)
versus_label.place(x=370,y=230)

""" default image"""
default_image = Image.open('default.jpeg')
resized_image = default_image.resize((300,300))
flipped_image = ImageOps.mirror(resized_image)

img_p = ImageTk.PhotoImage(resized_image)
img_c = ImageTk.PhotoImage(flipped_image)

canvas.create_image(0,100, anchor=tkinter.NW, image=img_p)  # These 2 just put the initial default image up at the start.
canvas.create_image(800,100,anchor=tkinter.NE, image=img_c)

""" rock image"""
rock_image = Image.open('rock.jpeg')
rock_resized_image = rock_image.resize((300,300))
rock_flipped_image = ImageOps.mirror(rock_resized_image)

rock_p = ImageTk.PhotoImage(rock_resized_image)
rock_c = ImageTk.PhotoImage(rock_flipped_image)

""" paper image"""
paper_image = Image.open('paper.jpeg')
paper_resized_image = paper_image.resize((300,300))
paper_flipped_image = ImageOps.mirror(paper_resized_image)

paper_p = ImageTk.PhotoImage(paper_resized_image)
paper_c = ImageTk.PhotoImage(paper_flipped_image)

""" scissor image"""
scissor_image = Image.open('scissor.jpeg')
scissor_resized_image = scissor_image.resize((300,300))
scissor_flipped_image = ImageOps.mirror(scissor_resized_image)

scissor_p = ImageTk.PhotoImage(scissor_resized_image)
scissor_c = ImageTk.PhotoImage(scissor_flipped_image)


""" selection image"""
selection_image = Image.open('rps.jpg')
resized_selection = selection_image.resize((300,130))
selection = ImageTk.PhotoImage(resized_selection)
canvas.create_image(400,500, anchor=tkinter.CENTER, image=selection)


# Without Lambda it just runs the function and draws the image. WITH lambda, it waits for the click
rock_button = tkinter.Button(root, text="Rock", command=lambda:game_function(1))
paper_button = tkinter.Button(root, text="Paper", command=lambda:game_function(2))
scissor_button = tkinter.Button(root, text="Scissor", command=lambda:game_function(3))

rock_button.place(x=100, y=340)
paper_button.place(x=400, y=340)
scissor_button.place(x=700, y=340)

# """ Part 2: Game Implementation"""
# def game_function(player_choice):
#     values = [1,2,3]
#     computer_choice = random.choice(values)
#     player_choice = int(input("enter rock[1], paper[2], scissors[3]: "))
#     if player_choice == 1 and computer_choice == 2:
#         canvas.create_image(0,100, anchor=tkinter.NW, image=rock_p)
#         canvas.create_image(800,100, anchor=tkinter.NE, image=paper_c)
#     elif player_choice == 2 and computer_choice == 3:
#         canvas.create_image(0,100, anchor=tkinter.NW, image=paper_p)
#         canvas.create_image(800,100, anchor=tkinter.NE, image=scissor_c)
#     elif player_choice == 3 and computer_choice == 1:
#         canvas.create_image(0,100, anchor=tkinter.NW, image=scissor_p)
#         canvas.create_image(800,100, anchor=tkinter.NE, image=rock_c)


root.mainloop()

#canvas.create_image(0,100, anchor=tkinter.NW, image=paper_p)
#canvas.create_image(800,100, anchor=tkinter.NE, image=paper_c)

