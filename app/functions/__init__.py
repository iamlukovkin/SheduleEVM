"""Open folder with schedule"""

import os
import subprocess
import config
import database
import tkinter as tk

from interface import *
from .downloading_files import download_tables as download_all_tables
from .parsing_tables import refresh_graphs
from .create_table import *

def open_folder():
    """Open folder with schedule"""
    folder_path = config.FOLDERS['MainSheedule']
    subprocess.run(["open", folder_path])


def exit_app():
    """Exit the application"""
    my_app.close()
    database.close_connection()
    exit()


def download_tables():
    """Download tables from https://rsreu.ru/studentu/raspisanie-zanyatij"""
    for file in os.listdir(config.FOLDERS['Shedule']):
        os.remove(os.path.join(config.FOLDERS['Shedule'], file))
    download_all_tables(config.FOLDERS['Shedule'])
   

def update_database():
    """Update database"""
    # download_tables()
    lessons: list[dict[str, str]] = refresh_graphs(config.FOLDERS['Shedule'])
    database.add_lessons(lessons)
    send_notification(f'База обновлена. Добавлено {len(lessons)} занятий.')


def get_tutor_name():
    input_dialog = tk.Toplevel(my_app)
    input_label = tk.Label(input_dialog, text="Введите ФИО преподавателя (полностью):")
    input_label.pack()
    user_entry = tk.Entry(input_dialog)
    user_entry.pack()
    submit_button = tk.Button(
        input_dialog, text="Submit", 
        command=lambda: process_user_input(user_entry.get(), input_dialog, searchParam='tutor')
    )
    submit_button.pack()
    

def get_group_name():
    input_dialog = tk.Toplevel(my_app)
    input_label = tk.Label(input_dialog, text="Введите номер группы:")
    input_label.pack()
    user_entry = tk.Entry(input_dialog)
    user_entry.pack()
    submit_button = tk.Button(
        input_dialog, text="Submit", 
        command=lambda: process_user_input(user_entry.get(), input_dialog, searchParam='group')
    )
    submit_button.pack()


def process_user_input(data, input_dialog, searchParam: str = 'tutor'):
    if data:
        make_schedule(data, searchParam)
        send_notification(f'Расписание создано.')
    else:
        send_notification(f'Не указано ФИО преподавателя.')
    input_dialog.destroy()


def make_schedule(argument: str, searchParam: str = 'tutor'):
    if searchParam == 'tutor':
        matrix, tutor_formated = database.get_tutor_matrix(argument)
        dst_path: str = config.FOLDERS['TutorSheedule'] + \
            tutor_formated + ' (расписание).xlsx'
    else:
        print(argument)
        matrix = database.get_group_matrix(argument)
        dst_path: str = config.FOLDERS['TutorSheedule'] + \
            str(argument) + ' (расписание).xlsx'
    if matrix is None:
        send_notification(f'Не удалось получить расписание.\nПроверьте правильность написания ФИО.')
        return
    elif not matrix:
        send_notification(f'Расписание для заданного параметра отсутствует.')
        return
    create_table(dst_path, matrix)
