import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'condition', 'temp', 'scale', 'location')


def main():
    print_header()      # printheader
    location = input('Enter zipcode (92081): ')         # get zipcode from user
    html = get_html_from_web(int(location))             # get html from web
    report = get_weather_from_html(html)                # parse html
    # display for the forcast


def print_header():
    print('--------------------')
    print('    WEATHER CLIENT APP')
    print('--------------------')


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()                   # cityCss
    condition = soup.find(class_='condition-icon').get_text()                               # weatherConditionCss
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()       # weatherTempCss
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()      # weatherScaleCss

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # print(loc + ': ' + temp, scale + ' and ' + condition)
    return WeatherReport


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()

