import json
import csv

import requests
from bs4 import BeautifulSoup as BS


Path = 'https://enter.kg/computers/noutbuki_bishkek'

def get_html(url):
    html = requests.get(url)
    return html.text    

def soup_html(html):
    soup = BS(html, 'lxml')
    return soup
    
def get_data(soup):
    data = soup.find_all('div', class_='row')
    dict_ = []
    for nout in data:
        title = nout.find('span', class_ = 'prouct_name').text
        img = 'https://enter.kg' + nout.find('img').get('src')
        price = nout.find('span', class_ = 'price').text
        dict_.append({'title': title, 'img': img, 'price': price})
    return dict_ 

# def write_to_csv(data):
#     with open('db.csv', 'w', newline='') as file:
#         fieldnames = ['title', 'img', 'price']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)

#         writer.writeheader()  # Write header row

#         for row in data:
#             writer.writerow(row)


def write_to_csv(data):
     with open('db.csv', 'a') as csv_file:
         writer = csv.writer(csv_file)
         writer.writerow((data['title'], 
                          data['img'], 
                          data['price']))
         

def get_total_page(url, count):
    html = requests.get(f'{url}/results,{count*100+1}-{count*100}')
    return html.text

def get_last_page(url):
    html = get_html(url)
    soup = soup_html(html)
    last_page = soup.find('span', class_="vm-page-counter").text[-2:]
    return int(last_page)  
    
def write_to_json(data):
    with open('db.json', 'w') as file_:
        json_data = json.dumps(data)
        file_.write(json_data)

def main(url):
    count = 0
    last_page = get_last_page(url)
    data = []
    while count < last_page:
        html = get_total_page(url, count)
        soup = soup_html(html)
        data.append(get_data(soup))
        print(f'спарсилась страница {count+1}')
        count += 1
    write_to_json(data)
    write_to_csv(data)

main(Path)
 
