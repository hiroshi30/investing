import os
import urllib
import requests


CoinMarketCap_url = 'https://coinmarketcap.com/currencies/{}/'
HTX_url = 'https://www.htx.com/en-us/trade/{}_usdt?type=spot'


def parse_html(url):
    request = urllib.request.Request(
        url=url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    )

    data = urllib.request.urlopen(request).read()
    try:
        return data.decode('utf-8')
    except:
        return parse_html(url)


def download_icon(short_name, info):
    print(short_name)
    data = parse_html(CoinMarketCap_url.format(info['CRYPTOCURRENCY'][short_name][1]))

    start_index = 0
    end_index = data.find(f'alt="{short_name}"')
    url = ''

    while True:
        if data[end_index] == '"':
            start_index = end_index - 1
            while data[start_index] != '"':
                start_index -= 1

            if 'https' in data[start_index + 1: end_index]:
                url = data[start_index + 1: end_index]
                break
        end_index -= 1

    print(url)

    response = requests.get(url)
    with open(f'icons/{short_name}.png', 'wb') as file:
        file.write(response._content)


def load_icons(info):
    if 'icons' not in os.listdir():
        os.mkdir('icons')

    if 'CRYPTOCURRENCY' in info:
        if 'BTC.png' not in os.listdir('./icons'):
            download_icon('BTC', info)

        for coin in info['CRYPTOCURRENCY']:
            if coin + '.png' not in os.listdir('./icons'):
                download_icon(coin, info)


# def get_price(short_name):
#     data = parse_html(HTX_url.format(short_name))
#     start_index = data.index('<span class="price color-down ">')
#     print(start_index)
#     end_index = start_index + 1
#     while data[end_index] != '<':
#         end_index += 1
#     return float(data[start_index: end_index])
