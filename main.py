import requests
from settings import TOKEN


class YaUploader:

    def __init__(self, token: str):
        self.token = token
        self.HOST = 'https://cloud-api.yandex.net/'

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def upload(self, path_to_file):
        uri = 'v1/disk/resources/upload'
        url = self.HOST + uri
        file_name = path_to_file.split("\\")[-1]
        params = {'path': file_name, 'overwrite': 'true'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        upload_link = response.json()['href']
        print(upload_link)
        resp = requests.put(upload_link, headers=self.get_headers(), data=open(path_to_file, 'rb'))
        if resp.status_code == 201 or 203:
            print('Success')
        else:
            (print(f' Код ошибки {resp.status_code}'))


if __name__ == '__main__':
    uploader = YaUploader(TOKEN)
    result = uploader.upload(r'C:\Users\Petr\PycharmProjects\Python_HW8.2\Test.txt')
