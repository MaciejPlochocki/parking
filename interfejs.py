import tkinter as tk
from tkinter import messagebox, simpledialog

def pobierz_rejestracje():
    return simpledialog.askstring("Numer rejestracyjny", "Proszę podać numer rejestracyjny:")

def wyswietl_blad(wiadomosc):
    messagebox.showerror("Błąd", wiadomosc)

def wyswietl_oplate(oplata):
    messagebox.showinfo("Opłata za parking", f"Opłata za parking wynosi {oplata} zł.")

def wyswietl_powitanie():
    messagebox.showinfo("Witamy", "Witamy na parkingu!")
