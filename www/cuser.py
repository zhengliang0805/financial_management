from coroweb import post
from apis import APIValueError
from musers import User
from models import next_id
from aiohttp import web
from handlers import user2cookies, COOKIE_NAME
import hashlib
import json


# 用户注册接口
@post('/api/user/registrar')
async def api_user_registrar(*, name, email, passwd):
    # 检查入参
    if not name:
        raise APIValueError('Invalid name')
    if not email:
        raise APIValueError('Invalid email')
    if not passwd:
        raise APIValueError('Invalid passwd')
    # 查询用户是否已注册
    users = await User.findAll('email=\'%s\'' % email)
    if len(users) > 0:
        raise APIValueError('register:failed', 'email', 'Email is already in use.')
    # 初始化用户信息并插入db
    uid = next_id()
    sha1_passwd = '%s:%s' % (id, passwd)
    user = User(id=uid, username=name, passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(), email=email)
    await user.save()
    # 构建response结构体
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookies(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r
