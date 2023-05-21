import tkinter as tk
import os
import json
from tkinter import ttk, font
from datetime import datetime
from notecard import Notecard

class Notebook(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.style = ttk.Style()
        self.pack(anchor="nw", fill="both", expand=True, padx=10, pady=10)
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
        frm_archive = tk.Canvas(self)
        self.add(frm_archive, text="Arkiv")
        self.container = ttk.Frame(frm_archive)
        frm_archive.create_window((0,0), window=self.container, anchor="nw")
        self.fetch_notes(self.container)

    def create_today_widgets(self, parent):
        frame_text = font.Font(family="Trebuchet MS", size=10, slant="italic")
        self.style.configure("TLabelframe.Label", font=frame_text)
        frm_positive = ttk.LabelFrame(parent, text=" Tre positiva händelser från idag ", padding=10)
        frm_positive.grid(row=0, column=0, rowspan=4, sticky="nw", padx=20, pady=20)
        lbl_one = ttk.Label(frm_positive, text="1. ", font=("Trebuchet MS", 10))
        lbl_one.grid(row=0, column=0, pady=2)
        ent_one = ttk.Entry(frm_positive, font=("Trebuchet MS", 10), width=32)
        ent_one.grid(row=0, column=1, pady=2)
        lbl_two = ttk.Label(frm_positive, text="2. ", font=("Trebuchet MS", 10))
        lbl_two.grid(row=1, column=0, pady=2)
        ent_two = ttk.Entry(frm_positive, font=("Trebuchet MS", 10), width=32)
        ent_two.grid(row=1, column=1, pady=2)
        lbl_three = ttk.Label(frm_positive, text="3. ", font=("Trebuchet MS", 10))
        lbl_three.grid(row=2, column=0, pady=2)
        ent_three = ttk.Entry(frm_positive, font=("Trebuchet MS", 10), width=32)
        ent_three.grid(row=2, column=1, pady=2)

        frm_mindset = ttk.LabelFrame(parent, text=" Positivt mindset inför morgondagen ", padding=10)
        frm_mindset.grid(row=4, column=0, rowspan=2, sticky="nw", padx=20, pady=(0, 20))
        txt_mindset = tk.Text(frm_mindset, height=2, width=35, font=("Trebuchet MS", 10))
        txt_mindset.grid(row=0, column=0, pady=(2, 1))

        frm_notes = ttk.LabelFrame(parent, text=" Dagboksanteckningar ", padding=10)
        frm_notes.grid(row=0, column=1, rowspan=8, sticky="ns", padx=20, pady=20)
        txt_notes = tk.Text(frm_notes, height=10, width=35, font=("Trebuchet MS", 10), wrap="word")
        txt_notes.grid(row=0, column=0)

        btn_save = ttk.Button(parent, text="Spara anteckning", padding=(30, 5), command=lambda: self.save_notes(ent_one, ent_two, ent_three, txt_mindset, txt_notes))
        btn_save.grid(row=8, column=0, columnspan=2, pady=(8, 0))

    def save_notes(self, ent_one, ent_two, ent_three, txt_mindset, txt_notes):
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
        if os.path.isfile('data.json'):
            with open('data.json', 'r') as fileHandler:
                data = json.load(fileHandler)
        else:
            data = []

        data.append(note)

        with open('data.json', 'w') as fileHandler:
            json.dump(data, fileHandler)

        self.fetch_notes(self.container)

    def fetch_notes(self, parent):
        for child in parent.winfo_children():
            child.destroy()

        if os.path.isfile('data.json'):
            with open('data.json', 'r') as fileHandler:
                data = json.load(fileHandler)
            for note in data:
                Notecard(parent, note)
        
        