import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)  # чищаем экран
    calc.insert(0, value + digit)  # вставляем на экран переменную value
    calc['state'] = tk.DISABLED


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)  # очищаем экран
    calc.insert(0, value + operation)  # вставляем на экран переменную value
    calc['state'] = tk.DISABLED


def clear():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)  # очищаем экран
    calc.insert(0, 0)
    calc['state'] = tk.DISABLED


def calculate():
    value = calc.get()
    if value[-1] in '-+/*':
        value = value + value[:-1]
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)  # чищаем экран
    try:
        calc.insert(0, eval(value))  # вставляем на экран переменную value
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Нужно вводить только цифры! Вы ввели другие символы')
        calc.insert(0,0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя')
        calc.insert(0, 0)
    calc['state'] = tk.DISABLED

def make_digit_button(digit):
    return tk.Button(text=digit, bd=3, font=('Arial', 14), command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=3, font=('Arial', 14), fg='red', command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=3, font=('Arial', 14), fg='red', command=calculate)


def make_clear_button():
    return tk.Button(text='C', bd=3, font=('Arial', 13), fg='red', command=clear)

def press_key(event):
    print(event.char)
    if event.char.isdigit():
        add_digit(event.char)
    if event.char in '-+*/':
        add_operation(event.char)
    if event.char == '\r' or event.char == '=':
        calculate()

win = tk.Tk()
win.geometry(f"240x282+100+200")
win.maxsize(240, 282)
win.minsize(240, 282)
win['bg'] = '#D6EBEF'
win.title('Калькулятор')

win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 16), width=15, bd=3)
calc.insert(0, '0')
calc['state'] = tk.DISABLED
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx=5, pady=5)

make_digit_button('1').grid(row=1, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, sticky='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, sticky='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, sticky='wens', padx=5, pady=5)
make_clear_button().grid(row=4, column=1, sticky='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)  # Минимальный размер колонки
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)  # Минимальный размер колонки
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
