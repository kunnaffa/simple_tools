import tkinter as tk
import subprocess

# Create the root window
root = tk.Tk()
root.title("Language Switcher")

# Function to switch to Hebrew language
def switch_to_hebrew():
    subprocess.run(['setxkbmap', 'il'])

# Function to switch to English language
def switch_to_english():
    subprocess.run(['setxkbmap', 'us'])

# Function to switch to Arabic language
def switch_to_arabic():
    subprocess.run(['setxkbmap', 'ar'])

# Create a button for Hebrew language
hebrew_button = tk.Button(root, text="Hebrew", cursor="hand2", command=switch_to_hebrew)
hebrew_button.pack()

# Create a button for English language
english_button = tk.Button(root, text="English", cursor="hand2", command=switch_to_english)
english_button.pack()

# Create a button for Arabic language
arabic_button = tk.Button(root, text='Arabic', cursor="hand2", command=switch_to_arabic)
arabic_button.pack()

# Start the main event loop
root.mainloop()
