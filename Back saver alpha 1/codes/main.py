import tkinter as tk # Библеотека для общего работы окна
from threading import Thread # Библеотека для работы с процесами (когда работает окно основной поток блокнут, вызываю daemon потоки)
from time import sleep # Библеотека для того что бы while не нагружал пк
from PIL import ImageTk # Библеотека для создания кнопок с изображениями (временно вырезанная функция)
from tkinter import ttk # Библеотека для создания меню с выбором звуков
from playsound import playsound # Библеотека для проигрования звуков
from tkinter.messagebox import showinfo # (временная библеотка для показа почты для связи)
import shutil # Библеотека для копирования файлов(в документы и автозагрузку)
from pathlib import Path # Библеотека для узнавания пути в котором запущена программа
import getpass # Библеотека для того что бы узнать как зовут пользователя
import os # Библеотека для удаления, создавания и проверки наличия папок


USER_NAME = getpass.getuser()  # Узнаём как зовут пользователя
Documents_path = "C:\\Users\\" + str(USER_NAME) + "\\Documents\\Foraho apps\\back saver\\settings.txt" # Путь для сохранения настроек
current_dir = str(Path.cwd()) # Узнаём текущую директорию
autorun_path = 'C:\\Users\\' + str(USER_NAME) + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' # Путь для автозагрузки
email = 'Foraho.Official@gmail.com' # Почта разработчика
sound_select = 0 # Переменая служит для хранения значении о выборе звука для уведомления
minTime = 0 # Переменая для нижнего порого срабатывания рандома для вызова окна о разминке
maxTime = 0 # Переменая для верхнего порога срабатывания рандома для вызова окна о разминке
minutes = 0 # Переменая о выборе основого кол-во минут для срабатывания окна о разминке
version = str(0.1) + '   (alpha test)' # Версия приложения
win = tk.Tk()  # Переменная создания главного окна
h = 500  # Высота окна
w = 600  # Ширина окна
photo = tk.PhotoImage(file='data/images/logo.png')  # Импорт логотипа для окна приложения
win.iconphoto(False, photo)  # Настройка логотипа
win.config(bg='#e3e3e3')  # Цвет основного заднего фона окна приложения
win.title('Back saver  ' + str(version))  # Название окна приложения
win.geometry(f"{h}x{w}")  # Указание размеров окна (см. 19 и 20 строки)
win.resizable(False, False)  # Указание того что размеры окна нельзя будет изменить


# Функция для показа почты для связи
def show_email():
    showinfo(title="Почта для связи", message=email)


# Функция для показа периода срабатывания в реальном времени
def abc():
    while True: # После закрытия окна поток убивается (см. строку сверху)
        sleep(0.05) # Что бы while не нагружал систему
        minutes = scale_1.get() # Первоночальное кол-во выбора минут
        minTime = minutes - scale_2.get() # Минимальное значение кол-во выбора минут
        maxTime = minutes + scale_2.get() # Максимальное значение кол-во выбора минут
        if minTime < 0: minTime = 0 # Если минимальное значение меньше чем 0 то оно равно 0
        Text_3.config(text='Период рандомизации между: ' + str(minTime) + ' и ' + str(maxTime) + ' минут') # Вывод информации на окно (изменение текста)


