from tkinter import *
from tkinter import ttk


# Метод, который отвечает за переключение радиокнопок и выставляет границы рамок захвата игровой области
# по параметрам из словаря координат self.cords_dict.
def rb_select():
    pare_box = ()
    suited_box = ()
    offsuited_box = ()
    for bg in hands_signals_tuple:
        bg['bg'] = 'SystemButtonFace'

    if rb.get() == '1':
        pare_box = (hAA, hKK, hQQ, hJJ, hTT, h99, h88, h77,
                    h66, h55, h44, h33, h22)
        suited_box = (hAKs, hAQs, hAJs, hATs, hA9s, hA8s, hA7s,
                      hA6s, hA5s, hA4s, hA3s, hA2s,
                      hKQs, hKJs, hKTs,
                      hQJs, hQTs, hQ9s,
                      hJTs, hJ9s,
                      hT9s)
        offsuited_box = (hAKo, hAQo, hAJo, hATo, hA9o, hA8o,
                         hKQo, hKJo)
    elif rb.get() == '2':
        pare_box = (hAA, hKK, hQQ, hJJ, hTT, h99, h88, h77,
                    h66, h55, h44, h33, h22)
        suited_box = (hAKs, hAQs, hAJs, hATs, hA9s, hA8s, hA7s,
                      hA6s, hA5s, hA4s, hA3s, hA2s,
                      hKQs, hKJs, hKTs, hK9s, hK8s,
                      hQJs, hQTs, hQ9s,
                      hJTs, hJ9s, hJ8s,
                      hT9s, hT8s,
                      h98s,
                      h87s)
        offsuited_box = (hAKo, hAQo, hAJo, hATo, hA9o, hA8o, hA7o,
                         hA6o, hA5o, hA4o, hA3o, hA2o,
                         hKQo, hKJo, hKTo,
                         hQJo,
                         hJTo)
    elif rb.get() == '3':
        pare_box = (hAA, hKK, hQQ, hJJ, hTT, h99, h88, h77,
                    h66, h55, h44, h33, h22)
        suited_box = (hAKs, hAQs, hAJs, hATs, hA9s, hA8s, hA7s,
                      hA6s, hA5s, hA4s, hA3s, hA2s,
                      hKQs, hKJs, hKTs, hK9s, hK8s, hK7s, hK6s,
                      hK5s, hK4s, hK3s, hK2s,
                      hQJs, hQTs, hQ9s, hQ8s, hQ7s, hQ6s, hQ5s,
                      hQ4s, hQ3s,
                      hJTs, hJ9s, hJ8s, hJ7s, hJ6s, hJ5s,
                      hT9s, hT8s, hT7s, hT6s,
                      h98s, h97s, h96s,
                      h87s, h86s, h85s,
                      h76s, h75s,
                      h65s, h64s,
                      h54s)
        offsuited_box = (hAKo, hAQo, hAJo, hATo, hA9o, hA8o, hA7o,
                         hA6o, hA5o, hA4o, hA3o, hA2o,
                         hKQo, hKJo, hKTo, hK9o, hK8o, hK7o, hK6o,
                         hK5o, hK4o, hK3o, hK2o,
                         hQJo, hQTo, hQ9o, hQ8o,
                         hJTo, hJ9o,
                         hT9o, hT8o,
                         h98o)
    elif rb.get() == '6':
        pare_box = (hAA, hKK, hQQ, hJJ, hTT, h99, h88, h77,
                    h66, h55)
        suited_box = (hAKs, hAQs, hAJs, hATs, hA9s, hA8s,
                      hKQs, hKJs)
        offsuited_box = (hAKo, hAQo, hAJo, hATo)
    elif rb.get() == '7':
        pare_box = (hAA, hKK, hQQ, hJJ, hTT, h99, h88, h77,
                    h66, h55, h44)
        suited_box = (hAKs, hAQs, hAJs, hATs, hA9s, hA8s, hA7s,
                      hKQs, hKJs)
        offsuited_box = (hAKo, hAQo, hAJo, hATo, hA9o,
                         hKQo)
    elif rb.get() == '8':
        pare_box = (hAA, hKK, hQQ, hJJ, hTT, h99, h88, h77,
                    h66, h55, h44, h33)
        suited_box = (hAKs, hAQs, hAJs, hATs, hA9s, hA8s, hA7s,
                      hA6s, hA5s, hA4s, hA3s,
                      hKQs, hKJs, hKTs,
                      hQJs)
        offsuited_box = (hAKo, hAQo, hAJo, hATo, hA9o, hA8o,
                         hKQo, hKJo)
    elif rb.get() == '11':
        pare_box = (hAA, hKK, hQQ, hJJ, hTT, h99, h88, h77,
                    h66, h55, h44, h33)
        suited_box = (hAKs, hAQs, hAJs, hATs, hA9s, hA8s, hA7s,
                      hA6s, hA5s, hA4s,
                      hKQs, hKJs, hKTs,
                      hQJs)
        offsuited_box = (hAKo, hAQo, hAJo, hATo, hA9o, hA8o, hA7o,
                         hKQo, hKJo)
    elif rb.get() == '12':
        pare_box = (hAA, hKK, hQQ, hJJ, hTT, h99, h88, h77,
                    h66, h55, h44, h33, h22)
        suited_box = (hAKs, hAQs, hAJs, hATs, hA9s, hA8s, hA7s,
                      hA6s, hA5s, hA4s, hA3s, hA2s,
                      hKQs, hKJs, hKTs, hK9s,
                      hQJs, hQTs)
        offsuited_box = (hAKo, hAQo, hAJo, hATo, hA9o, hA8o, hA7o,
                         hA6o, hA5o,
                         hKQo, hKJo, hKTo)
    elif rb.get() == '13':
        pare_box = (hAA, hKK, hQQ, hJJ, hTT, h99, h88, h77,
                    h66, h55, h44, h33, h22)
        suited_box = (hAKs, hAQs, hAJs, hATs, hA9s, hA8s, hA7s,
                      hA6s, hA5s, hA4s, hA3s, hA2s,
                      hKQs, hKJs, hKTs, hK9s, hK8s, hK7s, hK6s,
                      hK5s, hK4s, hK3s, hK2s,
                      hQJs, hQTs, hQ9s, hQ8s, hQ7s,
                      hJTs, hJ9s, hJ8s,
                      hT9s)
        offsuited_box = (hAKo, hAQo, hAJo, hATo, hA9o, hA8o, hA7o,
                         hA6o, hA5o, hA4o, hA3o, hA2o,
                         hKQo, hKJo, hKTo, hK9o, hK8o, hK7o, hK6o,
                         hQJo, hQTo, hQ9o,
                         hJTo)
    elif rb.get() == '14':
        pare_box = (hAA, hKK, hQQ, hJJ, hTT, h99, h88, h77)
        suited_box = (hAKs, hAQs, hAJs,
                      hKQs)
        offsuited_box = (hAKo, hAQo)
    elif rb.get() == '15':
        pare_box = (hAA, hKK, hQQ, hJJ, hTT, h99, h88, h77,
                    h66)
        suited_box = (hAKs, hAQs, hAJs, hATs,
                      hKQs, hKJs,
                      hQJs)
        offsuited_box = (hAKo, hAQo, hAJo)
    elif rb.get() == '16':
        pare_box = (hAA, hKK, hQQ, hJJ, hTT, h99, h88, h77,
                    h66, h55, h44)
        suited_box = (hAKs, hAQs, hAJs, hATs, hA9s,
                      hKQs, hKJs, hKTs,
                      hQJs, hQTs,
                      hJTs)
        offsuited_box = (hAKo, hAQo, hAJo, hATo,
                         hKQo)

    for pare_card in pare_box:
        pare_card['bg'] = 'SteelBlue'
    for suited_card in suited_box:
        suited_card['bg'] = 'Gold'
    for offsuited_card in offsuited_box:
        offsuited_card['bg'] = 'Tomato'


