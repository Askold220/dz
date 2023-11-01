import requests
from bs4 import BeautifulSoup

url = 'http://yermilovcentre.org/medias/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a', href=True)

    processed_links = []

    for link in links:
        href = link['href']
        title = link.get_text()  
    
        if href not in processed_links:
            processed_links.append(href)
            print(f'Назва: {title}')
            print(f'Посилання: {href}')
else:
    print(f'Помилка завантаження сторінки. Код статусу: {response.status_code}')

