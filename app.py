import tkinter as tk
import os
import json
import webbrowser
from tkinter import ttk, font
from datetime import datetime

def open_link(link):
    webbrowser.open(link)

def save_notes():
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

window = tk.Tk()
window.geometry("700x500")
window.title("Reflections")
window.iconbitmap("writing.ico")
style = ttk.Style()

# Ikon och länken
credit = ttk.Label(window, text="Diary icons created by Freepik - Flaticon", font=("Trebuchet MS", 8), style="Link.TLabel")
credit.pack(anchor="nw")
credit.bind("<Button-1>", lambda e: open_link("https://www.flaticon.com/free-icons/diary"))
style.configure("Link.TLabel", foreground="blue")

# Textvariabel
tab_text = font.Font(family="Trebuchet MS", size=10, weight="bold")
frame_text = font.Font(family="Trebuchet MS", size=10, slant="italic")
card_text = font.Font(family="Trebuchet MS", size=10)

# Notebook
notebook = ttk.Notebook(window)
notebook.pack(anchor="nw", fill="both", expand=True, padx=10, pady=10)

# Notebook Frames
frm_today = ttk.Frame(notebook, padding=20)
frm_today.pack(fill="both", expand=True)
frm_today.grid_columnconfigure(0, weight=1)
frm_archive = ttk.Frame(notebook)
frm_archive.pack(fill="both", expand=True)

container = tk.Canvas(frm_archive)
container.pack(side="left", fill="both", expand=True)
scrollbar = ttk.Scrollbar(frm_archive, orient="vertical", command=container.yview)
scrollbar.pack(side="right", fill="y")

container.configure(yscrollcommand=scrollbar.set)
inner_frame = ttk.Frame(container)
container.create_window((0,0), window=inner_frame, anchor="nw")
container.bind("<Configure>", lambda e: container.configure(scrollregion=container.bbox("all")))
container.bind_all("MouseWheel", scrollbar)
# Flikar
style.configure("TNotebook.Tab", padding=(30, 5), font=tab_text)
notebook.add(frm_today, text="Idag")
notebook.add(frm_archive, text="Arkiv")

# Fliken 'Idag'

# Första kolumnen
style.configure("TLabelframe.Label", font=frame_text)
frm_positive = ttk.LabelFrame(frm_today, text=" Tre positiva händelser från idag ", padding=10)
frm_positive.grid(row=0, column=0, rowspan=4, sticky="nw")
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

frm_mindset = ttk.LabelFrame(frm_today, text=" Positivt mindset inför morgondagen ", padding=10, style="Custom.TLabelframe")
frm_mindset.grid(row=4, column=0, rowspan=2, sticky="nw")
txt_mindset = tk.Text(frm_mindset, height=2, width=35, font=("Trebuchet MS", 10))
txt_mindset.grid(row=0, column=0, pady=(2, 1))

# Andra kolumnen
frm_notes = ttk.LabelFrame(frm_today, text=" Dagboksanteckningar ", padding=10, style="Custom.TLabelframe")
frm_notes.grid(row=0, column=1, rowspan=8, sticky="ns", padx=(8, 0))
txt_notes = tk.Text(frm_notes, height=9, width=35, font=("Trebuchet MS", 10), wrap="word")
txt_notes.grid(row=0, column=0)

# Spara
btn_save = ttk.Button(frm_today, text="Spara anteckning", padding=(30, 5), command=save_notes)
btn_save.grid(row=8, column=0, columnspan=2, pady=(8, 0))

# Fliken 'Arkiv'
style.configure("TLabel", font=card_text)
if os.path.isfile('data.json'):
    with open('data.json', 'r') as fileHandler:
        data = json.load(fileHandler)
    for notes in data:
        frm_notecard = ttk.LabelFrame(inner_frame, text=str(notes['date']), padding=5)
        frm_notecard.pack(anchor="nw", expand=True, fill="x", padx=10, pady=10)
        lbl_notecard_one = ttk.Label(frm_notecard, text=f"1. {notes['positive'][0]}")
        lbl_notecard_one.grid(row=0, column=0, columnspan=2, sticky="w")
        lbl_notecard_two = ttk.Label(frm_notecard, text=f"2. {notes['positive'][1]}")
        lbl_notecard_two.grid(row=1, column=0, columnspan=2, sticky="w")
        lbl_notecard_three = ttk.Label(frm_notecard, text=f"3. {notes['positive'][2]}")
        lbl_notecard_three.grid(row=2, column=0, columnspan=2, sticky="w")
        lbl_notecard_mindset = ttk.Label(frm_notecard, text=f"Mindset: {notes['mindset'].strip()}")
        lbl_notecard_mindset.grid(row=3, column=0, sticky="nw")
        daily_note = ttk.Label(frm_notecard, text=f"Anteckning: {notes['daily_notes'].strip()}", width=80, wraplength=500)
        daily_note.grid(row=4, column=0, sticky="w", rowspan=5)

tk.mainloop()