# Основные настройки главного окна интерфейса.
console = Tk()  # Обязательный протокол начала цикла tkinter.
screen_width = console.winfo_screenwidth()  # Считывание ширины экрана.
screen_height = console.winfo_screenheight()  # Считывание высоты экрана.
console.wm_attributes('-topmost', 1)  # Параметры задают нахождение окна интерфейса поверх остальных окон.
console.geometry('382x532+976+0')  # Параметр задаёт размеры окна интерфейса в пикселях.
console.resizable(False, False)  # Не даёт пользователю прав на изменение экрана ОИ.
console.config(bd=0, padx=0, pady=0, bg='black', highlightthickness=1, highlightcolor='white')
# Задаёт отступы, обрамления и цвет фона.
console.iconbitmap(r'console_icon.ico')  # Отображает иконку программы на ОИ.
console.title('PokerSPY lite')  # Отображает название программы на ОИ.

# Динамические переменные, участвующие в работе интерфейса.
rb = StringVar()  # Переменная значений для радиокнопки.

# Холст для отображения диапазонов рук.
range_canvas = Canvas(console, bd=0, height=297, highlightthickness=1)
range_canvas.pack()

# Создаём сетку рук для отображения в интерфейсе.
hands_grid = LabelFrame(range_canvas, bd=0, padx=0, pady=0, highlightthickness=0, highlightbackground='black')
hands_grid.place(x=0, y=0)

