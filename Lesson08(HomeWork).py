import requests

print("-------------------------------------------- Задание 1 (90)")

try:
    # url = 'htps://www.google.com/'  # URL
    # url = 'https://www.google.com/'  # 200
    url = 'https://www.google.com/ii'  # 404
    request = requests.get(url)
    html = request.text
    if str(request) == '<Response [404]>':
        print('Ошибочка. Сайт вернул 404!')
    if str(request) == '<Response [200]>':
        print('Гуд. Сайт вернул 200!')
except requests.exceptions.InvalidSchema:
    print('Ошибка в URL!')
except requests.exceptions.ConnectionError:
    print('Ошибка в подключении!')
