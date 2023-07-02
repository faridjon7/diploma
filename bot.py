import requests
from bs4 import BeautifulSoup

url1 = 'http://fapl.ru'
r1 = requests.get(url1)
soup1 = BeautifulSoup(r1.content, 'html.parser')
# apl_table = soup1.find_all('div', class_='block table')[0].text
apl_last_matches = soup1.find_all('div', class_='block table')[1].text
print(apl_last_matches)