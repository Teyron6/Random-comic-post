import os
import requests
import telegram
from dotenv import load_dotenv
import random


def get_comic(comic_id):
    url = f'https://xkcd.com/{comic_id}/info.0.json'
    response = requests.get(url)
    response_json = response.json()
    comic_img_url = response_json['img']
    print(comic_img_url)
    comic_img = requests.get(comic_img_url)
    response.raise_for_status()
    with open(f'comics/{comic_id}.png', 'wb') as f:
        f.write(comic_img.content)
    print(response_json['alt'])
    return {'caption' : response_json['alt'],
            'image_id' : comic_id,
            }


def post_random_comic():
    bot = telegram.Bot(token=os.environ.get('TG_TOKEN'))
    comic_info = get_comic(random.randint(1, 2988))
    image_id = comic_info['image_id']
    bot.send_photo(chat_id=os.environ.get('GROUP_ID'), photo=open(f'comics/{image_id}.png', 'rb'), caption=comic_info['caption'])
    os.remove(f'comics/{image_id}.png')


def main():
    load_dotenv()
    post_random_comic()


if __name__ == '__main__':
    main()