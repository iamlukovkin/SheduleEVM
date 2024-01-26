from .models import *
from .connection import *
from sqlalchemy import text

def add_lessons(lessons: list[dict]):
    """Add lessons to database."""
    with get_connection() as conn:
        conn.execute(Lesson.__table__.delete())
        for lesson in lessons:
            conn.execute(Lesson.__table__.insert().values(
                group=lesson['group'], 
                day=lesson['day'],
                time=lesson['time'], 
                week=lesson['week'], 
                lesson=lesson['lesson']
            ))
            conn.commit()


def get_tutor_variants(tutor: str):
    tutor_array = tutor.split(' ')
    if len(tutor_array) == 3:
        _formats = [
            f'{tutor_array[0]} {tutor_array[1][0]}.{tutor_array[2][0]}.',
            f'{tutor_array[0]} {tutor_array[1][0]}. {tutor_array[2][0]}.',
            f'{tutor_array[0]} {tutor_array[1]} {tutor_array[2]}',
        ]
    elif len(tutor_array) == 2:
        _formats = [f'{tutor_array[0]} {tutor_array[1]}']
    else:
        _formats = [f'{tutor_array[0]}']
    return _formats


def get_matrix_with_times(tutor_formats: list, session):
    _days: list[str] = [
        'Понедельник', 'Вторник', 'Среда', 
        'Четверг', 'Пятница', 'Суббота'
    ]
    temp: list = []
    for day in _days:
        day_times: set = set()
        for week in ['Числитель', 'Знаменатель']:
            for _tutor in tutor_formats:
                times = session.query(Lesson.time).distinct().filter_by(
                    day=day, week=week).filter(
                        Lesson.lesson.like(f'%{_tutor}%')
                ).order_by(Lesson.time.asc()).all()
                for time in times:
                    if time[0] not in day_times:
                        day_times.add(time[0])
        _times: list = list(day_times)
        _times.sort()
        for time in _times: temp.append([time, day])
        
    return temp


def get_tutor_matrix(tutor: str):
    """Get tutor matrix."""
    session = get_session()
    tutor_formats: list[str] = get_tutor_variants(tutor)
    matrix = get_matrix_with_times(tutor_formats, session)
    for row in matrix:
        for week in ['Числитель', 'Знаменатель']:
            result = None
            for tutor in tutor_formats:
                search = f'%{tutor.split(" ")[0]}%'
                result = session.query(Lesson).filter_by(
                    time=row[0], day=row[1], week=week
                ).filter(Lesson.lesson.like(f'%{search}%')).first()
            if result is not None:
                row.append(f'({result.get_group()}) {result.lesson}')
            else:
                row.append(None)
    matrix.insert(0, ['Время', 'День', 'Числитель', 'Знаменатель'])
    session.close()
    return matrix, tutor_formats[0]
                    
                
