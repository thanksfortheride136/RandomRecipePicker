import tkinter as tk
from PIL import ImageTk #needed to display images on tkinter
import sqlite3 #imports sqlite database



# initiallize app
root = tk.Tk() #inits a tk object and enables a tk screen.
root.title("Recipe Picker")  #titles the window
root.eval("tk::PlaceWindow . center") #places the window in center screen
bg_color = '#3d6466'

def fetch_db():
    connection = sqlite3.connect("data/recipes.db")

def load_frame1():
    frame1.pack_propagate(False) #need this to get bg color back and center i think?

    ##### Frame 1 Widgets #####
    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")   #saves image file to variable
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)                  #specifies where you want image file on frames and what image to use. need a bg attribute for the image to work
    logo_widget.image = logo_img #needed to just use the image, weird quick of tkinter
    logo_widget.pack()  #calls pack method to display image

    ##### Frame 1 text, specifies things like universal fonts, colors etc. #####
    tk.Label(frame1, 
            text="Ready for your random recipe?",
            bg=bg_color,
            fg="white",
            font=("TkMenuFont", 14)
            ).pack(pady=20) #adjusts padding

    ##### Frame 1 button widget #####
    tk.Button(frame1,           #lots of button parameters here
            text="shuffle", 
            font=("TkHeadingFont", 20), 
            bg="#28393a", fg="white", 
            cursor="hand2", 
            activebackground="#badee2",
            activeforeground="black",
            command=lambda:load_frame2()).pack(pady=20)  #lambda is very important, it makes the button execute the custom function after this lambda function.

frame1 = tk.Frame(root, width=500, height=600, bg=bg_color) #sets length and width of screen of FRAME 1, asigns to a variable that used in the .grid method below.
frame2 = tk.Frame(root, bg=bg_color) #frame 2

for frame in (frame1, frame2): #resizes frame iterated over these tuples
    frame.grid(row=0, column=0)

def load_frame2():
    print("hello")

load_frame1()

# run app
root.mainloop()