from nonebot import on_command,on_fullmatch
from nonebot.adapters.onebot.v11 import Message
from nonebot.params import CommandArg

from .netease_music_search import music_search

netease_music=on_command('网易云点歌',aliases={'点歌','music'})
@netease_music.handle()
async def _(args: Message=CommandArg()):
    msg=args.extract_plain_text().strip()
    if len(msg)<1:
        await netease_music.finish("参数错误！请参阅帮助")
    keyword=str(msg)
    try:
        music_msg=music_search(keyword)
    except:
        music_msg='查询失败！请稍后再试'
    await netease_music.finish(music_msg)


helpmsg=on_fullmatch(('?网易云点歌','?音乐','?点歌','?music'))
@helpmsg.handle()
async def _():
    await helpmsg.finish('【网易云点歌】\n'
                         '来点美妙的音乐吧！\n'
                         '用法（按照格式发送如下命令）：\n'
                         '(点歌 / 网易云点歌 / music) + [音乐名称]\n'
                         '（直接点歌，命令前需加斜杠）\n'
                         '(更多功能正在开发中)'
                         )