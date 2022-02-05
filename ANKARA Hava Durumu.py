from bs4 import BeautifulSoup
import requests
import datetime
import os


r = requests.get("http://www.havadurumu15gunluk.net/havadurumu/ankara-hava-durumu-15-gunluk.html")
soup = BeautifulSoup(r.content)
print("  ")
print("  ")
print("  ")
print("  ")
os.system("cls")
print(">>>>>>>>>>>>>>>>>>>>")
print("                    ")
print(" Ankara Hava Durumu ")
print("İnstagram : @bozk0rt")
print("                    ")
print(">>>>>>>>>>>>>>>>>>>>")

print("Kaç Derece: ")
find = soup.find("strong",attrs={"class":"strong2"})
print(find.text)

find2 = soup.find("strong",attrs={'class':'strong3'})
print("  ")
print("  ")
print("  ")
print("Durum : ")
print(find2.text)
print("  ")
print("  ")
print("  ")
#tarihler
trh = datetime.datetime.now()
ay = trh.month
yil = trh.year
gun = trh.day
print("Tarih: ", gun,ay,yil)