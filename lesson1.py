import tkinter as tk

win = tk.Tk()
photo = tk.PhotoImage(file='tkinter_icon.png')
win.iconphoto(False, photo)
win.config(bg='#E4F2EA')
win.title('Моё первое графическое приложение на Python')
win.geometry("500x1000+10+10")  # размеры окна + положение от левого вернего угла монитора
win.minsize(300, 400)  # минимальный размер окна
win.maxsize(700, 800)  # максимальный размер окна
win.resizable(True, True)  # изменяемость размеров в ширину и высоту

label1 = tk.Label(win, text='Привет',  # атрибуты лейбла
                  bg='#93A49A',  # цвет фона лейбла
                  fg='white',  # цвет шрифта
                  font=('Arial', 20, 'bold'),  # атрибуты шриф та лейбла
                  padx=10,  # отступ текста внутри лейбла по горизонтали
                  pady=5,  # отступ текста внутри лейбла по вертикали
                  width=10,  # ширина не пикселях, а в количестве знаков
                  height=3,  # высота не пикселях, а в количестве знаков
                  anchor='se',  # сторона света, к которой прижмется текст (n, s, w, e)
                  relief=tk.RAISED,  # границы виджета
                  bd=3,  # ширина границ(2 по умолчанию)
                  justify=tk.CENTER
                  )
label1.pack()   # Метод размещает лейбл на экране

win.mainloop()
