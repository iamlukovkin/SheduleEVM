import os
import re
import requests
from bs4 import BeautifulSoup


sources: list[str] = [
    'http://rsreu.ru/magistrantu/raspisanie-zanyatij',
    'http://rsreu.ru/studentu/raspisanie-zanyatij'
]


def download_tables(dst: str):
    for source in sources:
        url = source
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        require = soup.find_all('a', href=re.compile('/component/docman/doc_download/'))
        for req in require:
            if req.find('span', class_='docman xls'):
                url = 'https://rsreu.ru' + req['href']
                response = requests.get(url)
                filename = req.get('href').split('/')[-1] + '.xlsx'
                path = dst + filename
                with open(path, 'wb') as f:
                    f.write(response.content)


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
            path = dst + filename
            with open(path, 'wb') as f:
                f.write(response.content)
    if archive:
        import shutil
        shutil.make_archive(archive_dst, 'zip', dst)
        for file in os.listdir(dst):
            os.remove(dst + file)
    return True
