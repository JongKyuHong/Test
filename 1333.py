import requests
from bs4 import BeautifulSoup
import ssl
from itertools import count
import pandas as pd
import time
import csv
from selenium import webdriver
#from  geopy.geocoders import Nominatim
import geocoder #pip install
import openpyxl #pip install
context = ssl._create_unverified_context()
url = "https://kr.hotels.com/search.do?resolved-location=CITY%3A759818%3AUNKNOWN%3AUNKNOWN&destination-id=759818&q-destination=%EC%84%9C%EC%9A%B8,%20%ED%95%9C%EA%B5%AD&q-check-in=2020-05-18&q-check-out=2020-05-19&q-rooms=1&q-room-0-adults=2&q-room-0-children=0"
# % urllib.parse.quote("서울특별시") 
#print(url)
driver = webdriver.Chrome(('chromedriver'))
driver.get(url)
driver.implicitly_wait(5)

brand_list = []
SCROLL_PAUSE_TIME=2
last_height = driver.execute_script("return document.body.scrollHeight")
a=0
while True:
    a +=1
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight-50);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    if a==1:
        break
a = 0
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
#for i in range(0,100):
    #c = driver.find_elements_by_xpath("//*[@id=listings]/ol/li"+str(i)+"/article/section/div/h3/a")
    #c.click()
    #c = driver.find_element_by_class_name('p-name')
    #c.find_element_find_element_by_class_name('property-name-link').click()
    #c = driver.find_element_by_css_selector('#listings > ol > li > article > section > div > h3 > a').click()
    #name = soup.selector('#property-header > div > div.vcard > h1')
    #add = soup.selector('#property-header > div > span > span')
            
result = []

#name = soup.select('#listings > ol > li > article > section > div > h3 > a')
address = soup.select('#listings > ol > li > article > section > div > address > span')

#ad = address
#a=0
#for i in address:
#    address[a] = address[a].split(',')[0]
 #   a+=1
    
for i in address:
    result.append(i.text.split(','))

    
#for i in zip(name,address):
#    a+=1
    
#    result.append({
#       'name' : i[0].text.replace('\n','').replace('\t','').replace(' ',''),
#       'address' : i[1].text.replace('\n','').replace('\t','').replace(' ',''),
#    })
   
#    if a == 50:
#       break



data = pd.DataFrame(result)
#data.to_csv('hotel2.csv',index=False)#,encoding="euc-kr"
data.to_excel('hotel2.xlsx',index=False)#,encoding="euc-kr"


#elem = driver.find_element_by_id('address_input')
#elem.send_keys(n)


#la = soup.select('#reveal-card > div > div.widget-reveal-card-container > button.link-like.widget-reveal-card-lat-lng')



#for n in result:
    #driver.get("https://www.google.co.kr/maps")
    #driver.implicitly_wait(3)
    #html = driver.page_source
    #soup = BeautifulSoup(html,'html.parser')
    #elem = driver.find_element_by_id("searchboxinput")
    #elem.send_keys(n)
    #elem = driver.find_element_by_id("searchbox-searchbutton")
    #elem.click()
    #la = soup.select('#reveal-card > div > div.widget-reveal-card-container > button.link-like.widget-reveal-card-lat-lng')
    #ele1 = driver.find_element_by_class_name('app-viewcard-strip')
    #ele2 = ele1.find_element_by_class_name('app-center-widget-holder')
   # ele3 = ele2.find_element_by_class_name('widget-reveal-card widget-reveal-card-open')
    #ele4= ele3.find_element_by_class_name('widget-reveal-card-container')
    #ele = ele4.find_element_by_class_name('link-like widget-reveal-card-lat-lng')
    #print(ele)
    
    


#table = driver.find_elements_by_css_selector('listings > ol > li > article > section > div')
#print(table)

#listings > ol > li:nth-child(48) > article > section > div > address > span
#for ele in table:#h3.p-name
#    name = ele.find_elememnt_by_css_selector('h3.a').text
#    adr = ele.find_element_by_css_selector('span.address').text
#    result.append([name]+[adr])
#data = pd.DataFrame(result)
#data.to_csv('hotel2.csv',encoding="euc-kr")


#request = requests.get(url)
#html = request.text
#reponse = urllib.request.urlopen(request, context=context)
#soupdata = BeautifulSoup(reponse, "html.parser")
#soupdata = BeautifulSoup(html, "html.parser")
#listings > ol > li:nth-child(64) > article > section > div > h3 > a
#class="table mt20"

#name = soupdata.select('listings > ol > li')
#print(name)
#name = soupdata.find_all('a',class_='property-name-link')
#listings > ol > li:nth-child(34) > article > section > div > h3 > a
#print(name[0].text)
#address = soupdata.select('li > article > section > div > address > span')
#address = soupdata.find_all('span',class_='address')
#for i in range(0,100):
#    print(name[i].text)
#    print(address[i].text)
#print(address[0].text)

#for i in zip(name, address):
#    hotel.append({
#            'name' : i[0].text.replace('\n','').replace('\t','').replace(' ',''),
#            'address' : i[1].text.replace('\n','').replace('\t','').replace(' ',''),
#            })

#for i in name:
#    hotel.append({'name':'address'})
#data = pd.DataFrame(hotel)
#data.to_csv('hotel.csv',encoding="euc-kr")



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
