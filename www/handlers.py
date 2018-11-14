import re
import time
import hashlib
import logging
from users import User
from config import configs


COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret
# 正则表达式邮件, SHA1加密
_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')


async def cookies2user(cookies_str):
    '''
    Parse cookie and load user if cookie is valid.
    '''
    if not cookies_str:
        return None
    try:
        L = cookies_str.split('-')
        if len(L) != 3:
            return None
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return None
        user = await User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None
