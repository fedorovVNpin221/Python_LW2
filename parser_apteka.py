from bs4 import BeautifulSoup
import requests
import emoji

def parse(name1):
    tick = emoji.emojize(":check_mark_button:")
    cross = emoji.emojize(":cross_mark:")
    medic = emoji.emojize(":green_heart:")
    url = 'https://farmakopeika.ru/search?query=' + name1
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "lxml")
    block = soup.findAll('div', id="products-app")
    treat_info = ''
    for data in block:
        if data.find('div', class_='product product_grid'):
            treat_info = data.text
    for i in range(4):
        treat_info = treat_info.replace('\n\n', '\n')
    treat_info = treat_info.replace('В корзину', '')
    treat_info = treat_info.replace('от', 'Цена от: ')
    treat_info = treat_info.replace('\n\n', '\n')
    treat_info = treat_info.replace('\nесть', tick)
    treat_info = treat_info.replace('\nнет', cross)
    treat_info = treat_info.replace('аптеки\n', 'аптеки'+ medic + '\n\n')
    treat_info = treat_info.replace('аптек\n', 'аптек'+ medic + '\n\n')
    treat_info = treat_info.replace('аптека\n', 'аптека' + medic + '\n\n')
    treat_info = treat_info.replace('В аптеках:\n', 'В аптеках: ')
    treat_info = treat_info.replace('На складе:\n', 'На складе: ')
    return treat_info
