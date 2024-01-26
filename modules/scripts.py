import zipfile
import os
import config.settings as settings

from database.models import Lesson
from database.connection import engine
from app.functions.downloading_files import download_graphs
from app.functions.parsing_tables import refresh_graphs


import config.settings as settings


def update_lessons_site():
    """
    Updates site with new data.
    
    Returns:
        bool: True if site updated successfully.
    """
    source_tables = settings.DIRECTORIES['EXCEL_LESSONS_DIR']
    if settings.APP['MODE'] == 'dev':
        download_graphs(source_tables, 
            archive=True, archive_dst=settings.FILE_PATHS['LESSONS_ZIP'])
    else:
        archive_path = settings.FILE_PATHS['LESSONS_ZIP'] + '.zip'
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(settings.DIRECTORIES['EXCEL_LESSONS_DIR'])
        os.remove(archive_path)
    lessons = refresh_graphs(directory=source_tables)
    with engine.connect() as conn:
        conn.execute(Lesson.__table__.delete())
        conn.commit()
    counter = 0
    for lesson in lessons:
        try:
            with engine.connect() as conn:
                conn.execute(Lesson.__table__.insert().values(
                    group='gr_' + str(lesson[0]), day=lesson[1],
                    time=lesson[2], week=lesson[3], lesson=lesson[4]
                ))
                conn.commit()
        except:
            counter += 1
            continue
    return counter, len(lessons)
