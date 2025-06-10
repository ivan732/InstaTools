import os, random, time, json 
from IGTools import Instagram
from IGTools.automation import Post 
from datetime import datetime
from requests.exceptions import ConnectionError, ChunkedEncodingError

os.system('clear')
print('Login to instagram using cookie!!!')
print('Coded by ./Meizug\n\n')

cookie = input('Add your cookie: ')
instagram = Instagram(cookie=cookie)
post_obj = Post(session=instagram.session, token=instagram.token)

print()
while True:
    try:
        scrape_post_data = post_obj.scrape(cursor=None)
        for post in scrape_post_data['data']:
            try:
                like_response = post_obj.like(post_id=post['post_id'])
                if like_response:
                    print(f'LOG [{post["user"]["username"]}|{post["post_url"]}] {post["post_id"]} ->> ❤️ [{datetime.now().strftime("%H:%M %Ssec %d/%m/%Y")}]')

                time.sleep(random.randint(35, 60))
            except (ConnectionError, ChunkedEncodingError):
                time.sleep(random.randint(15, 30))
    except (ConnectionError, ChunkedEncodingError):
        time.sleep(random.randint(15, 30))
