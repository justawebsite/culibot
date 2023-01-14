import requests
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot import logger
def music_search(keyword):
    res=requests.get(f"https://music.163.com/api/cloudsearch/pc?s={keyword}&type=1&offset=0").json()['result']['songs'][0]
    logger.info(res['id'])
    return MessageSegment.music('163',res['id'])
