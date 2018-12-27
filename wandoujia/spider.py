# -*- coding=utf-8 -*-
import json
import re
import time

import requests
from requests.exceptions import RequestException
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

__author__ = 'STM'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
    'Referer': 'https://www.wandoujia.com/'
}


def get_page_index():
    url = 'https://www.wandoujia.com/category/app'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求网址失败')
        return None


def parse_page_index(html):
    urls = []
    texts = []
    url_parttern = re.compile(r'<li class="parent-cate">.*?<a class="cate-link" href="(.*?)".*?title="(.*?)".*?</a>',
                              re.S)
    items = re.findall(url_parttern, html)
    for item in items:
        urls.append(item[0])
        texts.append(item[1])
    return urls, texts


def parse_one_page(url):
    names = []
    browser = webdriver.Chrome()
    browser.get(url)
    for _ in range(4):
        wait = WebDriverWait(browser, 3)
        wait.until(EC.presence_of_element_located((By.ID, 'j-refresh-btn')))
        browser.find_element_by_id('j-refresh-btn').click()
        time.sleep(1)
    html = browser.page_source
    name_pattern = re.compile(r'<a.*?data-app-name="(.*?)".*?</a>', re.S)
    items = re.findall(name_pattern, html)
    for item in items:
        names.append(item)
    return names


def main():
    result = {}
    html = get_page_index()
    urls, texts = parse_page_index(html)
    for i in range(len(urls)):
        print(texts[i], urls[i])
        # result[texts[i]] = parse_one_page(urls[i])
    # return result


if __name__ == '__main__':
    # res = main()
    # print(res)
    # with open('res.json', 'w', encoding='utf-8') as file:
    #     file.write(json.dumps(res, indent=2, ensure_ascii=False))
    main()
