from pydantic import BaseModel

class count(BaseModel):
    dk: int=0 #打卡

class groupInfo(BaseModel):
    count:count=count()

class GroupConfig(BaseModel):
    groupInfo:groupInfo=groupInfo()
