import requests
from bs4 import BeautifulSoup

HEADERS = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'accept' :'*/*'}
URL = 'https://jut.su/'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('ul', class_='downer_nav').find_all('li')
    recors = []
    for item in items:
        name = item.find('a').text
        link = item.find('a').get('href')
        recors.append({
            'name': name,
            'link': 'https://jut.su/' + link
        })
        print(len(recors))


def main():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

if __name__ == '__main__':
    main()