hands_grid.grid_columnconfigure(0, minsize=30)
hands_grid.grid_columnconfigure(1, minsize=29)
hands_grid.grid_columnconfigure(2, minsize=29)
hands_grid.grid_columnconfigure(3, minsize=29)
hands_grid.grid_columnconfigure(4, minsize=29)
hands_grid.grid_columnconfigure(5, minsize=29)
hands_grid.grid_columnconfigure(6, minsize=30)
hands_grid.grid_columnconfigure(7, minsize=29)
hands_grid.grid_columnconfigure(8, minsize=29)
hands_grid.grid_columnconfigure(9, minsize=29)
hands_grid.grid_columnconfigure(10, minsize=29)
hands_grid.grid_columnconfigure(11, minsize=29)
hands_grid.grid_columnconfigure(12, minsize=30)

# Выводим в интерфейс пользователя весь диапазон рук,
# который по умолчанию будет неактивен и отображаться серым цветом.
# relief = flat, groove, raised, ridge, solid, or sunken
# n, ne, e, se, s, sw, w, nw, or center
hAA = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='AA',
            font=('', '9', 'bold'))
hAKs = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='AKs',
             font=('', '9', 'bold'))
hAQs = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='AQs',
             font=('', '9', 'bold'))
hAJs = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='AJs',
             font=('', '9', 'bold'))
hATs = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='ATs',
             font=('', '9', 'bold'))
hA9s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A9s',
             font=('', '9', 'bold'))
hA8s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A8s',
             font=('', '9', 'bold'))
hA7s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A7s',
             font=('', '9', 'bold'))
hA6s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A6s',
             font=('', '9', 'bold'))
hA5s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A5s',
             font=('', '9', 'bold'))
hA4s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A4s',
             font=('', '9', 'bold'))
hA3s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A3s',
             font=('', '9', 'bold'))
hA2s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A2s',
             font=('', '9', 'bold'))
hAKo = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='AKo',
             font=('', '9', 'bold'))
hAQo = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='AQo',
             font=('', '9', 'bold'))
hAJo = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='AJo',
             font=('', '9', 'bold'))
hATo = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='ATo',
             font=('', '9', 'bold'))
hA9o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A9o',
             font=('', '9', 'bold'))
hA8o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A8o',
             font=('', '9', 'bold'))
hA7o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A7o',
             font=('', '9', 'bold'))
hA6o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A6o',
             font=('', '9', 'bold'))
hA5o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A5o',
             font=('', '9', 'bold'))
hA4o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A4o',
             font=('', '9', 'bold'))
hA3o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A3o',
             font=('', '9', 'bold'))
hA2o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='A2o',
             font=('', '9', 'bold'))

hKK = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='KK',
            font=('', '9', 'bold'))
hKQs = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='KQs',
             font=('', '9', 'bold'))
hKJs = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='KJs',
             font=('', '9', 'bold'))
hKTs = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='KTs',
             font=('', '9', 'bold'))
hK9s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K9s',
             font=('', '9', 'bold'))
hK8s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K8s',
             font=('', '9', 'bold'))
hK7s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K7s',
             font=('', '9', 'bold'))
hK6s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K6s',
             font=('', '9', 'bold'))
hK5s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K5s',
             font=('', '9', 'bold'))
hK4s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K4s',
             font=('', '9', 'bold'))
hK3s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K3s',
             font=('', '9', 'bold'))
hK2s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K2s',
             font=('', '9', 'bold'))
hKQo = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='KQo',
             font=('', '9', 'bold'))
hKJo = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='KJo',
             font=('', '9', 'bold'))
hKTo = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='KTo',
             font=('', '9', 'bold'))
hK9o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K9o',
             font=('', '9', 'bold'))
hK8o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K8o',
             font=('', '9', 'bold'))
hK7o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K7o',
             font=('', '9', 'bold'))
hK6o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K6o',
             font=('', '9', 'bold'))
hK5o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K5o',
             font=('', '9', 'bold'))
