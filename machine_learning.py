#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 03:01:45 2020

@author: ceyda
"""

#Siteden verileri çektiğimiz kodlar

#requests ve beautiful soup kütüphaneleri import edildi.
from bs4 import BeautifulSoup
import requests

#Çekilecek verilerin url adresi tanımlandı.
url1 = "https://www.polygon.com/features/2017/12/1/16707720/the-500-best-games-of-all-time-100-1"
url2="https://www.polygon.com/features/2017/11/30/16717548/polygon-500-best-games-of-all-time-200-101"
url3= "https://www.polygon.com/features/2017/11/29/16693094/polygon-500-best-games-of-all-time-300-201"
url4="https://www.polygon.com/features/2017/11/28/16689522/polygon-500-best-games-of-all-time-400-301"
url5= "https://www.polygon.com/features/2017/11/27/16158276/polygon-500-best-games-of-all-time-500-401"

#Siteye HTML formatında istekte bulunduk ve çektiğimiz sayfayı soup değişkinine BeautifulSoup sayesinde atadık.

istek1 = requests.get(url = url1)
html1 = istek1.text
soup1 = BeautifulSoup(html1, 'html.parser')
istek2 = requests.get(url = url2)
html2 = istek2.text
soup2 = BeautifulSoup(html2, 'html.parser')
istek3 = requests.get(url = url3)
html3 = istek3.text
soup3 = BeautifulSoup(html3, 'html.parser')
istek4 = requests.get(url = url4)
html4 = istek4.text
soup4 = BeautifulSoup(html4, 'html.parser')
istek5 = requests.get(url = url5)
html5 = istek5.text
soup5 = BeautifulSoup(html5, 'html.parser')

for data1 in soup1.find_all('strong'):
#sayfa kaynağındaki 'strong' değerinin içindekimetin bilgisi alındı ve ekrana yazdırıldı.
    print(data1.get_text())
for data2 in soup2.find_all('strong'):
    print(data2.get_text())
for data3 in soup3.find_all('strong'):
    print(data3.get_text())
for data4 in soup4.find_all('strong'):
    print(data4.get_text())
for data5 in soup5.find_all('strong'):
    print(data5.get_text())


#Veriler üzerindeki ön işleme adımları:
import pandas as pd

data = pd.read_csv('veriler.csv')
#Veriler küçük harf formatına çevrildi.
new_Data = data['name'].str.lower()
print(new_Data)
#Verilerdeki noktalama işaretleri kaldırıldı.
new_Data1 = new_Data[:].str.replace('[^\w\s]','')
print(new_Data1)
#Verilerdeki metni kelimelere ayırdık
new_Data3 = data['name'].str.split()
print(new_Data3)

