import os
import requests
import telegram
from dotenv import load_dotenv
import random


def get_amount_of_comics():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    comics_amount = response['num']
    return comics_amount


def get_comic(comic_id):
    url = f'https://xkcd.com/{comic_id}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    comic_img_url = response['img']
    comic_name = response['title']
    comment = response['alt']
    comic_img = requests.get(comic_img_url)
    with open(f'{comic_name}.png', 'wb') as f:
        f.write(comic_img.content)
    return comic_name, comment


def post_random_comic(token, image_name, chat_id, comment):
    bot = telegram.Bot(token=token)
    with open(f'{image_name}.png', 'rb') as f: 
        bot.send_photo(chat_id=chat_id, photo=f, caption=comment)


def main():
    load_dotenv()
    token = os.environ['TG_TOKEN']
    chat_id = os.environ['GROUP_ID']
    try:
        comics_amount = get_amount_of_comics()
        comic_info = random.randint(1, comics_amount)
        image_name, comment = get_comic(comic_info)
        post_random_comic(token, image_name, chat_id, comment)
    finally:
        os.remove(f'{image_name}.png')


if __name__ == '__main__':
    main()