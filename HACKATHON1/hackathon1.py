'29.02.2024==================hackathon1=================='
'''## ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: лёгкая - 80 баллов)

- **📍Цель: Спарсить сайт [Kivano](https://www.kivano.kg/mobilnye-telefony) и получить следующие данные:**
        1. Наименование всех телефонов.
        2. Цену каждого продукта(в KGS).
        3. И ссылка к фотографии.
    4. Все это записать в CSV файл.
- **🛠 Инструменты:**
        1. BeautifulSoup.
        2. CSV.
        3. Requests.
- 🖇 **Дополнительно (по желанию):**
        1. Ваш парсинг скрипт должен выполняться каждые 60 минут.'''

import csv

import requests
from bs4 import BeautifulSoup as BS

def get_html(url): 
    response = requests.get(url)
    return (response.text)

def get_total_pages(html): 
    soup = BS(html, 'lxml')
    pages_ul = soup.find('div', class_ ='pager-wrap').find('ul')
    last_page = pages_ul.find_all('li')[-1]
    total_pages = last_page.find('a').get('href').split('=')[-1]
    return (int(total_pages)) 


def write_to_csv(data):
     with open('kivano_handys.csv', 'a') as csv_file:
         writer = csv.writer(csv_file)
         writer.writerow((data['title'], 
                          data['price'], 
                          data['photo']))
         
def get_page_data(html):
    soup = BS(html, 'lxml')
    product_list = soup.find('div', class_ = 'product-index product-index oh').find('div', class_ = 'list-view')
    products = product_list.find_all('div', class_ = 'item product_listbox oh')

    for product in products: 
        try:
            photo = ('https://www.kivano.kg'+product.find('div', class_ = 'listbox_img pull-left').find('a').find('img').get('src'))

        except:
            photo = ''
        try:
            title = product.find('div', class_ ='listbox_title oh').find('strong').text

        except:
            title = ''
        try: 
            price = product.find('div', class_='listbox_price text-center').find('strong').text

        except:
            price = ''

        data = {'title':title, 'price':price, 'photo':photo}
        write_to_csv(data)

def main():
    url = 'https://www.kivano.kg/mobilnye-telefony'
    
    pages = '?page='
    total_pages = get_total_pages(get_html(url))

    for page in range(1,total_pages+1): 
        url_with_page = url + pages + str(page)
        html = get_html(url_with_page)
        get_page_data(html)

main() 