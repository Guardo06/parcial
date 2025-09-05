import tkinter as tk
from tkinter import messagebox

class FormRectangulo:
    def __init__(self, master, titulo):
        self.master = master
        master.title(titulo)
        master.geometry("300x300")
        master.resizable(False, False)

        self.label_base = tk.Label(master, text="Ingrese la base:", font=("Arial", 12))
        self.label_base.pack(pady=10)

        self.entry_base = tk.Entry(master, width=20, font=("Arial", 12))
        self.entry_base.pack(pady=5)
        self.entry_base.focus_set()

        self.label_altura = tk.Label(master, text="Ingrese la altura:", font=("Arial", 12))
        self.label_altura.pack(pady=10)

        self.entry_altura = tk.Entry(master, width=20, font=("Arial", 12))
        self.entry_altura.pack(pady=5)

        self.btn_calcular = tk.Button(master, text="Calcular", command=self.calcular, width=15, height=1)
        self.btn_calcular.pack(pady=10)

        self.label_area = tk.Label(master, text="Área: ", font=("Arial", 12, "bold"))
        self.label_area.pack(pady=5)

        self.label_perimetro = tk.Label(master, text="Perímetro: ", font=("Arial", 12, "bold"))
        self.label_perimetro.pack(pady=5)

    def calcular(self):
        try:
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            if base < 0 or altura < 0:
                messagebox.showerror("Error de Entrada", "La base y la altura no pueden ser negativas.")
                return
            area = base * altura
            perimetro = 2 * (base + altura)
            self.label_area.config(text=f"Área: {area:.2f}")
            self.label_perimetro.config(text=f"Perímetro: {perimetro:.2f}")
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingrese números válidos para la base y la altura.")
