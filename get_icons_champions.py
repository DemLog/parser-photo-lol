import os
import requests

from procesing_name import process_card_name, get_champions

url = "https://www.leagueoflegends.com/en-us/champions/"


def get_icons_champions():
    output_folder = 'images/icons'
    os.makedirs(output_folder, exist_ok=True)

    champions = get_champions()

    len_champ = len(champions)
    len_images = 0

    for champion in champions:
        test = False

        image_url = "https://ddragon.leagueoflegends.com/cdn/14.6.1/img/champion/"
        for iu in process_card_name(champion):
            image_response = requests.get(image_url + iu + ".png")
            if image_response.status_code == 200:
                image_path = os.path.join(output_folder, f"{iu}.png")
                with open(image_path, 'wb') as file:
                    file.write(image_response.content)
                print(f"Сохранено изображение: {image_path}")
                len_images += 1
                test = True
                break
            else:
                continue

        if not test:
            print(f"Не удалось сохранить изображение: {champion}")

    print(f"Чемпионов: {len_champ}, фоток: {len_images}")
