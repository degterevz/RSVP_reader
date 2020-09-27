# -*- coding: utf-8 -*-
from Menu import *
from TextFrame import *
from ControlPanelFrame import *
from StatFrame import *

sample_data = '''
В университете Карнеги — Меллона велись исследования технологии RSVP, когда информация (изображение, текст) показывается 
человеку кадрами небольшого размера, чтобы свести к минимуму движения глаз при просмотре этого кадра. Например, когда мы 
читаем, мы вынуждены следить за словом в рамках одной строки и за строкой, перемещаясь по странице. Э
тот навык вырабатывается в начальной школе. Именно из-за сложности читать большие строки энциклопедические издания 
большого формата, газеты и журналы верстаются в несколько узких колонок.
Опыты показали, что если не двигать глаза во время чтения и смотреть, получая кадры, в одну точку, 
можно после определенной тренировки увеличить без потери смысла скорость с 250 wpm 
(слов в минуту, комфортное чтение среднего взрослого человека) до 600-750 wpm, иногда до 1000 wpm. 
Подчеркну, без потери смысла, а то будет как в анекдоте про печать 1200 символов в минуту...
Дальнейшее увеличение скорости приводит к пропускам и эквивалентно просто просматриванию книги взглядом наискосок.
Со временем компания Spritz на основе разных исследований сделала набор приложений, 
позволяющий читать статьи и книги, используя RSVP.
Особое внимание они уделили ORP -- оптимальной точке распознавания (подсвечивается красным).
Естественно, у метода есть ограничения. Нельзя с его помощью читать научные статьи по матанализу. 
А вот новости и художественную литературу -- очень даже. При этом чем больше вы будете расслаблены, тем лучше, 
а через некоторое время вы сможете буквально перейти в режим кинотеатра, представляя образы произведения у себя в голове
RSVP активно исследуется. Например, вот статья, где пытаются сделать набор символов с помощью нейроинтерфейса, 
показывая в случайном порядке при помощи RSVP буквы алфавита + пробел. Вы фокусируетесь на нужной, 
и тем самым печатаете следующую букву. Прочтите. Прям очень интересно.
Этой штукой мог бы пользоваться Стивен Хокинг.
'''


class GlobalVariables:
    """
    Класс глобальных переменных -- через них различные модули общаются с друг другом.
    Не знаю, насколько это удачный подход, опыта констурирования относительно сложных и объемных
    архитектур у меня еще не было, но хотелось убрать кашу обращений модулей друг к другу,
    сделать их более независимыми и целостными.
    """

    def __init__(self):
        self.width = 900
        self.height = 300

        self.ind = -1
        self.status = 'stop'
        self.status_stack = None
        self.wpm = 100
        self.step_wpm = 10
        self.pause_sentence = 800

        self.data = str()
        self.words = list()
        self.size = 0

        self.history = dict()
        self.file_name = 'sample_data'

    def new_data(self, data_):
        self.data = data_
        self.words = self.data.split()
        self.size = len(self.words)
        self.ind = GV.history.get(GV.file_name, 0)

        next_frame()


# Возвращает по длине слова два значения:
# 1) номер буквы, на который центируем слово
# 2) задержку после слово в мс
def optimal_n(len_word):
    if len_word <= 1:
        return 1, 0
    elif 1 < len_word < 6:
        return 2, 0
    elif 5 < len_word < 10:
        return 3, 100
    elif 9 < len_word < 14:
        return 4, 250
    else:
        return 5, 400


# Функция 'next_frame' взаимодействует с модулями и при необходимости их обновляет.
def next_frame():
    if GV.ind < GV.size:
        # обновляем статус-бар
        stat.update_bar()

        # обновляем слово
        n, pause_len = optimal_n(len(GV.words[GV.ind]))
        text.update(n)
        GV.history[GV.file_name] = GV.ind

        # переход с следующему кадру
        if GV.status == 'play':
            GV.ind += 1

            # если конец предложения -- делаем дополнительную паузу 'GV.pause_sentence'
            if GV.words[GV.ind - 1][-1] in ['.', '!', '?']:
                GV.status_stack = root.after(int(60 / GV.wpm * 1000) + int(GV.pause_sentence), next_frame)
            else:
                GV.status_stack = root.after(int(60 / GV.wpm * 1000) + pause_len, next_frame)

    else:
        GV.status = 'play'
        panel.playback()


GV = GlobalVariables()

root = tk.Tk()
root.title("RSVP reader")
root.geometry(f'{GV.width}x{GV.height}')
root.configure(background='white')

menu = Menu(root, GV)

# общий фрейм для текста и кнопок для удобства размещения
text_panel_frame = tk.Frame(root, background='white')
text = TextFrame(text_panel_frame, GV)
panel = ControlPanelFrame(text_panel_frame, GV, next_frame)
text.pack(anchor='c', pady=10)
panel.pack(anchor='c', side='top')
text_panel_frame.pack(expand=1, fill='x', anchor='c')

stat = StatFrame(root, GV)
stat.pack(fill='x', side='bottom')

GV.new_data(sample_data)

root.bind('<Key>', panel.keypress)
root.mainloop()
