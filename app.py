import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Reflections")
window.iconbitmap("diary.ico")

# Notebook
notebook = ttk.Notebook(window)
notebook.pack(anchor="nw", expand=True, padx=10, pady=10)

# Notebook Frames
frm_today = ttk.Frame(notebook)
frm_today.pack(fill="both", expand=True)
frm_archive = ttk.Frame(notebook)
frm_archive.pack(fill="both", expand=True)

# Flikar
style = ttk.Style()
style.configure("TNotebook.Tab", padding=(10, 5))
notebook.add(frm_today, text="Idag")
notebook.add(frm_archive, text="Arkiv")

tk.mainloop()