import requests
from pprint import pprint
TOKEN = 'y0_AgAAAABlVrvJAAib3QAAAADT7e7gRp8evt43Q-eQ2iujN06NQ9NsCAw'


def get_headers():
        return {
            'Content-Type': 'application/json',
            'Athorization': f'OAuth {TOKEN}'
        }

def get_files_list():
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()
        #return response.status_code

def upload(file_path):
        """Метод получает ссылку на загрузку"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json)
        return response.json().get('href')

def upload_file(file_path, filename):
        result = upload(file_path=file_path)
        href = result.get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.riase_for_status()
        if response.status_code == 201:
           print('success') 



if __name__ == '__main__':
    print(get_headers())