# Сохранение настроек в файл
def work():
    if os.path.exists("C:\\Users\\" + str(USER_NAME) + "\\Documents\\Foraho apps") == False: os.mkdir("C:\\Users\\" + str(USER_NAME) + "\\Documents\\Foraho apps") # Создание папки для хранения данных о приложениях разработчика (Да, будут ещё приложения)
    if os.path.exists("C:\\Users\\" + str(USER_NAME) + "\\Documents\\Foraho apps\\Back saver") == False: os.mkdir("C:\\Users\\" + str(USER_NAME) + "\\Documents\\Foraho apps\\Back saver") # Создание папки для хранения данных о приложении
    if os.path.exists("C:\\Users\\" + str(USER_NAME) + "\\Documents\\Foraho apps\\Back saver\\music") == False: os.mkdir("C:\\Users\\" + str(USER_NAME) + "\\Documents\\Foraho apps\\Back saver\\music") # Создание папки для хранения музыки приложения
    current_dir = os.path.abspath(os.curdir) # Для узнавания текущей директории
    autorun_path = "C:\\Users\\" + str(USER_NAME) + "\\Documents\\Foraho apps\\Back saver\\music" # Папка куда сохраняется музыка приложения
    i = 0 # см строку 59
    while i < 6: # Перенос всей музыки в документы по штучно
        i+=1
        shutil.copy2(current_dir + str('\\data\\Sounds\\Sound ' + str(i) + '.mp3'), autorun_path) # Копирование в документы из текущей директории
    minutes = scale_1.get() # Первоночальное кол-во выбора минут
    minTime = minutes - scale_2.get() # Минимальное значение кол-во выбора минут
    maxTime = minutes + scale_2.get() # Максимальное значение кол-во выбора минут
    if minTime < 1: minTime = 0 # Если минимальное значение меньше чем 0 то оно равно 0
    lines = [str(minTime), str(maxTime), str(not_sou_agr.get()), str(autrun_agree.get()), str(combobox_1.current() + 1)] # Данные которые записываются в настройки
    with open(Documents_path, "w") as file: # Запись выбранных настроек построчно
        for line in lines:
            file.write(line + '\n') # Запись значения и перенос строки
    file.close() # Завершение работы с файлом (сохранение изменений в нём)
    if autrun_agree.get(): # Если автозагрузка включена то копирование в автозагрузку
        autorun_path = 'C:\\Users\\' + str(USER_NAME) + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' # Путь автозагрузки
        shutil.copy2(current_dir + '\\work.exe', autorun_path) # Копирование
    elif autrun_agree.get() == False: # Если автозагрузка выключена то файл удаляется
        if os.path.exists('C:\\Users\\' + str(USER_NAME) + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\work.exe') == True: os.remove('C:\\Users\\' + str(USER_NAME) + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' + '\\work.exe') # Если файл есть то удаляется, иначе скип


# Проигрование звука (см. функцию ниже)
def play_sound():
    i = combobox_1.current() + 1 # Получение текущего выбора звука
    playsound('data/sounds/Sound ' + str(i) + '.mp3') # проигрование звука из предустановленых

def sound(): # Проигрование звука при выборе
    while True:
        sleep(0.01) # Что бы while true не грузил пк
        global sound_select # получение глобального значения для отслеживания изменений
        if sound_select != combobox_1.current(): # Если значение переменной отлично от текущего (происходит при выборе другого звука)
            thread_2 = Thread(target=play_sound, daemon=True) # Создание паралейного потока для проигрования звука без остановки работы основной програмы (иначе во время воспроизведения звука программа не работает)
            thread_2.start() # Запуск потока
            sound_select = combobox_1.current() # Обновление значения переменой на текущий выбор


            ##############  Графическая часть  ##############


mainmenu = tk.Menu(win) # Создание верхнего меню с пунктамии
win.config(menu=mainmenu) # Создание верхнего меню
mainmenu.add_command(label='Связь с разработчиком', command=show_email) # Один из пунктов меню (при нажатии показыввет почту разработчика(см. строку 36))
mainmenu.add_command(label='Отзыв', command=show_email) # Один из пунктов меню (пока неактивно)


# Пустышка
Text_1 = tk.Label(win, text='Введите время напоминания (в минутах):', bg='#e3e3e3', font = ('Arial', 14), fg=('#e3e3e3'), width=100, anchor='w', justify=tk.LEFT) # Вывод текста с цветом под фон для создания отступа сверху (костыль)
Text_1.pack() # Запуск первой надписи


Text_1 = tk.Label(win, text='Введите время напоминания (в минутах):', bg='#e3e3e3', font = ('Arial', 14), width=100, anchor='w', justify=tk.LEFT) # Вывод первой надписи
Text_1.pack() # Расположение элемента на окне (включение отображения)


scale_1 = tk.Scale(win, bg='#e3e3e3', orient='horizontal', from_=20, to=180, length=480) # Ползунок выбора минут
scale_1.pack() # Расположение элемента на окне (включение отображения)


Text_2 = tk.Label(win, text='Введите время рандомизации (в минутах):', bg='#e3e3e3', font = ('Arial', 14), width=100, anchor='w', justify=tk.LEFT) # Вывод второй надписи
Text_2.pack() # Расположение элемента на окне (включение отображения)


scale_2 = tk.Scale(win, bg='#e3e3e3', orient='horizontal', from_=0, to=80, length=480) # Ползунок выбора минут
scale_2.pack() # Расположение элемента на окне (включение отображения)