hK4o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K4o',
             font=('', '9', 'bold'))
hK3o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K3o',
             font=('', '9', 'bold'))
hK2o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='K2o',
             font=('', '9', 'bold'))

hQQ = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='QQ',
            font=('', '9', 'bold'))
hQJs = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='QJs',
             font=('', '9', 'bold'))
hQTs = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='QTs',
             font=('', '9', 'bold'))
hQ9s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q9s',
             font=('', '9', 'bold'))
hQ8s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q8s',
             font=('', '9', 'bold'))
hQ7s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q7s',
             font=('', '9', 'bold'))
hQ6s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q6s',
             font=('', '9', 'bold'))
hQ5s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q5s',
             font=('', '9', 'bold'))
hQ4s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q4s',
             font=('', '9', 'bold'))
hQ3s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q3s',
             font=('', '9', 'bold'))
hQ2s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q2s',
             font=('', '9', 'bold'))
hQJo = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='QJo',
             font=('', '9', 'bold'))
hQTo = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='QTo',
             font=('', '9', 'bold'))
hQ9o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q9o',
             font=('', '9', 'bold'))
hQ8o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q8o',
             font=('', '9', 'bold'))
hQ7o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q7o',
             font=('', '9', 'bold'))
hQ6o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q6o',
             font=('', '9', 'bold'))
hQ5o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q5o',
             font=('', '9', 'bold'))
hQ4o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q4o',
             font=('', '9', 'bold'))
hQ3o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q3o',
             font=('', '9', 'bold'))
hQ2o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='Q2o',
             font=('', '9', 'bold'))

hJJ = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='JJ',
            font=('', '9', 'bold'))
hJTs = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='JTs',
             font=('', '9', 'bold'))
hJ9s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J9s',
             font=('', '9', 'bold'))
hJ8s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J8s',
             font=('', '9', 'bold'))
hJ7s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J7s',
             font=('', '9', 'bold'))
hJ6s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J6s',
             font=('', '9', 'bold'))
hJ5s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J5s',
             font=('', '9', 'bold'))
hJ4s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J4s',
             font=('', '9', 'bold'))
hJ3s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J3s',
             font=('', '9', 'bold'))
hJ2s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J2s',
             font=('', '9', 'bold'))
hJTo = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='JTo',
             font=('', '9', 'bold'))
hJ9o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J9o',
             font=('', '9', 'bold'))
hJ8o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J8o',
             font=('', '9', 'bold'))
hJ7o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J7o',
             font=('', '9', 'bold'))
hJ6o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J6o',
             font=('', '9', 'bold'))
hJ5o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J5o',
             font=('', '9', 'bold'))
hJ4o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J4o',
             font=('', '9', 'bold'))
hJ3o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J3o',
             font=('', '9', 'bold'))
hJ2o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='J2o',
             font=('', '9', 'bold'))

hTT = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='TT',
            font=('', '9', 'bold'))
hT9s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T9s',
             font=('', '9', 'bold'))
hT8s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T8s',
             font=('', '9', 'bold'))
hT7s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T7s',
             font=('', '9', 'bold'))
hT6s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T6s',
             font=('', '9', 'bold'))
hT5s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T5s',
             font=('', '9', 'bold'))
hT4s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T4s',
             font=('', '9', 'bold'))
hT3s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T3s',
             font=('', '9', 'bold'))
hT2s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T2s',
             font=('', '9', 'bold'))
hT9o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T9o',
             font=('', '9', 'bold'))
hT8o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T8o',
             font=('', '9', 'bold'))
hT7o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T7o',
             font=('', '9', 'bold'))
hT6o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T6o',
             font=('', '9', 'bold'))
hT5o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T5o',
             font=('', '9', 'bold'))
hT4o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T4o',
             font=('', '9', 'bold'))
hT3o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T3o',
             font=('', '9', 'bold'))
hT2o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='T2o',
             font=('', '9', 'bold'))

h99 = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='99',
            font=('', '9', 'bold'))
h98s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='98s',
             font=('', '9', 'bold'))
h97s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='97s',
             font=('', '9', 'bold'))
h96s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='96s',
             font=('', '9', 'bold'))
h95s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='95s',
             font=('', '9', 'bold'))
h94s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='94s',
             font=('', '9', 'bold'))
h93s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='93s',
             font=('', '9', 'bold'))
h92s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='92s',
             font=('', '9', 'bold'))
h98o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='98o',
             font=('', '9', 'bold'))
