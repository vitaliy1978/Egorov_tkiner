import tkinter as tk
from tkinter import ttk

def show_day():
    print(combo.get(),combo_int.get())

weakDays = ("Monay", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", )
list_in = [1, 2, 3, 4, 5, 6, 7]

win = tk.Tk()
win.geometry(f"300x400+800+150")
win.title('Моё первое графическое приложение')

combo = ttk.Combobox(win, values=weakDays)
combo_int = ttk.Combobox(win, values=list_in)
ttk.Button(win, text='Show day', command=show_day).pack()
tk.Button(win, text='Show day').pack()
combo.current(4) # установка индекса комбобокса при открытии по умолчанию
combo_int.current(2) # установка индекса комбобокса при открытии по умолчанию
combo.pack()
combo_int.pack()

win.mainloop()