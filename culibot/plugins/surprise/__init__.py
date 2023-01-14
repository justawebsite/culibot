from random import randint
from nonebot.plugin import on_keyword

shima=on_keyword(keywords={'吗'})
@shima.handle()
async def sm_handle():
    num=randint(1,10)
    if num==1:
        await shima.finish('确实')
    elif num==2:
        await shima.finish('我觉得不是这样的')
