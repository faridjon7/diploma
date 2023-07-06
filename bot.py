import requests
from bs4 import BeautifulSoup
from telebot import types

url1 = 'http://fapl.ru'
r1 = requests.get(url1)
soup1 = BeautifulSoup(r1.content, 'html.parser')
# apl_table = soup1.find_all('div', class_='block table')[0].text
apl_last_matches = soup1.find_all('div', class_='block table')[1].text
print(apl_last_matches)

url2 = 'https://www.sports.ru/la-liga/table/'
r2 = requests.get(url2)
soup2 = BeautifulSoup(r2.content, 'html.parser')
laliga_table = soup2.find_all('div', class_='stat mB6')[0].text
print(laliga_table)

url3 = 'https://www.sports.ru/la-liga/calendar/'
r3 = requests.get(url3)
soup3 = BeautifulSoup(r3.content, 'html.parser')
laliga_matches = soup3.find_all('div', class_='stat mB15')[0].text

url4 = 'https://www.sports.ru/seria-a/table/'
r4 = requests.get(url4)
soup4 = BeautifulSoup(r4.content, 'html.parser')
seria_a_table = soup4.find_all('div', class_='stat mB6')[0].text
# print(seria_a_table)

url5 = 'https://www.sports.ru/seria-a/calendar/'
r5 = requests.get(url5)
soup5 = BeautifulSoup(r5.content, 'html.parser')
seria_a_matches = soup5.find_all('div', class_='stat mB15')[0].text

url6 = 'https://www.sports.ru/bundesliga/table/'
r6 = requests.get(url6)
soup6 = BeautifulSoup(r6.content, 'html.parser')
bundesliga_table = soup6.find_all('div', class_='stat mB6')[0].text

url7 = 'https://www.sports.ru/bundesliga/calendar/'
r7 = requests.get(url7)
soup7 = BeautifulSoup(r7.content, 'html.parser')
bundesliga_matches = soup7.find_all('div', class_='stat mB15')[0].text

url8 = 'https://www.sports.ru/ligue-1/table/'
r8 = requests.get(url8)
soup8 = BeautifulSoup(r8.content, 'html.parser')
ligue_1_table = soup8.find_all('div', class_='stat mB6')[0].text

url9 = 'https://www.sports.ru/ligue-1/calendar/'
r9 = requests.get(url9)
soup9 = BeautifulSoup(r9.content, 'html.parser')
ligue_1_matches = soup9.find_all('div', class_='stat mB15')[0].text

url10 = 'https://terrikon.com/champions-league'
r10 = requests.get(url10)
soup10 = BeautifulSoup(r10.content, 'html.parser')
ucl = soup10.find_all('div', class_='groups-info')[0].text

url11 = 'https://terrikon.com/europa-league'
r11 = requests.get(url11)
soup11 = BeautifulSoup(r11.content, 'html.parser')
uel = soup11.find_all('div', class_='groups-info')[0].text

url12 = 'https://terrikon.com/conference-league'
r12 = requests.get(url12)
soup12 = BeautifulSoup(r12.content, 'html.parser')
conference_league = soup12.find_all('div', class_='groups-info')[0].text


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Лига Чемпионов')
    button2 = types.KeyboardButton('Лига Европы')
    button3 = types.KeyboardButton('Лига Конференций')
    button4 = types.KeyboardButton('АПЛ')
    button5 = types.KeyboardButton('ЛаЛига')
    button6 = types.KeyboardButton('Серия А')
    button7 = types.KeyboardButton('Бундеслига')
    button8 = types.KeyboardButton('Лига 1')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8)


