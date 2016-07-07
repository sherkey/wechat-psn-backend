# -*- coding:utf-8 -*-
# import werobot

# #robot = werobot.WeRoBot(token='robot', enable_session=True, session_storage=saekvstorage.SaeKVDBStorage())
# #robot = werobot.WeRoBot(token='testrobot', enable_session=True, session_storage=filestorage.FileStorage())
# robot = werobot.WeRoBot(token='testrobot', enable_session=True)

# @robot.subscribe
# def subscribe(message):
#     return '欢迎关注本公众号！'

# @robot.handler
# def echo(message):
#     return 'hello'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import werobot
import gevent.monkey;

gevent.monkey.patch_all()
from werobot.reply import ArticlesReply, Article

robot = werobot.WeRoBot(token='testrobot', enable_session=True)

import re
from werobot.reply import ArticlesReply, Article
from RobotHandle import RobotHandle


@robot.filter(re.compile(r"^\?.*"))
def search(message, session):
    s = message.content
    searchstr = str(s).replace('?', '')
    handle = RobotHandle(message, session)
    return handle.search(searchstr)


@robot.filter(re.compile(r'^category\s*$', re.I))
def category(message, session):
    handel = RobotHandle(message, session)
    return handel.get_category()


@robot.filter(re.compile(r'^recent\s*$', re.I))
def recent(message, session):
    handel = RobotHandle(message, session)
    return handel.get_recent_posts()


@robot.filter(re.compile('^category\-.*$', re.I))
def categorypost(message, session):
    handel = RobotHandle(message, session)
    cate = str(message.content).replace('Category', '').replace('category', '').replace('-', '')

    return handel.get_category_posts(cate)


@robot.filter(re.compile('^weather\:.*$', re.I))
def weather(message, session):
    handel = RobotHandle(message, session)
    cate = str(message.content).replace('weather', '').replace('Weather', '').replace(':', '')

    return handel.weather(cate)


@robot.filter(re.compile('^idcard\:.*$', re.I))
def idcard(message, session):
    handel = RobotHandle(message, session)
    cate = str(message.content).replace('idcard', '').replace('Idcard', '').replace(':', '')

    return handel.idcard(cate)
@robot.filter(re.compile('^music\:.*$', re.I))
def music(message,session):
    handel = RobotHandle(message, session)
    cate = str(message.content).replace('music', '').replace('Music', '').replace(':', '')

    return handel.music(cate)


"""
#中文问号
def s(message):
    s=message.content
    blogapi=blog()
    ask='？'
    ask=ask.decode('utf-8')
    articles=blogapi.Search(str(s.replace(ask,'')))
    if len(articles) ==0:
        return str(s).replace('？','')+' 没有搜索到文章哦'
    reply = ArticlesReply(message=message)
    for article in articles:
        reply.add_article(article)

    return reply



"""


@robot.text
def deal(message):
    content = message.content
    ask = '？'
    ask = ask.decode('utf-8')
    if message.content.find(ask) == 0:
        searchstr = str(content.replace(ask, ''))
        if searchstr == '':
            return '请在?后面加上要搜索的关键字哦'


@robot.subscribe
def sub(message,session):
    handel = RobotHandle(message, session)
    return handel.helpinfo()


@robot.filter(re.compile('help', re.I))
def help(message,session):
    handel = RobotHandle(message, session)
    return handel.helpinfo()


@robot.text
@robot.handler
def echo(message,session):
    handel = RobotHandle(message, session)
    info=message.content
    return handel.tuling(info)
    
robot.run(server='cherrypy',host='0.0.0.0',port=80)
