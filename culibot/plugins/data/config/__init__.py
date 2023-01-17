# todo database的增删改查操作
# 此处大幅度地参考了setubot，向此项目的所有开发者致谢！
import json
from typing import Dict
from json import load, dump
from os import makedirs

from ..models import GroupConfig
from pathlib import Path

curPath = Path(__file__).parent


def getGroupConfig(groupID):
    # 获取群组的配置
    path = curPath / 'databases' / str(groupID) / 'config.json'
    if path.is_file():
        try:
            with open(path) as p:
                conf = load(p)
            return GroupConfig(**conf)
        except Exception as e:
            # TODO 读取失败后的反应
            return None
    return None


def buildGroupConfig(groupID):
    # 创建新群组档案
    #返回值相当于错误码

    path = curPath / 'databases' / str(groupID)
    if path.is_file():
        return False  #todo 此处我其实想做一个返回错误码什么的
    try:
        makedirs(path,exist_ok=True)
        with open(path/"config.json","w+") as f:
            json.dump(GroupConfig().json(),f)

        #todo 添加群员档案文件夹
        return True
    except Exception as e:
        return False

def saveGroupConfig(groupID,conf:Dict):
    path = curPath / 'databases' / str(groupID) / 'config.json'
    if path.is_file():
        try:
            with open(path) as f:
                json.dump(conf,f)
                return True
        except:
            return False
    else:
        return False


