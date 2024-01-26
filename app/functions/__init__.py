"""Open folder with schedule"""

import os
import subprocess
import config
from interface import my_app
import tkinter as tk
from .downloading_files import download_graphs

def open_folder():
    """Open folder with schedule"""
    folder_path = config.FOLDERS['Shedule']
    subprocess.run(["open", folder_path])


def exit_app():
    """Exit the application"""
    my_app.close()
    exit()


def download_tables():
    """Download tables from https://rsreu.ru/studentu/raspisanie-zanyatij"""
    for file in os.listdir(config.FOLDERS['Shedule']):
        os.remove(os.path.join(config.FOLDERS['Shedule'], file))
    download_graphs(config.FOLDERS['Shedule'])
    popup: tk.Toplevel = tk.Toplevel()
    popup.title(config.APP_SHORT_NAME)
    popup.geometry('200x100')
    popup.resizable(width=False, height=False)
    label: tk.Label = tk.Label(popup, text='Успешно!')
    button: tk.Button = tk.Button(popup, text='Закрыть', command=popup.destroy)
    label.pack()
    button.pack()


update_database: callable = lambda: print('Обновить базу данных')