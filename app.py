import tkinter as tk
from tkinter import ttk, font

window = tk.Tk()
window.title("Reflections")
window.iconbitmap("diary.ico")

# Textvariabel
tab_text = font.Font(family="Trebuchet MS", size=10, weight="bold")

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
tab_style = ttk.Style()
tab_style.configure("TNotebook.Tab", padding=(30, 5), font=tab_text)
notebook.add(frm_today, text="Idag")
notebook.add(frm_archive, text="Arkiv")

# Fliken 'Idag'

# Första kolumnen 
frm_positive = ttk.LabelFrame(frm_today, text=" Tre positiva händelser från idag ", padding=10)
frm_positive.grid(row=0, column=0, rowspan=4, sticky="nsew")
lbl_one = ttk.Label(frm_positive, text="1. ")
lbl_one.grid(row=0, column=0, pady=2)
ent_one = ttk.Entry(frm_positive, font=("Trebuchet MS", 8), width=32)
ent_one.grid(row=0, column=1, pady=2)
lbl_two = ttk.Label(frm_positive, text="2. ")
lbl_two.grid(row=1, column=0, pady=2)
ent_two = ttk.Entry(frm_positive, font=("Trebuchet MS", 8), width=32)
ent_two.grid(row=1, column=1, pady=2)
lbl_three = ttk.Label(frm_positive, text="3. ")
lbl_three.grid(row=2, column=0, pady=2)
ent_three = ttk.Entry(frm_positive, font=("Trebuchet MS", 8), width=32)
ent_three.grid(row=2, column=1, pady=2)

frm_mindset = ttk.LabelFrame(frm_today, text=" Positivt mindset inför morgondagen ", padding=10)
frm_mindset.grid(row=4, column=0, rowspan=2, sticky="nsew", pady=5)
txt_mindset = tk.Text(frm_mindset, height=2, width=35, font=("Trebuchet MS", 8))
txt_mindset.grid(row=0, column=0)

tk.mainloop()