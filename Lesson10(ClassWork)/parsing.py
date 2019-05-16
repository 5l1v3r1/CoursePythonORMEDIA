import requests
from bs4 import BeautifulSoup

url = 'https://afisha.tut.by/film/?crnd=49574'
r = requests.get(url).text  # Response
soup = BeautifulSoup(r, "html.parser")
link = soup.find('div', id='events-block')
links = link.find_all('li', class_='lists__li')

list_text = []
list_img = []
list_link = []


def create_text():
    for lk in links:
        text = lk.find('a', class_='name').text
        list_text.append(text)
    return list_text


def create_img():
    for im in links:
        image = im.find('a', class_='media')
        images = image.find('img').get('src')
        list_img.append(images)
    return list_img


def create_link():
    for ln in links:
        link = ln.find('a', class_='media').get('href')
        list_link.append(link)
    return list_link