h97o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='97o',
             font=('', '9', 'bold'))
h96o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='96o',
             font=('', '9', 'bold'))
h95o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='95o',
             font=('', '9', 'bold'))
h94o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='94o',
             font=('', '9', 'bold'))
h93o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='93o',
             font=('', '9', 'bold'))
h92o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='92o',
             font=('', '9', 'bold'))

h88 = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='88',
            font=('', '9', 'bold'))
h87s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='87s',
             font=('', '9', 'bold'))
h86s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='86s',
             font=('', '9', 'bold'))
h85s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='85s',
             font=('', '9', 'bold'))
h84s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='84s',
             font=('', '9', 'bold'))
h83s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='83s',
             font=('', '9', 'bold'))
h82s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='82s',
             font=('', '9', 'bold'))
h87o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='87o',
             font=('', '9', 'bold'))
h86o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='86o',
             font=('', '9', 'bold'))
h85o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='85o',
             font=('', '9', 'bold'))
h84o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='84o',
             font=('', '9', 'bold'))
h83o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='83o',
             font=('', '9', 'bold'))
h82o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='82o',
             font=('', '9', 'bold'))

h77 = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='77',
            font=('', '9', 'bold'))
h76s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='76s',
             font=('', '9', 'bold'))
h75s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='75s',
             font=('', '9', 'bold'))
h74s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='74s',
             font=('', '9', 'bold'))
h73s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='73s',
             font=('', '9', 'bold'))
h72s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='72s',
             font=('', '9', 'bold'))
h76o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='76o',
             font=('', '9', 'bold'))
h75o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='75o',
             font=('', '9', 'bold'))
h74o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='74o',
             font=('', '9', 'bold'))
h73o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='73o',
             font=('', '9', 'bold'))
h72o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='72o',
             font=('', '9', 'bold'))

h66 = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='66',
            font=('', '9', 'bold'))
h65s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='65s',
             font=('', '9', 'bold'))
h64s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='64s',
             font=('', '9', 'bold'))
h63s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='63s',
             font=('', '9', 'bold'))
h62s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='62s',
             font=('', '9', 'bold'))
h65o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='65o',
             font=('', '9', 'bold'))
h64o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='64o',
             font=('', '9', 'bold'))
h63o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='63o',
             font=('', '9', 'bold'))
h62o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='62o',
             font=('', '9', 'bold'))

h55 = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='55',
            font=('', '9', 'bold'))
h54s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='54s',
             font=('', '9', 'bold'))
h53s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='53s',
             font=('', '9', 'bold'))
h52s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='52s',
             font=('', '9', 'bold'))
h54o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='54o',
             font=('', '9', 'bold'))
h53o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='53o',
             font=('', '9', 'bold'))
h52o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='52o',
             font=('', '9', 'bold'))

h44 = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='44',
            font=('', '9', 'bold'))
h43s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='43s',
             font=('', '9', 'bold'))
h42s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='42s',
             font=('', '9', 'bold'))
h43o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='43o',
             font=('', '9', 'bold'))
h42o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='42o',
             font=('', '9', 'bold'))

h33 = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='33',
            font=('', '9', 'bold'))
h32s = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='32s',
             font=('', '9', 'bold'))
h32o = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='32o',
             font=('', '9', 'bold'))
h22 = Label(hands_grid, width=3, height=1, bd=1, highlightthickness=3, padx=0, pady=0, relief='solid', text='22',
            font=('', '9', 'bold'))

# Размещаем все руки в сетку интерфейса пользователя.
hAA.grid(row=0, column=0, stick='we')
hAKs.grid(row=0, column=1)
hAQs.grid(row=0, column=2)
hAJs.grid(row=0, column=3)
hATs.grid(row=0, column=4)
hA9s.grid(row=0, column=5)
hA8s.grid(row=0, column=6, stick='we')
hA7s.grid(row=0, column=7)
hA6s.grid(row=0, column=8)
hA5s.grid(row=0, column=9)
hA4s.grid(row=0, column=10)
hA3s.grid(row=0, column=11)
hA2s.grid(row=0, column=12, stick='we')

hAKo.grid(row=1, column=0, stick='we')
hKK.grid(row=1, column=1)
hKQs.grid(row=1, column=2)
hKJs.grid(row=1, column=3)
hKTs.grid(row=1, column=4)
hK9s.grid(row=1, column=5)
hK8s.grid(row=1, column=6, stick='we')
hK7s.grid(row=1, column=7)
hK6s.grid(row=1, column=8)
hK5s.grid(row=1, column=9)
hK4s.grid(row=1, column=10)
hK3s.grid(row=1, column=11)
hK2s.grid(row=1, column=12, stick='we')

