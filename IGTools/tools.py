import re 

save = lambda source: open('/sdcard/source.html', 'w').write(str(source))

def payload(source: str) -> dict:
    try:
        get = lambda pattern: re.search(pattern, str(source)).group(1)
        return {
            'av': get(r'actorID":"(.*?)"'),
            '__d': 'www',
            '__user': '0',
            '__a': '1',
            '__req': '1g',
            '__hs': get(r'"haste_session":"(.*?)"'),
            'dpr': '3',
            '__ccg': 'POOR',
            '__rev': get(r'client_revision":(.*?),'),
            '__s': '',
            '__hsi': get(r'hsi":"(.*?)"'),
            '__comet_req': '7',
            'fb_dtsg': get(r'DTSGInitData",\[\],{"token":"(.*?)"'),
            'jazoest': get(r'jazoest=(.*?)",'),
            'lsd': get(r'LSD",\[\],{"token":"(.*?)"'),
            '__spin_r': get(r'__spin_r":(.*?),'),
            '__spin_b': 'trunk',
            '__spin_t': get(r'__spin_t":(.*?),'),
            '__crn': 'comet.igweb.PolarisFeedRoute',
            'fb_api_caller_class': 'RelayModern',
            'server_timestamps': 'true',
        }
    except Exception as e:
        return {}
