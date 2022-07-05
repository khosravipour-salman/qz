from bs4 import BeautifulSoup
import requests

	
url = 'https://www.countries-ofthe-world.com/capitals-of-the-world.html'
r = requests.get(url)
# table class --> two-column td-red
soup = BeautifulSoup(r.content, 'html.parser')

table = soup.find('table', attrs={'class':'two-column td-red'})

table_body = table.find('tbody')
rows = table_body.find_all('tr')

handler = open('country_capitals.txt', 'a')

for row in rows:
    cols = row.find_all('td')
    if len(cols) != 1:
    	country, capital = cols
    	handler.write(f'{country.text}@@{capital.text}\n')
else:
	handler.close()
