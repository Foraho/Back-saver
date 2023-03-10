from random import randint # Библеотека для рандомизации времени срабатывания окна (см. строку 51)
from time import sleep # Библеотека для приостановления программы на рандомный промежуток времени (см. строки 1 и 36,51)
import tkinter # Библеотека для общего работы окна
from threading import Thread # Библеотека для работы с процесами (когда работает окно основной поток блокнут, вызываю daemon потоки)
from playsound import playsound # Библеотека для проигрования звуков
import getpass # Библеотека для того что бы узнать как зовут пользователя


USER_NAME = getpass.getuser() # Узнаём как зовут пользователя
mess = False  # Переменная о том запущено ли в данный момент окно (для воспроизведения звука)
text = 'Встань и сделай разминку на 1 минуту' # Текст о побуждении к действию (в будущем будет больше)
h = 300  # Ширина окна
w = 100  # Высота окна

# Перезапуск окна после закрытия
def start():
    global win # Данная строка позволяет запускать окно после каждого его закрытия
    win = tkinter.Tk()  # Переменная создания главного окна
    win.config(bg='#e3e3e3')  # Цвет основного заднего фона окна приложения
    win.title('Пора размятся!')  # Название окна приложения
    win.geometry(f"{h}x{w}")  # Указание размеров окна (см. 12 и 13 строки)
    win.resizable(False, False)  # Указание того что размеры окна нельзя будет изменить

# Функция которая позволяет закрыть окно при её вызове
def leave():
    win.destroy()

# Чтение файла построчно
with open("C:\\Users\\" + getpass.getuser() + "\\Documents\\Foraho apps\\Back saver\\settings.txt", "r") as f:
    settings = f.readlines() # Содержимое файла с настройками

# Проигрование звука при выборе
def play_sound():
    global mess # Глобальное чтение/изменение переменной
    while True:
        sleep(0.05) # Пауза что бы ПК не взорвался
        while mess: # Когда появлется сообщение (см. 66 строку)
            if settings[2].translate(str.maketrans("", "", '\n')) == 'True': # Если 3 строка true то звук будет, иначе нет
                # Проигрование звука из предустановленых
                playsound(("C:\\Users\\" + getpass.getuser() + "\\Documents\\Foraho apps\\Back saver\\music/Sound " + str(settings[4]) + ".mp3").translate(str.maketrans("", "", '\n')))
            mess = False # Возращение false для одного звучания звука


start() # Необходимо для запуска окна раз за разом полсе его закрытия

thread_1 = Thread(target=play_sound, daemon=True) # Создание потока для проигрывания и воспроизведения звука при выборе (см. строки 33 и 66)
thread_1.start()  # Запуск потока

while True:
    # Первые 2 значения из настроек являются промежутками для рандомного вызова окна (см. 30 строку)
    sleep(randint(int(settings[0]) * 60, int(settings[1]) * 60))

    # Текст с побуждением к разминке
    Text_1 = tkinter.Label(win, text=text, bg='#e3e3e3', font=('Arial', 10), fg=('black'), anchor='sw', pady=10)
    Text_1.pack() # "Включение" этого текста в окно

    # Переменная для составления расстояния между текстом и кнопкой, цвет фона и текста одинаковый (т.е. костыль)
    Text_1 = tkinter.Label(win, text=text, bg='#e3e3e3', font=('Arial', 7), fg=('#e3e3e3'), anchor='sw',)
    Text_1.pack() # "Включение" этого текста в окно

    # Кнопка для подтверждения разминки и перезапуска программы
    Text_2 = tkinter.Button(win, text='Размялся, спасибо!', command=leave)
    Text_2.pack() # "Включение" этой кнопки в окно


    mess = True # Для воспроизведения звука
    win.mainloop() # Ожидание закрытия программы через крестик
    start() # Перезапуск программы (см. строку 20)