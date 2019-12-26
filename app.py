from bs4 import BeautifulSoup
import requests


url = 'https://www.tradingview.com/chart/BTCUSD/rNOu4egQ-upwork/'


def get_info_from_chart(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    main_info = requests.get(url, headers=headers).text
    soup = BeautifulSoup(main_info, 'lxml')
    return soup

def get_tv_chart_view(soup):
    chart = soup.find_all("div", class_="tv-chart-view js-chart-view")
    return chart

if __name__ == '__main__':
    soup = get_info_from_chart(url)
    chart = get_tv_chart_view(soup)
    print(chart)
