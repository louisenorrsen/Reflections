import tkinter as tk
import webbrowser
from tkinter import ttk, colorchooser
from notebook import Notebook

class App(tk.Tk):
    def __init__(self, title, size, icon_url):
        super().__init__()
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.title(title)
        self.iconbitmap(icon_url)
        self.style = ttk.Style()

        self.colors = "#ab6bfd"

        frm_top = ttk.Frame(self)
        frm_top.pack(side="top", fill="x")
        self.style.configure("Link.TLabel",font=("Trebuchet MS", 8, "underline", "bold"), foreground=self.colors)
        self.credit = ttk.Label(frm_top, text="Diary icons created by Freepik - Flaticon", cursor="hand2", style="Link.TLabel")
        self.credit.pack(side="left", anchor="nw", padx=10)
        self.credit.bind("<Button-1>", lambda e: self.open_link("https://www.flaticon.com/free-icons/diary"))

        self.btn_color = tk.Button(frm_top, text="Change colors", relief="groove", background=self.colors, command=self.change_color)
        self.btn_color.pack(side="right", padx=10)

        self.notebook = Notebook(self, self.colors)
               
        # Starta loopen
        self.mainloop()

    def open_link(self, link):
        webbrowser.open(link)

    def change_color(self):
        # FIXME: fixa så texten blir något mörkare än användaren har valt om det är en ljus färg (HLS?)
        # FIXME: ändra knapparnas textfärg beroende på bakgrundsfärgens nyans 
        new_colors = colorchooser.askcolor()[1]
        if new_colors:
            self.colors = new_colors
            self.credit.configure(foreground=self.colors)
            self.btn_color.configure(background=self.colors)
            self.notebook.update_colors(new_colors)
        
App("Reflections", (700, 500), "writing.ico")