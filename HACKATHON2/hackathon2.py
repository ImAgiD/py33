'29.02.24=================hackathon2================='
'''## ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: средняя - 90 баллов)
- **📍Цель: Спарсить [mashina.kg,](https://www.mashina.kg/) разделив на категории:**
        1. Название всех моделей.
        2. Цену всех моделей.
        3. Изображение всех моделей.
        4. Краткое описание всех моделей.
        5. Записать все в csv файл.
- **🛠 Инструменты**
        1. BeautifulSoup4.
        2. csv.
        3. Requests.'''
        
import csv
import requests
from bs4 import BeautifulSoup as BS

def get_html(url): 
    response = requests.get(url)
    return response.text

def get_total_pages(html): 
    soup = BS(html, 'lxml')
    pages_ul = soup.find('div', class_ ='search-results-table').find('ul')
    last_page = pages_ul.find_all('li')[-1]
    total_pages = last_page.find('a').get('href').split('=')[-1]
    return (int(total_pages)) 

def write_to_csv(data):
     with open('mashiny.csv', 'a') as csv_file:
         writer = csv.writer(csv_file)
         writer.writerow((data['title'], 
                          data['price'], 
                          data['img'],
                          data['desc']))

def get_page_data(html):
    soup = BS(html, 'lxml')
    data_page = soup.find('form', id='search-filter')
    cars_list = data_page.find('div', class_='search-results-table')
    cars = cars_list.find_all('div', class_='list-item list-label')

    for car in cars:
        title = car.find('h2', class_='name').text.replace(' ', '').replace('\n','')
        price = car.find('div', class_='block price').text.replace(' ', '').replace('\n','')
        img = car.find('img').get('src')
        desc = car.find('div', class_='block info-wrapper item-info-wrapper').text.replace(' ', '').replace('\n','')
        data = {'title': title, 'price': price,  'img': img, 'desc': desc}
        write_to_csv(data) 
        
def main():
    url = 'https://www.mashina.kg/search/all/'
    pages = '?page='
    total_pages = min(5, get_total_pages(get_html(url)))  

    for page in range(1, total_pages + 1):
        url_with_page = url + pages + str(page)
        html = get_html(url_with_page)
        get_page_data(html)

main()
