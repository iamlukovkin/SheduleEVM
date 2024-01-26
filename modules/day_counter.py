from math import fabs

import datetime
from config.settings import CONSTANTS

def week_today():
    """
    Counts week today.

    Returns:
        str: week today
    """
    today = datetime.datetime.now()
    event = CONSTANTS['EVENT_DATE']
    diff = (today.date() - event.date()).days
    week_numb = fabs(diff // 7)
    if week_numb % 2 == 0:
        week = 'Числитель'
    else:
        week = 'Знаменатель'
    return week


def week_tomorrow():
    """
    Counts week tomorrow.

    Returns:
        str: week tomorrow
    """
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    event = CONSTANTS['EVENT_DATE']
    diff = (tomorrow.date() - event.date()).days
    week_numb = fabs(diff // 7)
    if week_numb % 2 == 0:
        week = 'Числитель'
    else:
        week = 'Знаменатель'
    return week


def day_of_week():
    """
    Counts day of the week.

    Args:
        day (str): day of the week

    Returns:
        int: day of the week
    """
    today = datetime.datetime.now()
    
    day = today.weekday().as_integer_ratio()[0]
    days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    day_today = days[day]
    return day_today


def day_tomorrow():
    """
    Counts day tomorrow.

    Returns:
        str: day tomorrow
    """
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    day = tomorrow.weekday().as_integer_ratio()[0]
    days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    day_tomorrow = days[day]
    return day_tomorrow

