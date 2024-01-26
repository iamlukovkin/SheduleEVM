"""Create notification"""

import tkinter as tk
import config


def send_notification(message_text: str):
    """Create notification"""
    popup: tk.Toplevel = tk.Toplevel()
    popup.title(config.APP_SHORT_NAME)
    # popup.geometry('200x100')
    popup.resizable(width=False, height=False)
    label: tk.Label = tk.Label(popup, text=message_text)
    button: tk.Button = tk.Button(popup, text='Закрыть', command=popup.destroy)
    label.pack()
    button.pack()