import tkinter as tk
from tkinter import messagebox
import random
import time

# ---- Game Settings ----
TILE_SIZE = 6  # 6x6 grid
symbols = list("🍎🍌🍇🍉🍓🍒🍍🍑🍋🥝🍈🍐💎🎵⭐💖🔥🌙⚡🎲🎯🎁🏆🍰🍪🍫🎂🎮")[: (TILE_SIZE * TILE_SIZE) // 2]
symbols *= 2
random.shuffle(symbols)

# ---- Tkinter Window ----
root = tk.Tk()
root.title("🧠 Memory Puzzle Game")
root.config(bg="#222831")

# ---- Variables ----
first = second = None
buttons = []
matches = 0
clicks = 0

# ---- Functions ----
def reveal(r, c):
    global first, second, matches, clicks

    btn = buttons[r][c]
    if btn["state"] == "disabled":
        return

    btn.config(text=btn.symbol, bg="#FFD369", state="disabled")
    clicks += 1

    if not first:
        first = btn
    elif not second:
        second = btn
        root.after(800, check_match)

def check_match():
    global first, second, matches

    if first.symbol == second.symbol:
        first.config(bg="#32CD32")
        second.config(bg="#32CD32")
        matches += 1
    else:
        first.config(text="?", bg="#393E46", state="normal")
        second.config(text="?", bg="#393E46", state="normal")

    first = second = None

    if matches == (TILE_SIZE * TILE_SIZE) // 2:
        messagebox.showinfo("Congratulations!", f"You won the game in {clicks} clicks!")

# ---- Create Buttons Grid ----
for r in range(TILE_SIZE):
    row = []
    for c in range(TILE_SIZE):
        b = tk.Button(root, text="?", width=4, height=2, font=("Arial", 18, "bold"),
                      bg="#393E46", fg="white",
                      command=lambda r=r, c=c: reveal(r, c))
        b.symbol = symbols.pop()
        b.grid(row=r, column=c, padx=5, pady=5)
        row.append(b)
    buttons.append(row)

# ---- Run ----
root.mainloop()






without comments 





ChatGPT can make mistakes. Check important info. See Cookie Preferences.
