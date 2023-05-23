import tkinter as tk
import os
import json
from tkinter import ttk, font
from datetime import datetime
from notecard import Notecard

# TODO: fixa en "statistik"-tab med data som: antal dagar i rad, totalt antal dagar, totalt skrivna ord, mest använda orden

class Notebook(ttk.Notebook):
    def __init__(self, parent, colors):
        super().__init__(parent)
        self.style = ttk.Style()
        self.pack(anchor="nw", fill="both", expand=True, padx=10, pady=10)
        self.colors = colors
        self.create_notebook_tabs()

    def create_notebook_tabs(self):
        tab_text = font.Font(family="Trebuchet MS", size=10, weight="bold")
        self.style.configure("TNotebook.Tab", padding=(30, 5), font=tab_text)
        self.create_today_tab()
        self.create_archive_tab()

    def create_today_tab(self):
        frm_today = ttk.Frame(self)        
        self.add(frm_today, text="Idag")
        self.create_today_widgets(frm_today)

    def create_archive_tab(self):
        # Skapar yttre ram för att få scrollen att fungera
        outer_frame = ttk.Frame(self)
        outer_frame.pack(fill="both", expand=True)

        # Skapar en Canvas som stödjer scroll
        self.frm_archive = tk.Canvas(outer_frame)
        self.frm_archive.pack(side="left", fill="both", expand=True)

        # Skapar en inre ram att lägga innehållet i
        self.container = ttk.Frame(self.frm_archive)
        self.container.bind("<Configure>", self.update_content_height)
        self.frm_archive.create_window((0,0), window=self.container, anchor="nw")

        # Skapar en scrollbar
        scrollbar = ttk.Scrollbar(outer_frame, orient="vertical", command=self.frm_archive.yview)
        scrollbar.pack(side="right", fill="y")

        self.frm_archive.configure(yscrollcommand=scrollbar.set)
        self.frm_archive.bind_all("<MouseWheel>", lambda e: self.frm_archive.yview_scroll(int(-1*(e.delta/120)), "units"))
        
        # Lägger till fliken i Notebook
        self.add(outer_frame, text="Arkiv")
        
        # Hämtar alla notes från JSON 
        self.fetch_notes(self.container)

    def create_today_widgets(self, parent):
        frame_text = font.Font(family="Trebuchet MS", size=10, slant="italic")
        self.style.configure("TLabelframe.Label", font=frame_text, foreground=self.colors)
        frm_positive = ttk.LabelFrame(parent, text=" Tre positiva händelser från idag ", padding=10)
        frm_positive.grid(row=0, column=0, rowspan=4, sticky="nw", padx=20, pady=20)
        lbl_one = ttk.Label(frm_positive, text="1. ", font=("Trebuchet MS", 10))
        lbl_one.grid(row=0, column=0, pady=2)
        self.ent_one = ttk.Entry(frm_positive, font=("Trebuchet MS", 10), foreground=self.colors, width=32)
        self.ent_one.grid(row=0, column=1, pady=2)
        lbl_two = ttk.Label(frm_positive, text="2. ", font=("Trebuchet MS", 10))
        lbl_two.grid(row=1, column=0, pady=2)
        self.ent_two = ttk.Entry(frm_positive, font=("Trebuchet MS", 10), foreground=self.colors, width=32)
        self.ent_two.grid(row=1, column=1, pady=2)
        lbl_three = ttk.Label(frm_positive, text="3. ", font=("Trebuchet MS", 10))
        lbl_three.grid(row=2, column=0, pady=2)
        self.ent_three = ttk.Entry(frm_positive, font=("Trebuchet MS", 10), foreground=self.colors, width=32)
        self.ent_three.grid(row=2, column=1, pady=2)

        frm_mindset = ttk.LabelFrame(parent, text=" Positivt mindset inför morgondagen ", padding=10)
        frm_mindset.grid(row=4, column=0, rowspan=2, sticky="nw", padx=20, pady=(0, 20))
        self.txt_mindset = tk.Text(frm_mindset, height=2, width=35, font=("Trebuchet MS", 10), foreground=self.colors)
        self.txt_mindset.grid(row=0, column=0, pady=(2, 1))

        frm_notes = ttk.LabelFrame(parent, text=" Dagboksanteckningar ", padding=10)
        frm_notes.grid(row=0, column=1, rowspan=8, sticky="ns", padx=20, pady=20)
        self.txt_notes = tk.Text(frm_notes, height=10, width=35, font=("Trebuchet MS", 10), foreground=self.colors, wrap="word")
        self.txt_notes.grid(row=0, column=0)

        self.btn_save = tk.Button(parent, text="Spara anteckning", padx=30, pady=5, background=self.colors, relief="groove", command=lambda: self.save_notes(self.ent_one, self.ent_two, self.ent_three, self.txt_mindset, self.txt_notes))
        self.btn_save.grid(row=8, column=0, columnspan=2, pady=(8, 0))

    def save_notes(self, ent_one, ent_two, ent_three, txt_mindset, txt_notes):
        # FIXME: spara inte om något av fälten är tomma
        # FIXME: ge användaren en varning om något av fälten är tomma
        note = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
            'positive': [
                ent_one.get(),
                ent_two.get(), 
                ent_three.get()
            ], 
            'mindset': txt_mindset.get("1.0", tk.END), 
            'daily_notes': txt_notes.get("1.0", tk.END)
        }
        # FIXME: om det redan finns en anteckning från den dagen, fråga användaren om den ska ersättas
        if os.path.isfile('data.json'):
            with open('data.json', 'r') as fileHandler:
                data = json.load(fileHandler)
        else:
            data = []

        data.append(note)

        with open('data.json', 'w') as fileHandler:
            json.dump(data, fileHandler)

        ent_one.delete(0, tk.END)
        ent_two.delete(0, tk.END)
        ent_three.delete(0, tk.END)
        txt_mindset.delete("1.0", tk.END)
        txt_notes.delete("1.0", tk.END)

        self.fetch_notes(self.container)

    def fetch_notes(self, parent):
        for child in parent.winfo_children():
            child.destroy()

        if os.path.isfile('data.json'):
            with open('data.json', 'r') as fileHandler:
                data = json.load(fileHandler)
            for note in data:
                Notecard(parent, note)

    def update_content_height(self, event):
        self.container.update_idletasks()
        self.frm_archive.configure(scrollregion=self.frm_archive.bbox("all"))

    def update_colors(self, colors):
        self.ent_one.configure(foreground=colors)
        self.ent_two.configure(foreground=colors)
        self.ent_one.configure(foreground=colors)
        self.txt_mindset.configure(foreground=colors)
        self.txt_notes.configure(foreground=colors)
        self.btn_save.configure(background=colors)
        self.style.configure("TLabelframe.Label", foreground=colors)
        
        
        