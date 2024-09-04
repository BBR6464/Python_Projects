from tkinter import *
import pandas as pd
from random import choice
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words = {}

# ---------------------------- RANDOM WORD FUNCTION ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel the previous timer
    current_card = choice(words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_image, image=card_back)

def is_known():
    words.remove(current_card)
    pd.DataFrame(words).to_csv('data/words_to_learn.csv', index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Load data
if os.path.exists('data/words_to_learn.csv'):
    data = pd.read_csv('data/words_to_learn.csv')
else:
    data = pd.read_csv('data/french_words.csv')
words = data.to_dict(orient='records')

# Canvas setup
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 68, "bold"))

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

# Initial card display and flip timer
flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()