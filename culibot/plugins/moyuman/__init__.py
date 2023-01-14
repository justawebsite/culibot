import requests
from nonebot import on_command
from nonebot import on_fullmatch
from nonebot import logger
from nonebot.adapters.onebot.v11 import MessageSegment
from datetime import date
import json
import os

# 将图片下载到“moyupic”文件夹中


moyuman=on_command('moyuren',aliases={'摸鱼人日历','摸鱼人','摸鱼',"moyu"})
@moyuman.handle()
async def _():
    response = requests.get('https://api.vvhan.com/api/moyu?type=json').json()
    imgurl = response['url']
    logger.debug(imgurl)
    await moyuman.send(MessageSegment.image(imgurl))

helpmsg=on_fullmatch(('?摸鱼人日历','?摸鱼','?摸鱼人','?moyu'))
@helpmsg.handle()
async def _():
    await helpmsg.finish('【摸鱼人日历】\n'
                         '调用此功能即会发送一张当日的摸鱼人日历图片！今天你摸鱼了吗？\n'
                         '用法（发送如下任意命令）：\n'
                         '摸鱼人日历 / 摸鱼 / 摸鱼人 / moyu (命令前需加斜杠)'
                         )