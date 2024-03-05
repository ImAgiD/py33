# # # "26.02.24=======================Parsing 1======================="
# # # '''
# # # 1. Получить html-код страницы
# # # 2. Получить блок с товарами в html- коде
# # # 3. Получить данные из блока
# # # 4. Сохранить полученные данные в файл (json, csv, txt) 
# # # # ''' 
# # import json
# # import csv

# # import requests
# # from bs4 import BeautifulSoup as BS


# # Path = 'https://enter.kg/computers/noutbuki_bishkek'

# # def get_html(url):
# #     html = requests.get(url)
# #     return html.text    

# # def soup_html(html):
# #     soup = BS(html, 'lxml')
# #     return soup
    
# # def get_data(soup):
# #     data = soup.find_all('div', class_='row')
# #     dict_ = []
# #     for nout in data:
#         # title = nout.find('span', class_ = 'prouct_name').text
#         # img = 'https://enter.kg' + nout.find('img').get('src')
#         # img = nout.find('span', class_ = 'prouct_name').text
#         # price = nout.find('span', class_ = 'price').text
#         # dict_ = {'title': title, 'img': img, 'price': price}
# #         write_to_csv(dict_) 
                 
# #     return dict_

# # def write_to_csv(dict_):
# #     with open('db.csv', 'a') as file:
# #         write = csv.writer(file)
# #         write.writerow('db.csv'('title'),('img'),('price'))
        
# # def get_total_page(url, count):
# #     html = requests.get(f'{url}/results,{count*100+1}-{count*100}')
# #     return html.text

# # def get_last_page(url):
# #     html = get_html(url)
# #     soup = soup_html(html)
# #     last_page = soup.find('span', class_="vm-page-counter").text[-2:]
# #     return int(last_page)  
    
# # def write_to_json(data):
# #     with open('db.json', 'w') as file_:
# #         json_data = json.dumps(data)
# #         file_.write(json_data)

# # def main(url):
# #     count = 0
# #     last_page = get_last_page(url)
# #     data = []
# #     while count < last_page:
# #         html = get_total_page(url, count)
# #         soup = soup_html(html)
# #         data.append(get_data(soup))
# #         print(f'спарсилась страница {count+1}')
# #         count += 1
# #     write_to_json(data)

# # main(Path)
# '========================='
# import json
# import csv
# import requests
# from bs4 import BeautifulSoup as BS

# Path = 'https://enter.kg/computers/noutbuki_bishkek'

# def get_html(url):
#     html = requests.get(url)
#     return html.text

# def soup_html(html):
#     soup = BS(html, 'lxml')
#     return soup

# def get_data(soup):
#     data = soup.find_all('div', class_='product-item')
#     list_ = []
#     for nout in data:
#         title = nout.find('span', class_='prouct_name').text
#         img = 'https://enter.kg' + nout.find('img').get('src')
#         price = nout.find('span', class_='price').text
#         item = {'title': title, 'img': img, 'price': price}
#         list_.append(item)
#     return list_

# def get_total_page(url, count):
#     html = requests.get(f'{url}/results,{count*100+1}-{count*100}')
#     return html.text

# def get_last_page(url):
#     html = get_html(url)
#     soup = soup_html(html)
#     last_page = soup.find('span', class_="vm-page-counter").text.split()[-1]
#     return int(last_page)

# def write_to_json(data):
#     with open('db.json', 'w') as file_:
#         json_data = json.dumps(data, ensure_ascii=False, indent=2)
#         file_.write(json_data)

# def write_to_csv(data):
#     with open('db.csv', 'a', newline='', encoding='utf-8') as file:
#         fieldnames = ['title', 'img', 'price']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)

#         # If the file is empty, write the header
#         if file.tell() == 0:
#             writer.writeheader()

#         for row in data:
#             writer.writerow(row)

# def main(url):
#     count = 0
#     last_page = get_last_page(url)
#     data = []
#     while count < last_page:
#         html = get_total_page(url, count)
#         soup = soup_html(html)
#         data += get_data(soup)
#         print(f'Page {count+1} parsed successfully')
#         count += 1
#     write_to_json(data)
#     write_to_csv(data)

# main(Path)

import requests
from bs4 import BeautifulSoup

def parse_top_250_movies(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Ошибка при запросе. Код статуса: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "lxml")
    movie_table = soup.find_all(class_ = 'ipc-title-link-wrapper')
    print(movie_table)
    
#     if movie_table is None:
#         print("Не удалось найти таблицу с фильмами.")
#         return []

#     movie_rows = movie_table.find_all("tr")
#     title_list = []
#     for row in movie_rows[1:]:
#         cells = row.find_all("td")
#         rank = cells[0].get_text().strip()
#         title = cells[1].a.get_text().strip()
#         title_list.append(title)
#     return title_list

# def get_link(title_list, name):
#     for title in title_list:
#         if name.lower() in title.lower():
#             search_url = f"https://www.imdb.com/find?q={title.replace(' ', '+')}"
#             return urljoin("https://www.imdb.com/", search_url)
#     return None

# Пример использования
url = "https://www.imdb.com/chart/top/"
title_list = parse_top_250_movies(url)
# search_name = "shawshank"
# link = get_link(title_list, search_name)
# if link:
#     print(f"Ссылка на фильм '{search_name}': {link}")
# else:
#     print(f"Фильм '{search_name}' не найден.")
#  #parsing