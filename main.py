from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re


url = "https://corona-live.com/sitemap.xml/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)

driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

today = []
total = []
total_d = []
city = soup.select('td.c-fWUTTQ.c-fWUTTQ-fYeKAw-shadow-true.c-fWUTTQ-cOWTvr-centered-true.c-fWUTTQ-ihKxHaz-css > a > div > div.c-PJLV')
c_data = soup.find_all('div',{'class':'c-grmDeR'})

city_csv=[]
total_csv=[]
today_csv=[]
total_d_csv=[]
city_data=[]
for i in c_data:
    today = c_data[::5]
    total = c_data[1::5]
    total_d = c_data[2::5]

for a,b,c,d in zip(city,today,total,total_d):
    city_csv = a.get_text()
    today_csv = b.get_text()
    total_csv = c.get_text()
    total_d_csv = d.get_text()
    city_data.append([city_csv,today_csv,total_csv,total_d_csv])

df=pd.DataFrame(np.array(city_data), columns=["지역","오늘 확진자","총 확진자", "총 사망자"])
df.to_csv('C:\\Users\\ksk03\\PycharmProjects\\Web\\data_df.csv', sep=',',encoding='utf-8-sig')


