import requests
import os
from nonebot import logger
from nonebot import on_command
apiKey="1c95adf561754718a3777ec40f663d79"
def getCityLocation(city:str):

    geoUrl='https://geoapi.qweather.com/v2/city/lookup?'
    res=requests.get(f"{geoUrl}location={city}&key={apiKey}").json()
    logger.debug(apiKey)
    logger.debug(str(res))
    cityName = res['location'][0]['id']
    return cityName

def getMsg(city:str):
    try:

        weaUrl = "https://devapi.qweather.com/"
        cityId=getCityLocation(city)
        res = requests.get(f"{weaUrl}v7/weather/3d?location={cityId}&key={apiKey}").json()
        data = res['daily'][0]
        Tdate = data['fxDate']
        sunrise = data['sunrise']
        sunset = data['sunset']
        textDay = data['textDay']
        moonPhase = data['moonPhase']
        tempMax = data['tempMax']
        tempMin = data['tempMin']
        windDirDay = data['windDirDay']
        windScaleDay = data['windScaleDay']
        vis = data['vis']
        text = f"[CQ:face,id=144]{Tdate}天气预报[CQ:face,id=144]\n" \
               f"  天气：{textDay}\n" \
               f"  温度：{tempMin}°C ~ {tempMax}°C\n" \
               f"  风向风力：{windDirDay} {windScaleDay}级\n" \
               f"  能见度指数：{vis}\n" \
               f"  日出时间：{sunrise}\n" \
               f"  日落时间：{sunset}\n" \
               f"  月相：{moonPhase}"
        logger.debug(text)
        return text
    except:
        return ""
