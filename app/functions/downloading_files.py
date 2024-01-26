import os
import re
import requests
from bs4 import BeautifulSoup


# исключенные названия файлов
excluded_files = ['vecherniki', 'zaochniki', '011']


def download_graphs(
    dst: str, 
    archive: bool = False, 
    archive_dst: str = None
):
    """
    Downloads files from https://rsreu.ru/studentu/raspisanie-zanyatij

    Args:
        dst (str): destination path

    Returns:
        bool: True if files downloaded successfully.
    """
    url = "https://rsreu.ru/studentu/raspisanie-zanyatij"  
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    require = soup.find_all('a', href=re.compile('/component/docman/doc_download/'))
    for req in require:
        if req.find('span', class_='docman xls'):
            url = 'https://rsreu.ru' + req['href']
            response = requests.get(url)
            filename = req.get('href').split('/')[-1] + '.xlsx'
            if (any(excluded_file in filename for excluded_file in excluded_files)):
                continue
            path = dst + filename
            with open(path, 'wb') as f:
                f.write(response.content)
    if archive:
        import shutil
        shutil.make_archive(archive_dst, 'zip', dst)
        for file in os.listdir(dst):
            os.remove(dst + file)
    return True
