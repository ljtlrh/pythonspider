# -*- coding=utf-8 -*-
import os
import re
import time
from hashlib import md5
import requests
from requests.exceptions import RequestException
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from multiprocessing import Pool

__author__ = 'STM'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Referer': 'http://www.mmjpg.com'
    # 'content-type': 'application/x-www-form-urlencoded'
}


def get_page_index(keyword):
    url = 'http://www.mmjpg.com/search.php'
    data = {'key': keyword}
    try:
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            return str(response.content, 'utf-8')
        return None
    except RequestException:
        print('请求网址失败')
        return None


def parse_page_index(html):
    urls = []
    texts = []
    url_parttern = re.compile(r'<li>.*?<a href="(.*?)".*?target.*?alt="(.*?)".*?>', re.S)
    items = re.findall(url_parttern, html)
    for item in items:
        urls.append(item[0])
        texts.append(item[1])
    return urls, texts


def parse_one_page(url):
    browser = webdriver.Chrome()
    browser.get(url)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.presence_of_element_located((By.ID, 'opic')))
    browser.find_element_by_id('opic').click()
    # browser.find_element_by_xpath('//em[@class="ch all"]').click()
    time.sleep(1)
    html = browser.page_source
    # print(html)
    image_pattern = re.compile('<img src=.*?data-img="(.*?)".*?>', re.S)
    items = re.findall(image_pattern, html)
    for item in items:
        yield item


def save_image(path, content):
    if not os.path.exists(path):
        os.mkdir(path)
    file_path = '{0}/{1}{2}'.format(path, md5(content), '.jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)


def download_image(path, url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            save_image(path, response.content)
            return True
        return None
    except RequestException:
        print('请求图片出错', url)
        return None


def main():
    html = get_page_index('')
    # print(html)
    urls, texts = parse_page_index(html)
    for i in range(len(urls)):
        for url in parse_one_page((urls[i])):
            print(url)
            download_image(texts[i], url)
    # urls, texts = parse_page_index(html)
    # for url in parse_one_page(urls[offset]):
    #     download_image(texts[offset], url)


if __name__ == '__main__':
    # pool = Pool()
    # groups = [x for x in range(30)]
    # pool.map(main, groups)
    # pool.close()
    # pool.join()

    # for i in range(30):
    main()

    # download_image('http://fm.shiyunjj.com/2016/559/16.jpg')
    # for url in parse_one_page("http://www.mmjpg.com/mm/1553"):
    #     print(url)
