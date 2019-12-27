from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.tradingview.com/chart/BTCUSD/rNOu4egQ-upwork/'
main = None
indicators = []

def get_info_from_chart(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    main_info = requests.get(url, headers=headers).text
    soup = BeautifulSoup(main_info, 'lxml')
    return soup

def get_tv_chart_view(soup):
    chart = soup.find_all("div", class_="tv-chart-view js-chart-view")
    chart_json = chart[0]['data-options']
    str_data = json.loads(chart_json)
    return str_data

if __name__ == '__main__':
    soup = get_info_from_chart(url)
    str_data = get_tv_chart_view(soup)
    panes = json.loads(str_data['content'])['panes']
    for item2 in item['sources']:
        if item2['type'] == 'MainSeries':
            main = item2
        elif item2['type'] == 'Study':
            indicators.append(item2)
            
    print(indicators)