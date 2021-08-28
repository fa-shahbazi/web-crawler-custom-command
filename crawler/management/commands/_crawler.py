import re

import requests
from bs4 import BeautifulSoup
from crawler.management.commands._urls import links

def crawl_product(url, page_number_limit):
    data = []
    page_number = 1
    crawl = True
    pat = r'[-\w]*(?=\?sort)'
    pat2 = r'([-\w]*)&page'
    if re.search(r'\?sort', url) is not None:
        category = re.search(pat, url).group()
        data.append(category)
    else:
        category = re.search(pat2, url).groups()[0]
        data.append(category)
    while crawl:
        response = requests.get(url.format(page_number=page_number))
        crawl = response.ok

        soup = BeautifulSoup(response.text, 'html.parser')

        product_selector = soup.select('section.tw-flex')

        for product in product_selector:
            single_data = {}
            single_data['name'] = product.select('h4')[0].text.strip()
            try:
                single_data['price'] = product.select('span')[-2].text.strip()
            except:
                single_data['price'] = product.select('div')[-1].text.strip()
            data.append(single_data)

        page_number += 1
        if page_number > page_number_limit:
            crawl = False

    return data
