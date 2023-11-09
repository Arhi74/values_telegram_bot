import requests
import json
from config import keys


class APIException(Exception):
    pass


class ValuesConverter:

    @staticmethod
    def get_prise(quote, base, amount):

        if not keys.get(quote):
            raise APIException(f'Не найдена валюта {quote}!\nСписок доступных валют можно вывести командой /values')

        if not keys.get(base):
            raise APIException(f'Не найдена валюта {base}!\nСписок доступных валют можно вывести командой /values')

        if quote == base:
            raise APIException('Валюты должны быть разные!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException('Неправильно задано количество валюты')

        value_str = f'{keys.get(quote)}_{keys.get(base)}'
        api_key = '7402931417476eafe41b'
        req = requests.get(f'https://free.currconv.com/api/v7/convert?q={value_str}&compact=ultra&apiKey={api_key}')
        if req.status_code != 200:
            raise APIException('Возникли проблемы с API')
        return json.loads(req.content).get(value_str) * amount
