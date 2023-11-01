from bs4 import BeautifulSoup

with open('sample.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

title = soup.find('h1', class_='title')
content = soup.find('p', class_='content')
list_items = soup.find_all('li', class_='list-item')

print("Заголовок:", title.text)
print("Вміст:", content.text)

print("Елементи списку:")
for item in list_items:
    print(item.text)
