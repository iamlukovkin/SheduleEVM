"""Main page of application on start."""
from interface import *
from functions import *


def buttons_widget() -> Frame:
    """Create a widget with functional buttons."""
    _frame: Frame = Frame()
    _frame_width: int = my_app.width * (1 - 0.2)
    _frame_height: int = my_app.height * (1 - 0.2)
    _frame.set_resolution(_frame_width, _frame_height)
    _frame.place(x=my_app.width * 0.1, y=my_app.height * 0.1)

    _functions: dict[str, list[str, callable]] = {
        'OpenFolder': [
            'Открыть папку с расписаниями', 
            open_folder
        ],
        'DownloadTables': [
            'Скачать таблицы расписания', 
            download_tables
        ],
        'UpdateDatabase': [
            'Обновить базу данных',
            update_database
        ],
        'MakeSchedule': [
            'Составить расписание',
            get_tutor_name
        ],
        'Exit': [
            'Выход',
            exit_app
        ],
    }

    margin: int = my_app.height * 0.05
    button_height: int = margin * 1
    buttons_length: int = len(_functions) * button_height
    buttons_length += margin * (len(_functions) - 1)
    _place_shelf: int = (_frame_height - buttons_length) // 2

    for _func in _functions.keys():
        _button: Button = Button(_frame)
        _button.config(
            text=_functions[_func][0],
            command=_functions[_func][1]
        )
        _button.place(
            anchor='center', x=_frame_width // 2, 
            y=_place_shelf
        )
        _place_shelf += button_height + margin


def main() -> None:
    """Show the main page of application."""
    main_page: Frame = buttons_widget()
