import tkinter as tk
from tkinter import ttk, font

window = tk.Tk()
window.title("Reflections")
window.iconbitmap("diary.ico")
style = ttk.Style()

# Textvariabel
tab_text = font.Font(family="Trebuchet MS", size=10, weight="bold")
frame_text = font.Font(family="Trebuchet MS", size=10, slant="italic")

# Notebook
notebook = ttk.Notebook(window)
notebook.pack(anchor="nw", expand=True, padx=10, pady=10)

# Notebook Frames
frm_today = ttk.Frame(notebook, padding=20)
frm_today.pack(fill="both", expand=True)
frm_today.grid_columnconfigure(0, weight=1)
frm_archive = ttk.Frame(notebook)
frm_archive.pack(fill="both", expand=True)

# Flikar
style.configure("TNotebook.Tab", padding=(30, 5), font=tab_text)
notebook.add(frm_today, text="Idag")
notebook.add(frm_archive, text="Arkiv")

# Fliken 'Idag'

# Första kolumnen 
style.configure("TLabelframe.Label", font=frame_text)
frm_positive = ttk.LabelFrame(frm_today, text=" Tre positiva händelser från idag ", padding=10)
frm_positive.grid(row=0, column=0, rowspan=4, sticky="nsew")
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
frm_mindset.grid(row=4, column=0, rowspan=2, sticky="nsew")
txt_mindset = tk.Text(frm_mindset, height=2, width=35, font=("Trebuchet MS", 10))
txt_mindset.grid(row=0, column=0, pady=(2, 1))

# Andra kolumnen
frm_notes = ttk.LabelFrame(frm_today, text=" Dagboksanteckningar ", padding=10, style="Custom.TLabelframe")
frm_notes.grid(row=0, column=1, rowspan=8, sticky="ns", padx=(8, 0))
txt_notes = tk.Text(frm_notes, height=9, width=35, font=("Trebuchet MS", 10))
txt_notes.grid(row=0, column=0)

# Spara
btn_save = ttk.Button(frm_today, text="Spara anteckning", padding=(30, 5))
btn_save.grid(row=8, column=0, columnspan=2, pady=(8, 0))

tk.mainloop()