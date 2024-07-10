import tkinter as tk
from time import strftime

def relogio():
    tempo = strftime('%H:%M:%S')
    label.config(text=tempo)
    label.after(1000, relogio)

root = tk.Tk()
root.title('Relógio Digital')

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

relogio()
root.mainloop()
