import tkinter as tk
from random import randint

def say_hello():
    print('Hello')

def add_label():  # функция создает новый лейбл
    label1 = tk.Label(win, text='Новый', )  # атрибуты лейбла
    label1.pack()

def counter():
    global count
    count += 1
    btn4['text'] = f'Счетчик: {count}'

def disabler():
    global num
    num += 1
    if num == 0:
        btn4['state'] = tk.DISABLED
        btn2['state'] = tk.NORMAL
        btn3['state'] = tk.NORMAL
    if num == 1:
        btn4['state'] = tk.NORMAL
        btn2['state'] = tk.DISABLED
        btn3['state'] = tk.NORMAL
    if num == 2:
        btn4['state'] = tk.NORMAL
        btn2['state'] = tk.NORMAL
        btn3['state'] = tk.DISABLED
        num = -1
def rand_color():
    x = f'#{str(hex(randint(10,255)))[2:]}{str(hex(randint(10,255)))[2:]}{str(hex(randint(10,255)))[2:]}'
    return x

num = -1
count = 0

win = tk.Tk()
photo = tk.PhotoImage(file='tkinter_icon.png')
win.iconphoto(False, photo)
win.config(bg=rand_color())
win.title('Моё первое графическое приложение на Python')
win.minsize(300, 400)  # минимальный размер окна

btn1 = tk.Button(win, text='Hello',  # атрибуты кнопки
                 command=disabler  # пишем функцию без скобок вызова функции
                 )

btn2 = tk.Button(win, text='Создаем лэйбл',  # атрибуты кнопки
                 command=add_label  # передаем функцию для создания лейбла
                 )

btn3 = tk.Button(win, text='Создаем лэйбл лямбда',  # атрибуты кнопки
                 command=lambda: tk.Label(win, text='Новая лямбда').pack()  # передаем функцию
                 )

btn4 = tk.Button(win, text=f'Счетчик: {count}',
                 command=counter,
                 activebackground='blue',
                 # state=tk.DISABLED,
                 bg='red'
                 )

btn1.pack()  # Метод размещает кнопку на экране
btn2.pack()  # Метод размещает кнопку на экране
btn3.pack()
btn4.pack()

win.mainloop()