hAQo.grid(row=2, column=0, stick='we')
hKQo.grid(row=2, column=1)
hQQ.grid(row=2, column=2)
hQJs.grid(row=2, column=3)
hQTs.grid(row=2, column=4)
hQ9s.grid(row=2, column=5)
hQ8s.grid(row=2, column=6, stick='we')
hQ7s.grid(row=2, column=7)
hQ6s.grid(row=2, column=8)
hQ5s.grid(row=2, column=9)
hQ4s.grid(row=2, column=10)
hQ3s.grid(row=2, column=11)
hQ2s.grid(row=2, column=12, stick='we')

hAJo.grid(row=3, column=0, stick='we')
hKJo.grid(row=3, column=1)
hQJo.grid(row=3, column=2)
hJJ.grid(row=3, column=3)
hJTs.grid(row=3, column=4)
hJ9s.grid(row=3, column=5)
hJ8s.grid(row=3, column=6, stick='we')
hJ7s.grid(row=3, column=7)
hJ6s.grid(row=3, column=8)
hJ5s.grid(row=3, column=9)
hJ4s.grid(row=3, column=10)
hJ3s.grid(row=3, column=11)
hJ2s.grid(row=3, column=12, stick='we')

hATo.grid(row=4, column=0, stick='we')
hKTo.grid(row=4, column=1)
hQTo.grid(row=4, column=2)
hJTo.grid(row=4, column=3)
hTT.grid(row=4, column=4)
hT9s.grid(row=4, column=5)
hT8s.grid(row=4, column=6, stick='we')
hT7s.grid(row=4, column=7)
hT6s.grid(row=4, column=8)
hT5s.grid(row=4, column=9)
hT4s.grid(row=4, column=10)
hT3s.grid(row=4, column=11)
hT2s.grid(row=4, column=12, stick='we')

hA9o.grid(row=5, column=0, stick='we')
hK9o.grid(row=5, column=1)
hQ9o.grid(row=5, column=2)
hJ9o.grid(row=5, column=3)
hT9o.grid(row=5, column=4)
h99.grid(row=5, column=5)
h98s.grid(row=5, column=6, stick='we')
h97s.grid(row=5, column=7)
h96s.grid(row=5, column=8)
h95s.grid(row=5, column=9)
h94s.grid(row=5, column=10)
h93s.grid(row=5, column=11)
h92s.grid(row=5, column=12, stick='we')

hA8o.grid(row=6, column=0, stick='we')
hK8o.grid(row=6, column=1)
hQ8o.grid(row=6, column=2)
hJ8o.grid(row=6, column=3)
hT8o.grid(row=6, column=4)
h98o.grid(row=6, column=5)
h88.grid(row=6, column=6, stick='we')
h87s.grid(row=6, column=7)
h86s.grid(row=6, column=8)
h85s.grid(row=6, column=9)
h84s.grid(row=6, column=10)
h83s.grid(row=6, column=11)
h82s.grid(row=6, column=12, stick='we')

hA7o.grid(row=7, column=0, stick='we')
hK7o.grid(row=7, column=1)
hQ7o.grid(row=7, column=2)
hJ7o.grid(row=7, column=3)
hT7o.grid(row=7, column=4)
h97o.grid(row=7, column=5)
h87o.grid(row=7, column=6, stick='we')
h77.grid(row=7, column=7)
h76s.grid(row=7, column=8)
h75s.grid(row=7, column=9)
h74s.grid(row=7, column=10)
h73s.grid(row=7, column=11)
h72s.grid(row=7, column=12, stick='we')

hA6o.grid(row=8, column=0, stick='we')
hK6o.grid(row=8, column=1)
hQ6o.grid(row=8, column=2)
hJ6o.grid(row=8, column=3)
hT6o.grid(row=8, column=4)
h96o.grid(row=8, column=5)
h86o.grid(row=8, column=6, stick='we')
h76o.grid(row=8, column=7)
h66.grid(row=8, column=8)
h65s.grid(row=8, column=9)
h64s.grid(row=8, column=10)
h63s.grid(row=8, column=11)
h62s.grid(row=8, column=12, stick='we')

