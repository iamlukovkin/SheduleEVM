"""Launch the application."""

from interface import my_app
from pages import main_page
import database

def main():
    main_page()
    my_app.show()


if __name__ == '__main__':
    main()