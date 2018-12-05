# -*- coding=utf-8 -*-
import requests
from requests.exceptions import RequestException

__author__ = 'STM'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Referer': 'https://www.mzitu.com'
}


def get_page_index(page, keyword):
    url = 'https://www.mzitu.com/search/' + keyword + '/page/' + str(page)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求网址失败')
        return None


def main():
    html = get_page_index(1, '美胸')
    print(html)


if __name__ == '__main__':
    main()
