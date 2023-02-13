import tkinter as tk


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')


def delete_entry():
    name.delete(name.index(tk.END) - 1)  # удаляет последний символ

def submit():
    print(name.get())
    print(password.get())
    name.delete(0, tk.END)
    password.delete(0, tk.END)

win = tk.Tk()
win.geometry(f'400x500+100+200')
win.title('Урок 5')

tk.Label(win, text='Имя').grid(row=0, column=0, sticky='w')
tk.Label(win, text='Пароль').grid(row=1, column=0, sticky='w')
name = tk.Entry(win)
password = tk.Entry(win, show='*')
name.grid(row=0, column=1)
password.grid(row=1, column=1)

tk.Button(win, text='Get', command=get_entry).grid(row=2, column=0, sticky='we')
tk.Button(win, text='Submit', command=submit).grid(row=1, column=2, sticky='we')
tk.Button(win, text='Delete', command=delete_entry).grid(row=2, column=1, sticky='we')
tk.Button(win, text='Insert', command=lambda: name.insert(0, 'hello')).grid(row=3, column=1, sticky='we')

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
