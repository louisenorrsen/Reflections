import tkinter as tk
from tkinter import ttk

class Notebook(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(anchor="nw", fill="both", expand=True, padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        self.create_today_tab()
        self.create_archive_tab()

    def create_today_tab(self):
        frm_today = ttk.Frame(self)
        self.add(frm_today, text="Idag")

    def create_archive_tab(self):
        frm_archive = ttk.Frame(self)
        self.add(frm_archive, text="Arkiv")