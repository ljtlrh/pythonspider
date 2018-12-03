# -*- coding=utf-8 -*-
import json
import re

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from urllib.parse import urlencode

__author__ = 'STM'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}


def get_page_index(offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求索引页失败")
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield "https://www.toutiao.com/a" + item.get('id')


def get_page_detail(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求页面失败', url)
        return None


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile(r'JSON.parse.*?url_list\\":\[(.*?)\],', re.S)
    result = re.search(images_pattern, html)
    if result:
        data = result.group(1)
        print(data)
        urlList = [url for url in data.split(",")]
        urls = [url[11:-2].replace('\\', '') for url in urlList]
        return {
            'title': title,
            'url': url,
            'images': urls
        }
    return None


def main():
    html = get_page_index(0, '街拍')
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html, url)
            print(result)


if __name__ == '__main__':
    main()
