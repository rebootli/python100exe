
import requests
import logging
import re
from urllib.parse import urljoin

import json
from os import makedirs
from os.path import exists

import multiprocessing

RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s: %(message)s')

BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10

def scrape_page(url):
    logging.info('scraping %s...',url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s',response.status_code,url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s',url,exc_info=True)


def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url) 

def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name"')
    items = re.findall(pattern,html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL,item)  #它能够将一个基础 URL（BASE_URL）和一个相对 URL（item）组合成一个完整的绝对 URL（detail_url）
        logging.info('get detail url %s',detail_url)
        yield detail_url #每次循环时，yield detail_url 会把当前生成的绝对 URL detail_url 返回给调用者，并且暂停函数的执行。当调用者请求下一个值时，函数会从暂停的位置继续执行，直到生成所有的值或者函数结束。

def scrape_detail(url):
    return scrape_page(url)

def parse_detail(html):
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')
    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>', re.S)
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)
    cover = re.search(cover_pattern, html).group(1).strip() if re.search(cover_pattern, html) else None
    name = re.search(name_pattern, html).group(1).strip() if re.search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) if re.findall(categories_pattern, html) else []
    published_at = re.search(published_at_pattern, html).group(1) if re.search(published_at_pattern, html) else None
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) else None
    score = float(re.search(score_pattern, html).group(1).strip()) if re.search(score_pattern, html) else None
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }

def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

def main(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail data %s', data)
        logging.info('saving data to json file')
        save_data(data)
        logging.info('data saved successfully')



if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PAGE + 1)
    pool.map(main, pages)
    pool.close()
    pool.join()



