import requests
import re
from .tools import save, payload
from .automation import Post

class Instagram:
    def __init__(self, cookie: str) -> None:
        self.session = requests.session()
        self.session.cookies['cookie'] = cookie

        src = self.session.get('https://www.instagram.com/').text
        self.token = re.search(r'"csrf_token":"(.*?)"', src).group(1)

    def like(self, post_id: str) -> bool:
        obj = Post(session=self.session, token=self.token)
        return obj.like(post_id=post_id)

    def scrape_post(self):
        obj = Post(session=self.session, token=self.token)
        return obj.scrape()

