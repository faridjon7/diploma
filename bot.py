import requests
from bs4 import BeautifulSoup


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



