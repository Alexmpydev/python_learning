#
#
#
# Подключитесь к API НБУ ( документация тут https://bank.gov.ua/ua/open-data/api-dev ),
# получите текущий курс валют и запишите его в TXT-файл в таком формате:
#  "[дата создания запроса]"
# 1. [название ввалюты 1] to UAH: [значение курса к валюте 1]
# 2. [название ввалюты 2] to UAH: [значение курса к валюте 2]
# 3. [название ввалюты 3] to UAH: [значение курса к валюте 3]


# n. [название ввалюты n] to UAH: [значение курса к валюте n]
# 2. * Пользователь вводит название валюты и дату, программа возвращает пользователю курс гривны к
# этой валюте за указаную дату используя API НБУ. Формат ввода пользователем данных - на ваше усмотрение.
# Реализовать с помощью ООП!
#
#
#
# p.s. ну и как обычно, чистота, лаконичность и информативность - наше все!

from datetime import date as d_
from requests import request
import json


class NbuAccess:
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange'

    def __init__(self, date=d_.today(), currency: str = 'USD', url: str = url):
        self.date = date
        self.currency = currency
        self.url = url

    def __str__(self):
        return f'Текущий курс гривны к {self.currency}, на дату {self.date}'

    def get_all_rates(self):
        req = self.url + '?json'
        with open('nbu_rates.txt', 'a') as f:
            try:
                result = request('GET', req, timeout=3)
                parse = json.loads(result.text)
                print(parse)
                for index in range(len(parse)):
                    for key in parse[index]:
                        if key == 'txt' or key == 'rate':
                            f.write(f'{parse[index][key]}\n')
            except Exception as e:
                print('Exception!', e)

    def get_rate(self):
        user_date = input('Введите дату в формате yyyymmdd \n')
        user_curr = input('Введите валюту в формате usd или aud \n')

        if not user_date:
            strdate = self.date.strftime("%Y%m%d")
        else:
            strdate = user_date

        if not user_curr:
            curr = self.currency
        else:
            curr = user_curr

        req = self.url + f'?valcode={curr}&date={strdate}&json'
        try:
            result = request('GET', req, timeout=3)
            parse = json.loads(result.text)
            print(f"Курс {parse[0]['txt']} - {parse[0]['rate']} на дату {parse[0]['exchangedate']}")

        except Exception as e:
            print('Exception!', e)

        # if 300 > result.status_code >= 200:
        #     with open('python_logo.png', 'wb') as file:
        #         file.write(result.content)


r1 = NbuAccess()
# r1.get_rate()
r1.get_all_rates()

