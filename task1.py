import requests
from jinja2 import Template
import xml.etree.ElementTree as ET

URL = "https://www.cbr.ru/scripts/XML_daily.asp"

def get_exchange_rates():
    response = requests.get(URL)
    tree = ET.fromstring(response.text)
    rates = {}

    for currency in tree.findall('Valute'):
        code = currency.find('CharCode').text
        rate = float(currency.find('Value').text.replace(',', '.'))
        nominal = int(currency.find('Nominal').text)
        rates[code] = rate / nominal
    
    return {
        'USD': rates['USD'],
        'EUR': rates['EUR'],
        'CNY': rates['CNY']
    }

template_text = """{{ rubles }} рубль = {{ usd | round(2) }} USD = {{ eur | round(2) }} EUR = {{ cny | round(2) }} CNY"""
template = Template(template_text)

rubles = float(input("Введите сумму в рублях: "))

rates = get_exchange_rates()
data = {
    'rubles': rubles,
    'usd': rubles / rates['USD'],
    'eur': rubles / rates['EUR'],
    'cny': rubles / rates['CNY']
}

output = template.render(data)
print(output)
