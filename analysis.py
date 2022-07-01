print("АНАЛИЗ РЕСТАВРАЦИОННЫХ РАБОТ ПО СОХРАНЕНИЮ ОБЪЕКТОВ КУЛЬТУРНОГО НАСЛЕДИЯ В САНКТ-ПЕТЕРБУРГЕ")


from bs4 import BeautifulSoup
import requests

url = 'https://kgiop.gov.spb.ru/deyatelnost/restoration/' #Сохраняю URL в переменную
page = requests.get(url) #Отправляю GET()-запрос на сайт и сохраняю полученное в переменную 'page'

print(page.status_code) #Проверяю подключение

filteredNews = []
allNews = []

soup = BeautifulSoup(page.text, "html.parser")

print(soup)

allNews = soup.findAll('table border="1')

for data in allNews:
    if data.find('p', 'a') is not None:
        filteredNews.append(data.text)

for data in filteredNews:
    print(data)


print("В период с 2004 по 2022 год была проведена комплексная реконструкция более 3,5 тысяч ОКН.На рисунке "
      "\nприведены результаты проведения анализа реставрации существующих объектов ОКН в г. Санкт-Петербург с 2015 "
      "\nпо 2017 гг. По произведённому анализу видно, что в настоящее время проблема сохранения объектов "
      "\nкультурного наследия достаточно актуальна. Наблюдается рост количества отреставрированных объектов "
      "\nкультурного наследия с 2015 по 2017 гг.Количество объектов, подлежащих реставрации почти не изменяется.")