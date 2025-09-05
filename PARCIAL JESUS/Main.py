import tkinter as tk

from tkinter import messagebox 

from Formularios.FormCirculo import FormCirculo
from Formularios.FormCuadrado import FormCuadrado
from Formularios.FormRectangulo import FormRectangulo
from Formularios.FormTriangulo import FormTriangulo


class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("Cálculo de Figuras")
        master.geometry("300x300")
        master.resizable(False, False)

        tk.Label(master, text="Seleccione una figura:", font=("Arial", 14, "bold")).pack(pady=20)

        tk.Button(master, text="Círculo", width=20, command=self.abrir_circulo).pack(pady=5)
        tk.Button(master, text="Cuadrado", width=20, command=self.abrir_cuadrado).pack(pady=5)
        tk.Button(master, text="Rectángulo", width=20, command=self.abrir_rectangulo).pack(pady=5)
        tk.Button(master, text="Triángulo", width=20, command=self.abrir_triangulo).pack(pady=5)

    def abrir_circulo(self):
        win = tk.Toplevel(self.master)
        FormCirculo(win, "Círculo")

    def abrir_cuadrado(self):
        win = tk.Toplevel(self.master)
        FormCuadrado(win, "Cuadrado")

    def abrir_rectangulo(self):
        win = tk.Toplevel(self.master)
        FormRectangulo(win, "Rectángulo")

    def abrir_triangulo(self):
        win = tk.Toplevel(self.master)
        FormTriangulo(win, "Triángulo")


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
