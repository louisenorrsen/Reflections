from tkinter import ttk, font
class Notecard(ttk.LabelFrame):
    def __init__(self, parent, note):
        super().__init__(parent, text=str(note['date']), padding=5)
        self.pack(anchor="nw", expand=True, fill="x", padx=10, pady=10)
        
        self.style = ttk.Style()
        card_text = font.Font(family="Trebuchet MS", size=10)
        self.style.configure("TLabel", font=card_text)
        
        lbl_notecard_one = ttk.Label(self, text=f"1. {note['positive'][0]}")
        lbl_notecard_one.grid(row=0, column=0, columnspan=2, sticky="w")
        
        lbl_notecard_two = ttk.Label(self, text=f"2. {note['positive'][1]}")
        lbl_notecard_two.grid(row=1, column=0, columnspan=2, sticky="w")
        
        lbl_notecard_three = ttk.Label(self, text=f"3. {note['positive'][2]}")
        lbl_notecard_three.grid(row=2, column=0, columnspan=2, sticky="w")
        
        lbl_notecard_mindset = ttk.Label(self, text=f"Mindset: {note['mindset'].strip()}")
        lbl_notecard_mindset.grid(row=3, column=0, sticky="nw")
        
        daily_note = ttk.Label(self, text=f"Anteckning: {note['daily_notes'].strip()}", width=80, wraplength=500)
        daily_note.grid(row=4, column=0, sticky="w", rowspan=5)
