import itertools
import re

import requests
from bs4 import BeautifulSoup


def get_champions():
    url = "https://www.leagueoflegends.com/en-us/champions/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return [div.text for div in soup.find_all('div', class_='sc-ce9b75fd-0 lmZfRs', attrs={'data-testid': 'card-title'})]
    else:
        print(f"Не удается получить доступ к сайту. Код ошибки: {response.status_code}")


def process_card_name(card_name):
    # Словарь специальных случаев
    special_cases = {
        "Nunu & Willump": "Nunu",
        "Wukong": "MonkeyKing",
        "Renata Glasc": "Renata",
        "Jarvan IV": "JarvanIV",
        "Dr. Mundo": "DrMundo"
    }

    if card_name in special_cases:
        return [special_cases[card_name]]

    card_name = re.sub(r'([A-Za-z])([A-Za-z]*)', lambda x: x.group(1).upper() + x.group(2).lower(), card_name).replace(
        ' ', '')

    if "'" in card_name:
        parts = card_name.split("'")
        base_name = parts[0]
        combinations = []

        # Создание всех возможных комбинаций
        for combination in itertools.product(*((part.capitalize(), part.lower()) for part in parts[1:])):
            combined = base_name + ''.join(combination)
            combinations.append(combined)

        return combinations

    return [card_name]
