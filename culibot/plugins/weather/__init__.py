from typing import Tuple

from .getWeatherMsg import getMsg
from nonebot import on_command
from nonebot import on_fullmatch
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Message
from nonebot.params import RegexGroup
weatherCom=on_command("天气")

@weatherCom.handle()
async def _(args: Message=CommandArg()):
    msg= args.extract_plain_text().strip().split()
    if len(msg)<1:
        await weatherCom.finish('参数错误！请查看帮助')

    city =msg[0]
    try:
        text = getMsg(str(city))

    except:
        text='获取失败！请稍后再试'
    await weatherCom.finish(Message(text))




helpmsg=on_fullmatch(('?天气',))
@helpmsg.handle()
async def _():
    await helpmsg.finish('【天气】\n'
                         '发送所指定城市当日的天气详情！\n'
                         '用法（按照格式发送如下命令）：\n'
                         '天气 [城市名] (命令前需加斜杠)'
                         )