hA5o.grid(row=9, column=0, stick='we')
hK5o.grid(row=9, column=1)
hQ5o.grid(row=9, column=2)
hJ5o.grid(row=9, column=3)
hT5o.grid(row=9, column=4)
h95o.grid(row=9, column=5)
h85o.grid(row=9, column=6, stick='we')
h75o.grid(row=9, column=7)
h65o.grid(row=9, column=8)
h55.grid(row=9, column=9)
h54s.grid(row=9, column=10)
h53s.grid(row=9, column=11)
h52s.grid(row=9, column=12, stick='we')

hA4o.grid(row=10, column=0, stick='we')
hK4o.grid(row=10, column=1)
hQ4o.grid(row=10, column=2)
hJ4o.grid(row=10, column=3)
hT4o.grid(row=10, column=4)
h94o.grid(row=10, column=5)
h84o.grid(row=10, column=6, stick='we')
h74o.grid(row=10, column=7)
h64o.grid(row=10, column=8)
h54o.grid(row=10, column=9)
h44.grid(row=10, column=10)
h43s.grid(row=10, column=11)
h42s.grid(row=10, column=12, stick='we')

hA3o.grid(row=11, column=0, stick='we')
hK3o.grid(row=11, column=1)
hQ3o.grid(row=11, column=2)
hJ3o.grid(row=11, column=3)
hT3o.grid(row=11, column=4)
h93o.grid(row=11, column=5)
h83o.grid(row=11, column=6, stick='we')
h73o.grid(row=11, column=7)
h63o.grid(row=11, column=8)
h53o.grid(row=11, column=9)
h43o.grid(row=11, column=10)
h33.grid(row=11, column=11)
h32s.grid(row=11, column=12, stick='we')

hA2o.grid(row=12, column=0, stick='we')
hK2o.grid(row=12, column=1)
hQ2o.grid(row=12, column=2)
hJ2o.grid(row=12, column=3)
hT2o.grid(row=12, column=4)
h92o.grid(row=12, column=5)
h82o.grid(row=12, column=6, stick='we')
h72o.grid(row=12, column=7)
h62o.grid(row=12, column=8)
h52o.grid(row=12, column=9)
h42o.grid(row=12, column=10)
h32o.grid(row=12, column=11)
h22.grid(row=12, column=12, stick='we')

# Кортеж, в котором находятся сигналы ранков рук.
# Обнуляет значения бэкграунда сигналов.
hands_signals_tuple = (hAA, hKK, hQQ, hJJ, hTT, h99, h88, h77, h66, h55, h44, h33, h22,
                       hAKs, hAQs, hAJs, hATs, hA9s, hA8s, hA7s, hA6s, hA5s, hA4s, hA3s, hA2s,
                       hKQs, hKJs, hKTs, hK9s, hK8s, hK7s, hK6s, hK5s, hK4s, hK3s, hK2s,
                       hQJs, hQTs, hQ9s, hQ8s, hQ7s, hQ6s, hQ5s, hQ4s, hQ3s, hQ2s,
                       hJTs, hJ9s, hJ8s, hJ7s, hJ6s, hJ5s, hJ4s, hJ3s, hJ2s,
                       hT9s, hT8s, hT7s, hT6s, hT5s, hT4s, hT3s, hT2s,
                       h98s, h97s, h96s, h95s, h94s, h93s, h92s,
                       h87s, h86s, h85s, h84s, h83s, h82s,
                       h76s, h75s, h74s, h73s, h72s,
                       h65s, h64s, h63s, h62s,
                       h54s, h53s, h52s,
                       h43s, h42s,
                       h32s,
                       hAKo, hAQo, hAJo, hATo, hA9o, hA8o, hA7o, hA6o, hA5o, hA4o, hA3o, hA2o,
                       hKQo, hKJo, hKTo, hK9o, hK8o, hK7o, hK6o, hK5o, hK4o, hK3o, hK2o,
                       hQJo, hQTo, hQ9o, hQ8o, hQ7o, hQ6o, hQ5o, hQ4o, hQ3o, hQ2o,
                       hJTo, hJ9o, hJ8o, hJ7o, hJ6o, hJ5o, hJ4o, hJ3o, hJ2o,
                       hT9o, hT8o, hT7o, hT6o, hT5o, hT4o, hT3o, hT2o,
                       h98o, h97o, h96o, h95o, h94o, h93o, h92o,
                       h87o, h86o, h85o, h84o, h83o, h82o,
                       h76o, h75o, h74o, h73o, h72o,
                       h65o, h64o, h63o, h62o,
                       h54o, h53o, h52o,
                       h43o, h42o,
                       h32o)

