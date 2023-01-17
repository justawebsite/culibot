import traceback

from nonebot import on_command
from nonebot.adapters.cqhttp import Bot,GroupMessageEvent
from pathlib import Path
from ..data import buildGroupConfig



setup=on_command("setup",aliases={"安装",})
@setup.handle()
async def _(bot:Bot,message:GroupMessageEvent):
    groupid=str(message.group_id)
    try:
        buildGroupConfig(groupid)
        text="创建档案成功！"

    except Exception as e:
        text=str(e)
        traceback.print_exc()
    await setup.finish(text)