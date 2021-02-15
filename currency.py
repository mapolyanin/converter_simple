#pylint:disable=E0602
from bs4 import BeautifulSoup
from decimal import Decimal
import requests





def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get("https://www.cbr.ru/scripts/XML_daily.asp",
                                               params={'date_req': date})  
    soup = BeautifulSoup(response.text, 'lxml')
    catalog = {'RUR':[1, Decimal('1.0000')]}
    for tag in soup.find_all('valute'):
        catalog [tag.charcode.get_text()] = [int(tag.nominal.get_text()), Decimal(tag.value.get_text().replace(',', '.'))]
     
    rur = Decimal(Decimal(amount) * catalog[cur_from][1] / catalog[cur_from][0])
    #print('rur: ', rur)
    result = Decimal(rur*(catalog[cur_to][0]/catalog[cur_to][1])).quantize(Decimal("1.0000"))
    #print ('result: ', result)
    
    #print(catalog)
    
    
    return result  # не забыть про округление до 4х знаков после запятой
    
    
    
    
    
    
    
