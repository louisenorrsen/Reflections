import tkinter as tk
import webbrowser
from tkinter import ttk
from notebook import Notebook

class App(tk.Tk):
    def __init__(self, title, size, icon_url):
        super().__init__()
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.title(title)
        self.iconbitmap(icon_url)
        self.style = ttk.Style()

        credit = ttk.Label(self, text="Diary icons created by Freepik - Flaticon", font=("Trebuchet MS", 8), style="Link.TLabel")
        credit.pack(anchor="nw")
        credit.bind("<Button-1>", lambda e: open_link("https://www.flaticon.com/free-icons/diary"))
        self.style.configure("Link.TLabel", foreground="blue")

        Notebook(self)
        
        # Starta loopen
        self.mainloop()

        def open_link(link):
            webbrowser.open(link)

        
App("Reflections", (700, 500), "writing.ico")