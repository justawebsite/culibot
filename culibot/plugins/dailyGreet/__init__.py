from nonebot import require
from random import randint
require("nonebot_plugin_apscheduler")
from nonebot import get_bots
from nonebot_plugin_apscheduler import scheduler

groups = [703445354,778986873]
morninggreet=[
    '按时睡觉身体好哦~','睡觉了睡觉了','月亮不睡我不睡','事已至此，先睡觉吧','晚安哦各位',
    '不为不值得的东西花钱，不为不值得的事情失眠',
    '熬夜一时爽...',
    '别睡太晚 梦会变短',
    'Throw your sad feelings into outer space and cover yourself. Good night.',
    'The bed is warm. When will you come.',
    '别熬夜了，对手机不好'
]
nightgreet=[
    '起床啦起床啦','一日之计在于晨呐！早安！','各位草上好','澡啊',
    '早安打工人!'
]
@scheduler.scheduled_job("cron", day_of_week='*', hour=22, minute="10")
async def goodnight():
    (bot,) = get_bots().values()
    msg=morninggreet[randint(0,len(morninggreet)-1)]
    for i in groups:
        await bot.send_msg(
            message_type='group',
            group_id=i,
            message=msg
        )

@scheduler.scheduled_job("cron", day_of_week='*', hour=6, minute="40")
async def goodmorning():
    (bot,) = get_bots().values()
    msg = nightgreet[randint(0, len(nightgreet) - 1)]
    for i in groups:
        await bot.send_msg(
            message_type='group',
            group_id=i,
            message=msg
        )
