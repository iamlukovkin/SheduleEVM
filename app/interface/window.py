"""Class for window of app."""

import tkinter as tk

from config import *


class Window(tk.Tk):
    """Main window of application"""
    def __init__(self) -> None:
        """Construct the window."""
        super().__init__()
        self.title(APP_NAME)
        self.width: int = APP_RESOLUTION['X']
        self.height: int = APP_RESOLUTION['Y']
        self.color: str = "#FFFFFF"
        self.configure(width=self.width, height=self.height)
        self.resizable(width=False, height=False)
        self.iconphoto(False, tk.PhotoImage(file=APP_ICON))
    
    def show(self) -> None:
        """Show the window."""
        self.mainloop()

    def close(self) -> None:
        """Close the window."""
        self.destroy()


my_app: Window = Window()
