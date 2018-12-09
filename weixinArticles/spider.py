# -*- coding=utf-8 -*-
from urllib.parse import urlencode

import requests
from requests.exceptions import ConnectionError

__author__ = 'STM'

base_url = 'https://weixin.sogou.com/weixin?'
keyword = '风景'
proxy_pool_url = 'http://localhost:5000/get'
headers = {
    'Cookie': 'IPLOC=CN3100; SUID=D0D52D652313940A000000005C0BCF60; SUV=1544277856282190; ABTEST=7|1544277858|v1; SNUID=E5E01951353048B7011F4B23354ECCB8; weixinIndexVisited=1; sct=1; JSESSIONID=aaaeHlzeYGHpHdliFM6Cw; ppinf=5|1544280100|1545489700|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTUlQTQlQTklRTYlOTglOEV8Y3J0OjEwOjE1NDQyODAxMDB8cmVmbmljazoxODolRTUlQTQlQTklRTYlOTglOEV8dXNlcmlkOjQ0Om85dDJsdUtKOUxNWEtzLUxKUWs0WnFrWmJFWHNAd2VpeGluLnNvaHUuY29tfA; pprdig=M2Q4hlem5K3js3oBcCOFJRePl9TQFdOuBdhCYozzKwxG9RVw6Zql_qQFD3QPH1cCUQvRkUvTQSa01OHU9Ro-Cl2g043z-4c_8V8NHpSwyKmLGFqAniKiaPiACMpuxR-nA9gg60coy2z-RVFAFQfxdV53vPZ6Uv8iYr9tFWFpLfc; sgid=00-43258663-AVwL2CSMZupibBSRhhHSdATA; ppmdig=1544280100000000dceb65970db2df491d50523ad1adc8c1',
    'Host': 'weixin.sogou.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

proxy = None
max_count = 5


def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None


def get_html(url, count=1):
    print('Crawling', url)
    print('Tring Count', count)
    global proxy
    if count >= max_count:
        print('Tried Too Many Counts.')
        return None
    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            # need proxy
            print('302')
            proxy = get_proxy()
            if proxy:
                print('Using Proxy', proxy)
                # count += 1
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occurred', e.args)
        count += 1
        proxy = get_proxy()
        return get_html(url, count)


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html


def main():
    for page in range(1, 101):
        html = get_index(keyword, page)
        print(html)


if __name__ == '__main__':
    # get_index('风景', 1)
    main()