# Холст для отображения информации интерфейса.
interface_canvas = Canvas(console, bd=0, bg='#8B4513', height=230, highlightthickness=0)
interface_canvas.pack()

# Белая линия.
interface_canvas.create_line(0, 0, 382, 0, fill='white')

# Надписи в информационном табло интерфейса.
# n, ne, e, se, s, sw, w, nw, or center
label_style = ttk.Style()
label_style.configure('info.TLabel', background='#8B4513', foreground='white', font=('', 11, 'bold'))

co_label = ttk.Label(interface_canvas, style='info.TLabel', text='CO')
co_label.place(x=115, y=22, anchor='center')
btn_label = ttk.Label(interface_canvas, style='info.TLabel', text='BTN')
btn_label.place(x=185, y=22, anchor='center')
sb_label = ttk.Label(interface_canvas, style='info.TLabel', text='SB')
sb_label.place(x=255, y=22, anchor='center')
bb_label = ttk.Label(interface_canvas, style='info.TLabel', text='BB')
bb_label.place(x=325, y=22, anchor='center')
sit1_label = ttk.Label(interface_canvas, style='info.TLabel', text='open')
sit1_label.place(x=80, y=45, anchor='ne')
sit2_label = ttk.Label(interface_canvas, style='info.TLabel', text='vs co')
sit2_label.place(x=80, y=75, anchor='ne')
sit3_label = ttk.Label(interface_canvas, style='info.TLabel', text='vs btn')
sit3_label.place(x=80, y=105, anchor='ne')
sit4_label = ttk.Label(interface_canvas, style='info.TLabel', text='vs sb')
sit4_label.place(x=80, y=135, anchor='ne')
sit5_label = ttk.Label(interface_canvas, style='info.TLabel', text='vs co+')
sit5_label.place(x=80, y=165, anchor='ne')
sit6_label = ttk.Label(interface_canvas, style='info.TLabel', text='vs btn+sb')
sit6_label.place(x=80, y=195, anchor='ne')

# Радиокнопки.
rb_style = ttk.Style()
rb_style.configure('TRadiobutton', padding=0, background='#8B4513')

rb1 = ttk.Radiobutton(interface_canvas, style='TRadiobutton', variable=rb, value='1', command=rb_select)
rb1.place(x=120, y=55, anchor='center')
rb2 = ttk.Radiobutton(interface_canvas, style='TRadiobutton', variable=rb, value='2', command=rb_select)
rb2.place(x=190, y=55, anchor='center')
rb3 = ttk.Radiobutton(interface_canvas, style='TRadiobutton', variable=rb, value='3', command=rb_select)
rb3.place(x=260, y=55, anchor='center')
rb6 = ttk.Radiobutton(interface_canvas, style='TRadiobutton', variable=rb, value='6', command=rb_select)
rb6.place(x=190, y=85, anchor='center')
rb7 = ttk.Radiobutton(interface_canvas, style='TRadiobutton', variable=rb, value='7', command=rb_select)
rb7.place(x=260, y=85, anchor='center')
rb8 = ttk.Radiobutton(interface_canvas, style='TRadiobutton', variable=rb, value='8', command=rb_select)
rb8.place(x=330, y=85, anchor='center')
rb11 = ttk.Radiobutton(interface_canvas, style='TRadiobutton', variable=rb, value='11', command=rb_select)
rb11.place(x=260, y=115, anchor='center')
rb12 = ttk.Radiobutton(interface_canvas, style='TRadiobutton', variable=rb, value='12', command=rb_select)
rb12.place(x=330, y=115, anchor='center')
rb13 = ttk.Radiobutton(interface_canvas, style='TRadiobutton', variable=rb, value='13', command=rb_select)
rb13.place(x=330, y=145, anchor='center')
rb14 = ttk.Radiobutton(interface_canvas, style='TRadiobutton', variable=rb, value='14', command=rb_select)
rb14.place(x=260, y=175, anchor='center')
rb15 = ttk.Radiobutton(interface_canvas, style='TRadiobutton', variable=rb, value='15', command=rb_select)
rb15.place(x=330, y=175, anchor='center')
rb16 = ttk.Radiobutton(interface_canvas, style='TRadiobutton', variable=rb, value='16', command=rb_select)
rb16.place(x=330, y=205, anchor='center')

# Обязательный протокол завершения цикла tkinter.
console.mainloop()
