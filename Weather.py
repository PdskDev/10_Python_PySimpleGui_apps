import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs


def get_weather_data(location):
    url = f"https://www.google.com/search?q=weather+{location.replace(' ', '')}"
    session = requests.Session()
    session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    html = session.get(url)

    soup = bs(html.text, 'html.parser')
    name = soup.find('div', attrs={'id': 'wob_loc'}).text
    time = soup.find('div', attrs={'id': 'wob_dts'}).text
    weather = soup.find('span', attrs={'id': 'wob_dc'}).text
    temp = soup.find('span', attrs={'id': 'wob_tm'}).text
    return name, time, weather, temp


sg.theme('reddit')

image_col = sg.Column(
    [[sg.Image(key='-IMAGE-', background_color='#FFFFFF')]])
info_col = sg.Column([
    [sg.Text('', key='-LOCATION-', font='calibri 30', text_color='#FFFFFF',
             background_color='#FF0000', pad=0, visible=False)],
    [sg.Text('', key='-TIME-', font='calibri 16', background_color='#000000',
             text_color='#FFFFFF', pad=0, visible=False)],
    [sg.Text('', key='-TEMP-', font='calibri 16',  text_color='#000000', background_color='#FFFFFF',
             pad=(0, 10), justification='center', visible=False)]
])

layout = [
    [sg.Input(expand_x=True, key='-INPUT-'),
     sg.Button('Enter',  font='calibri 12', button_color='#000000', border_width=0)],
    [image_col, info_col]


]

window = sg.Window('Weather', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Enter':
        name, time, weather, temp = get_weather_data(values['-INPUT-'])
        window['-LOCATION-'].update(name, visible=True)
        window['-TIME-'].update(time.split(' ')[0], visible=True)
        window['-TEMP-'].update(f'{temp} \u2103 ({weather})', visible=True)

        # sun
        if weather in ('Temps clair', 'Sun', 'Sunny', 'Clear', 'Clear with periodic clouds', 'Mostly sunny'):
            window['-IMAGE-'].update('images/sun.png')

        # part sun
        if weather in ('Partly Sunny', 'Mostly Sunny', 'Partly cloudy', 'Mostly cloudy', 'Cloudy', 'Overcast'):
            window['-IMAGE-'].update('images/part_sun.png')

        # rain
        if weather in ('Rain', 'Chance of Rain', 'Light Rain', 'Showers', 'Scattered Showers', 'Rain and Snow', 'Hail'):
            window['-IMAGE-'].update('images/rain.png')

        # thunder
        if weather in ('Scattered Thunderstorms', 'Chance of Storm', 'Storm', 'Thunderstorm', 'Chance of TStorm'):
            window['-IMAGE-'].update('images/thunder.png')

        # foggy
        if weather in ('Mist', 'Dust', 'Fog', 'Smoke', 'Haze', 'Flurries'):
            window['-IMAGE-'].update('images/fog.png')

        # snow
        if weather in ('Freezing Drizzle', 'Chance of Snow', 'Sleet', 'Snow', 'Icy', 'Snow Showers'):
            window['-IMAGE-'].update('images/snow.png')


window.close()
