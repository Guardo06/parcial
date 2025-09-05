import tkinter as tk
from tkinter import messagebox
import math

class FormCirculo:
    def __init__(self, master, titulo):
        self.master = master
        master.title(titulo)
        master.geometry("300x250")
        master.resizable(False, False)

        self.label_radio = tk.Label(master, text="Ingrese el radio:", font=("Arial", 12))
        self.label_radio.pack(pady=10)

        self.entry_radio = tk.Entry(master, width=20, font=("Arial", 12))
        self.entry_radio.pack(pady=5)
        self.entry_radio.focus_set()

        self.btn_calcular = tk.Button(master, text="Calcular", command=self.calcular, width=15, height=1)
        self.btn_calcular.pack(pady=10)

        self.label_area = tk.Label(master, text="Área: ", font=("Arial", 12, "bold"))
        self.label_area.pack(pady=5)

        self.label_perimetro = tk.Label(master, text="Perímetro: ", font=("Arial", 12, "bold"))
        self.label_perimetro.pack(pady=5)

    def calcular(self):
        try:
            radio = float(self.entry_radio.get())
            if radio < 0:
                messagebox.showerror("Error de Entrada", "El radio no puede ser negativo.")
                return
            area = math.pi * (radio ** 2)
            perimetro = 2 * math.pi * radio
            self.label_area.config(text=f"Área: {area:.2f}")
            self.label_perimetro.config(text=f"Perímetro: {perimetro:.2f}")
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingrese un número válido para el radio.")
