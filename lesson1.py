import tkinter as tk

win = tk.Tk()
photo = tk.PhotoImage(file='tkinter_icon.png')
win.iconphoto(False, photo)
win.config(bg='#E4F2EA')
win.title('Моё первое графическое приложение на Python')
win.geometry("500x1000+10+10")   # размеры окна + положение от левого вернего угла
win.minsize(300,400)    # минимальный размер окна
win.maxsize(700,800)    # максимальный размер окна
win.resizable(True, True)     # изменяемость размеров в ширину и высоту


win.mainloop()