import tkinter as tk
import subprocess

root = tk.Tk()
root.title("Language Switcher")

def switch_to_hebrew():
    subprocess.run(['setxkbmap', 'il'])

def switch_to_english():
    subprocess.run(['setxkbmap', 'us'])

def switch_to_arabic():
    subprocess.run(['setxkbmap', 'ar'])
    
hebrew_button = tk.Button(root, text="Hebrew",cursor="hand2", command=switch_to_hebrew)
hebrew_button.pack()


english_button = tk.Button(root, text="English",cursor="hand2", command=switch_to_english)
english_button.pack()

arabic_button = tk.Button(root, text='Arabic',cursor="hand2", command=switch_to_arabic)
arabic_button.pack()

root.mainloop()
