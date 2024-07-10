import os

import requests

from procesing_name import process_card_name, get_champions


def get_splash_champions():
    champions = get_champions()

    len_champ = len(champions)
    len_images = 0

    for champion in champions:
        count_photo = 0

        image_url = "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/"
        for iu in process_card_name(champion):
            for x in range(0, 50):
                image_response = requests.get(image_url + f"{iu}_{x}.jpg")
                if image_response.status_code == 200:
                    output_folder = f'images/splash/{iu}'
                    os.makedirs(output_folder, exist_ok=True)
                    image_path = os.path.join(output_folder, f"{iu}_{x}.jpg")
                    with open(image_path, 'wb') as file:
                        file.write(image_response.content)
                    print(f"Сохранено изображение: {image_path}")
                    len_images += 1
                    count_photo += 1
                else:
                    break

        print(f"Сохранено splash для {champion}: {count_photo}")

    print(f"Чемпионов: {len_champ}, фоток: {len_images}")
