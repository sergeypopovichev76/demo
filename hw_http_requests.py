# -*- coding: utf-8 -*-
import requests


class YaUploader:
    # Запрос URL для загрузки:
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        """Метод загрузки заголовков"""
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'}

    @property
    def header(self):
        return self.get_headers()

    def _get_upload_link(self, file_path: str):
        """Метод запрашивает ссылку для загрузки"""
        params = {'path': file_path, 'overwrite': 'true'}
        responce = requests.get(self.upload_url, params=params, headers=self.header)
        return responce.json()

    def upload(self, file_path: str):
        """Метод загружает файл на яндекс диск"""
        href = self._get_upload_link(file_path).get('href')

        if not href:
            return False
        if href:
            responce = requests.put(href, data=open(file_path, 'rb'))
            if responce.status_code == 201:
                print('Файл загружен')
                return True

    def upload_list_file(self, file_list: list):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for i in file_list:
            self.upload(f'{i}')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите путь к загружаемому файлу:')
    token = input('Введите токен:')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
