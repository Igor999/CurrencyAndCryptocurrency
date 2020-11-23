import requests
import json
from ft import keys

class APIExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIExeption(f"Невозможно перевести одинаковые валюты {quote}")


        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIExeption(f'Не удалось определить валюту {quote}')


        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIExeption(f'Не удалось определить валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIExeption(f'Не удалось обработать количество {amount}')

        if amount < 0:
            raise APIExeption("Вы ввели отрицательное число")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * float(amount)
        return total_base