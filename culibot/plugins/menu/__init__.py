from nonebot import on_command,on_fullmatch

menu = on_command('menu', aliases={'菜单', '醋栗菜单'})


@menu.handle()
async def _():
    await menu.finish('醋栗菜单v1.0\n'
                      '在功能前加\"?\"查询用法哦！\n'
                      '已启用的功能：\n'
                      '今日人品\n'
                      '摸鱼人日历\n'
                      '天气\n'
                      '（更多功能正在开发中！）')

helpmsg = on_fullmatch(('?menu','?菜单','?醋栗菜单'))

@helpmsg.handle()
async def _():
    await helpmsg.finish('【醋栗菜单】\n'
                         '汇总所有当前可用的功能！\n'
                         '用法（发送如下任意命令）：\n'
                         '菜单 / 醋栗菜单 / menu (命令前需加斜杠)'
                         )
