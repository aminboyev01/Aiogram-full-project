# # import googletrans as gl
import requests
from bs4  import BeautifulSoup
# # matn="salom dunyo men yashayapman"
# # tarjima=gl.Translator()
# # tarji=tarjima.translate(matn)
# # print(tarji.text)
#
#
# from pprint import pprint
# manzil="https://kun.uz"
# r=requests.get(manzil)
# pprint(r.text)
# Api_key='e816761036d64133e49011fd'
# curren='USD'
# url=f"https://v6.exchangerate-api.com/v6/{Api_key}/pair/{curren}/UZS"
# respons=requests.get(url)
# kurs=respons.json()["conversion_rate"]
# print(f"1 dolllar kursi: {kurs}")
#
#


sahifa="https://cbu.uz/uz/"
r=requests.get(sahifa)
soup=BeautifulSoup(r.text,'html.parser')
news=soup.find_all(class_='exchange__item_value')
print(news[0].text)





