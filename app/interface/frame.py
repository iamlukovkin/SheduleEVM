"""A class of frames inside a window of application."""

import tkinter as tk
from config import *


class Frame(tk.Frame):
    """A class of frame inside application"""
    def __init__(self):
        """A constructor for new frame"""
        super().__init__()
        self.width = APP_RESOLUTION['X']
        self.height = APP_RESOLUTION['Y']
        self.color = "#FFFFFF"

    def set_resolution(self, width: int, height: int, ):
        """
        Set resolution of frame
        
        Args:
            height (int): height of frame
            width (int): width of frame
            
        Returns:
            None
        """
        self.width = width
        self.height = height
        self.configure(width=self.width, height=self.height)

    def get_resolution(self) -> dict[str, int]:
        """
        Get resolution of frame
        
        Returns:
            dict: {'X': width, 'Y': height}
        """
        return {'X': self.width,  'Y': self.height}

    def set_background(self, color: str):
        """
        Set background of frame
        
        Args:
            color (str): color of background in hex
            
        Returns:
            None
        """
        self.color = color
        self.configure(bg=color)
    
    def get_background(self) -> str:
        """
        Get background of frame
        
        Returns:
            str: color of background in hex
        """
        return self.color
