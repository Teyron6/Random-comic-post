import os
import requests
import telegram
from dotenv import load_dotenv
import random


def get_amount_of_comics():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response_json = response.json()
    comics_amount = response_json['num']
    return comics_amount


def get_comic(comic_id):
    url = f'https://xkcd.com/{comic_id}/info.0.json'
    response = requests.get(url)
    response_json = response.json()
    comic_img_url = response_json['img']
    comic_img = requests.get(comic_img_url)
    response.raise_for_status()
    with open(f'comics/{comic_id}.png', 'wb') as f:
        f.write(comic_img.content)
    return {'caption' : response_json['alt'],
            'image_id' : comic_id,
            }


def post_random_comic(token, comics_amount, chat_id):
    bot = telegram.Bot(token=token)
    comic_info = get_comic(random.randint(1, comics_amount))
    image_id = comic_info['image_id']
    with open(f'comics/{image_id}.png', 'rb') as f: 
        bot.send_photo(chat_id=chat_id, photo=f, caption=comic_info['caption'])
    os.remove(f'comics/{image_id}.png')


def main():
    load_dotenv()
    token=os.environ.get('TG_TOKEN')
    comics_amount = get_amount_of_comics()
    chat_id = os.environ.get('GROUP_ID')
    post_random_comic(token, comics_amount, chat_id)
    

if __name__ == '__main__':
    main()