Text_3 = tk.Label(win, text='', bg='#e3e3e3', font = ('Arial', 12), width=100, anchor='n', justify=tk.LEFT) # текст для показа разброса рандомизации в минутах (см. строку 41,48)
Text_3.pack() # Расположение элемента на окне (включение отображения)


# Пустышка
Text_4 = tk.Label(win, text='Введите время напоминания (в минутах):', bg='#e3e3e3', font = ('Arial', 14), fg=('#e3e3e3'), width=100, anchor='w', justify=tk.LEFT, pady=1) # Вывод текста с цветом под фон для создания отступа сверху (костыль)
Text_4.pack() # Расположение элемента на окне (включение отображения)


Text_5 = tk.Label(win, text='Выберите желаемые пункты: ', bg='#e3e3e3', font = ('Arial', 14), width=100, anchor='w', justify=tk.LEFT) # Вывод текста о выборе пунктов
Text_5.pack() # Расположение элемента на окне (включение отображения)


not_sou_agr = tk.BooleanVar() # Создание перменой bool о значении данного пункта
notification_sound_agree = tk.Checkbutton(win, text='Включить звук напоминания', anchor='nw', bg='#e3e3e3', justify=tk.LEFT, variable=not_sou_agr, width=200) # Пункт о звуке уведомлений
notification_sound_agree.pack() # Расположение элемента на окне (включение отображения)

# (Временно вырезано)
# not_agr = tk.BooleanVar() # Создание перменой bool о значении данного пункта
# notification_agree = tk.Checkbutton(win, text='Включить уведомления', anchor='nw', bg='#e3e3e3', justify=tk.LEFT, variable=not_agr, width=200) # Пункт об показа уведомления
# notification_agree.pack() # Расположение элемента на окне (включение отображения)

autrun_agree = tk.BooleanVar() # Создание перменой bool о значении данного пункта
autorun_agree = tk.Checkbutton(win, text='Включить автозапуск вместе с windows', anchor='w', bg='#e3e3e3', justify=tk.LEFT, variable=autrun_agree, width=200) # Пункт о автозапуске
autorun_agree.pack() # Расположение элемента на окне (включение отображения)


# Пустышка
Text_1 = tk.Label(win, text='Введите время напоминания (в минутах):', bg='#e3e3e3', font = ('Arial', 14), fg=('#e3e3e3'), width=100, anchor='w', justify=tk.LEFT, pady=10) # Вывод текста с цветом под фон для создания отступа сверху (костыль)
Text_1.pack() # Расположение элемента на окне (включение отображения)

Text_5 = tk.Label(win, text='Выберите звук уведомлений: ', bg='#e3e3e3', font = ('Arial', 14), width=100, anchor='w', justify=tk.LEFT) # Текст о выборе звука для уведомлений
Text_5.pack() # Расположение элемента на окне (включение отображения)


list = ('Звук 1','Звук 2','Звук 3','Звук 4','Звук 5','Звук 6') # Названия для звуков
combobox_1 = ttk.Combobox(win, values = list, justify=tk.LEFT) # Создание меню с пунктами выбора
combobox_1.current(0) # Установление текущего значения на меню на [0]
combobox_1.pack() # Расположение элемента на окне (включение отображения)


# Пустышка
Text_1 = tk.Label(win, text='Введите время напоминания (в минутах):', bg='#e3e3e3', font = ('Arial', 14), fg=('#e3e3e3'), width=100, anchor='w', justify=tk.LEFT, pady=20) # Вывод текста с цветом под фон для создания отступа сверху (костыль)
Text_1.pack() # Расположение элемента на окне (включение отображения)


# кнопка обработки событий
Text_2 = tk.Button(win, text='готово', command=work) # Кнопка о завершении всех настроек и по нажатию на неё сохранение данных в файл (см. строка 52)
Text_2.pack() # Расположение элемента на окне (включение отображения)



thread_1 = Thread(target=sound, daemon=True) # Создание потока для проигрывания и воспроизведения звукоа при выборе (см. строку 88)
thread_1.start() # Запуск потока

thread_3 = Thread(target=abc, daemon=True) # Создание потока для изменения периодов срабатывания напоминания (см. строку 41)
thread_3.start() # Запуск потока


win.mainloop() # Запуск окна приложения