import random
from datetime import date

from nonebot.plugin import  on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

from nonebot import on_fullmatch

def luck_simple(num):
    if num < 18:
        return '大吉'
    elif num < 53:
        return '吉'
    elif num < 58:
        return '半吉'
    elif num < 62:
        return '小吉'
    elif num < 65:
        return '末小吉'
    elif num < 71:
        return '末吉'
    else:
        return '凶'


jrrp = on_command(cmd='rp',aliases={'jrrp','人品','rp'})


@jrrp.handle()
async def jrrp_handle(bot: Bot, event: Event):
    rnd = random.Random()
    rnd.seed(int(date.today().strftime("%y%m%d")) + int(event.get_user_id()))
    lucknum = rnd.randint(1, 100)
    await jrrp.finish(
        Message(f'[CQ:at,qq={event.get_user_id()}]您今日的幸运指数是{lucknum}/100（越低越好），为"{luck_simple(lucknum)}"'))

helpmsg=on_fullmatch(('?rp',"?今日人品","?人品","?jrrp"))
@helpmsg.handle()
async def _():
    await helpmsg.finish('【今日人品】\n'
                         '测一测你今天的人品如何？虽然有点迷信，但据说很准哦！\n'
                         '用法（发送如下任意命令）：\n'
                         'jrrp / 人品 / rp'
                         '（命令前需要带斜杠）'
                         )