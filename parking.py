import tkinter as tk
from tkinter import messagebox
import zapisz
import time
import re
from oplaty import oblicz_oplate

def zaplac(dialog):
    rejestracja = rejestracja_entry.get()
    if rejestracja in parking:
        godzina_wyjazdu = time.strftime("%H:%M")
        parking[rejestracja].append(godzina_wyjazdu)
        oplata = oblicz_oplate(parking[rejestracja][0], godzina_wyjazdu, 2)
        zapisz.zapisz(rejestracja, parking[rejestracja][0], godzina_wyjazdu)
        del parking[rejestracja]
        dialog.destroy()

def dodaj_pojazd():
    rejestracja = rejestracja_entry.get()
    if not rejestracja:
        messagebox.showerror("Błąd", "Numer rejestracyjny nie może być pusty.")
        return

    if rejestracja in parking:
        godzina_wyjazdu = time.strftime("%H:%M")
        parking[rejestracja].append(godzina_wyjazdu)
        oplata = oblicz_oplate(parking[rejestracja][0], godzina_wyjazdu, 2)
        dialog = tk.Toplevel(root)
        dialog.title("Opłata za parking")
        label = tk.Label(dialog, text=f"Opłata za parking wynosi {oplata} zł.")
        label.pack()
        button = tk.Button(dialog, text="Zapłać", command=lambda: zaplac(dialog))
        button.pack()
    else:
        godzina_wjazdu = time.strftime("%H:%M")
        parking[rejestracja] = [godzina_wjazdu]
        messagebox.showinfo("Witamy", "Witamy na parkingu!")

parking = {}

root = tk.Tk()
root.title("System parkingu")
root.geometry("300x200")  # Zwiększ rozmiar okna

rejestracja_label = tk.Label(root, text="Numer rejestracyjny:")
rejestracja_label.pack()

rejestracja_entry = tk.Entry(root)
rejestracja_entry.pack()

dodaj_button = tk.Button(root, text="Dodaj pojazd", command=dodaj_pojazd)
dodaj_button.pack()

root.mainloop()
