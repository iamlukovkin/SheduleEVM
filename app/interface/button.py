"""A class of buttons inside a window of application."""

import tkinter as tk
from .frame import Frame


class Button(tk.Button):
    """Configurate buttons inside a window of application."""

    def __init__(self, parent_frame: Frame):
        """Construct the button."""
        super().__init__(master=parent_frame)
        
        self.width: int = 10
        self.height: int = 10
        self.bg_color: str = '#FF0000'
        self.color: str = self.bg_color
        parent_frame.configure(
            highlightthickness=0,
            highlightbackground=self.bg_color,
            bd=0,
            borderwidth=0
        )

    
    def set_size(self, width: int, height: int):
        """
        Set size of button
        
        Args:
            width (int): width of button
            height (int): height of button
        
        Returns:
            None
        """
        self.width = width
        self.height = height
        self.configure(width=self.width, height=self.height)

    def get_size(self) -> dict[str, int]:
        """
        Get size of button
        
        Returns:
            dict: {'X': width, 'Y': height}
        """
        return {'X': self.width,  'Y': self.height}

    def set_background(self, bg_color: str):
        """
        Set background of button
        
        Args:
            bg_color (str): color of background in hex
        
        Returns:
            None
        """
        self.bg_color = bg_color
        self.configure(bg=bg_color)
    
    def get_background(self) -> str:
        """
        Get background of button
        
        Returns:
            str: color of background in hex
        """
        return self.bg_color

    def set_color(self, color: str) -> None:
        """
        Set color of button.
        
        Args:
            color (str): color of button in hex

        Returns:
            None
        """
        self.color = color
        self.configure(bg=self.color)