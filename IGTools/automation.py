import json, re
from requests import Session
from .tools import payload, save

class Post:
    def __init__(self, session: Session, token: str) -> None:
        self.session = session 
        self.headers = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"','sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"23108RN04Y"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36','x-asbd-id': '359341','x-csrftoken': token}

    def like(self, post_id: str) -> bool:
        source = self.session.get('https://www.instagram.com').text
        data = payload(source=source)
        data.update({'fb_api_req_friendly_name':'usePolarisLikeMediaLikeMutation', 'variables': json.dumps({"media_id": str(post_id),"container_module":"single_post"}), 'doc_id': '23951234354462179'})
        post = self.session.post('https://www.instagram.com/graphql/query', data=data, headers=self.headers).text

        if 'status":"ok"' in post: return True 
        else: return False

    def scrape(self, cursor: str = None) -> dict:
        source = self.session.get('https://www.instagram.com').text
        data = payload(source=source)
        data.update({'fb_api_req_friendly_name': 'PolarisFeedRootPaginationCachedQuery_subscribe','variables': json.dumps({"after": cursor,"before": None,"data": {"device_id": "44EC41CC-42E5-42E2-8A09-DA64530E08B4","is_async_ads_double_request": "0","is_async_ads_in_headload_enabled": "0","is_async_ads_rti": "0","rti_delivery_backend": "0","feed_view_info": [{"media_id": '',"media_pct": 1,"time_info": {"10": 1327,"25": 1327,"50": 1327,"75": 1327},"version": 24}]},"first": 12,"last": None,"variant": "home","__relay_internal__pv__PolarisIsLoggedInrelayprovider": True,"__relay_internal__pv__PolarisShareSheetV3relayprovider": True}),'doc_id': '9818107414934772'})
        post = self.session.post('https://www.instagram.com/graphql/query', data=data, headers=self.headers).text

        get = lambda pattern: re.search(pattern, post)
        username = re.findall(r',"transparency_label":.*?,"username":"(.*?)","ai_agent', post)
        user_id = re.findall(r'"owner":\{"pk":"(.*?)"', post)
        post_id = re.findall(r'\{"media":\{"id":"(.*?)_.*?"', post)
        post_url = re.findall(r'"code":"(.*?)"', post)
        caption = re.findall(r'"pk":".*?","text":"(.*?)"', post)
        comment_count = re.findall(r'"comment_count":(.*?),', post)
        like_count = re.findall(r'"story_cta":null,"like_count":(.*?),', post)

        data = [{'user':{'username': uname__, 'user_id': uid__}, 'post_id': pid__, 'post_url': purl__, 'caption': cptn__, 'comment_count': cmc__, 'like_count': lkc__} for pid__, purl__, cptn__, cmc__, lkc__, uname__, uid__ in zip(post_id, post_url, caption, comment_count, like_count, username, user_id)]
        cursor = get(r'"page_info":{"has_next_page":true,"end_cursor":"(.*?)"')

        return {'cursor': cursor.group(1) if cursor else None, 'data': data}

