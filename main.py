import requests
from bs4 import BeautifulSoup

url = 'https://moodle.voenmeh.ru/my/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.text
    print(f'Заголовок страницы: {title}')

    print('\nСсылки на странице:')
    for link in soup.find_all('a', href=True):
        print(f"Текст: {link.text.strip()}, Ссылка: {link['href']}")

    print('\nАбзацы текста:')
    for paragraph in soup.find_all('p'):
        text = paragraph.text.strip()
        if text:  # Пропускаем пустые абзацы
            print(text)

else:
    print(f'Ошибка при запросе: {response.status_code}')