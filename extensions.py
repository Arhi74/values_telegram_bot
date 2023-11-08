import requests
import json
from config import keys


class ConvertException(Exception):
    pass


class ValuesConverter:

    @staticmethod
    def get_prise(quote, base, amount):

        if quote == base:
            raise ConvertException('Валюты должны быть разные!')

        try:
            float(amount)
        except ValueError:
            raise ConvertException('Неправильно задано количество валюты')

        value_str = f'{keys.get(quote)}_{keys.get(base)}'
        api_key = '7402931417476eafe41b'
        req = requests.get(f'https://free.currconv.com/api/v7/convert?q={value_str}&compact=ultra&apiKey={api_key}')
        return json.loads(req.content).get(value_str) * amount
