import requests
from bs4 import BeautifulSoup
import ssl
from itertools import count
import pandas as pd
context = ssl._create_unverified_context()
url = "https://kr.hotels.com/search.do?resolved-location=CITY%3A759818%3AUNKNOWN%3AUNKNOWN&destination-id=759818&q-destination=%EC%84%9C%EC%9A%B8,%20%ED%95%9C%EA%B5%AD&q-check-in=2020-05-18&q-check-out=2020-05-19&q-rooms=1&q-room-0-adults=2&q-room-0-children=0"
# % urllib.parse.quote("서울특별시") 
#print(url)
request = requests.get(url)
html = request.text
#reponse = urllib.request.urlopen(request, context=context)
#soupdata = BeautifulSoup(reponse, "html.parser")
soupdata = BeautifulSoup(html, "html.parser")

#class="table mt20"
#name = soupdata.select('li> article > section > div > h3 > a')
name = soupdata.find_all('a',class_='property-name-link')
print(name[0].text)

address = soupdata.find_all('span',class_='address')
print(address[0].text)
hotel = []
for i in zip(name, address):
    hotel.append({
            'name' : i[0].text.replace('\n','').replace('\t','').replace(' ',''),
            'address' : i[1].text.replace('\n','').replace('\t','').replace(' ',''),
            })
data = pd.DataFrame(hotel)
data.to_csv('hotel.csv')

#store_table = soupdata.find('table',{'class':'table mt20'})
#tbody = store_table.find("tbody")
#tr = tbody.findAll('tr')
#bEnd = True
#for store in tr:
    #bEnd = False
    #store_info= list(store.strings)
    #store_name = store_info[1]
    #store_address = store_info[2]
    #print(store_name, store_address, store_phone)

#listings > ol > li:nth-child(2) > article > section > div > h3 > a
#listings > ol > li:nth-child(16) > article > section > div > h3 > a
