from nonebot import on_command, CommandSession,on_natural_language,NLPSession
from use.test.qq.plugins.work import clockIn
from use.test.qq.plugins.work import clockOut
import urllib.request
import requests
import json
from nonebot import permission as per

@on_natural_language(keywords={'天气'}, only_to_me=False, permission=per.EVERYBODY)
async def weather(session: CommandSession):
    text = str(session.ctx['message'])
    city = text.split('天气')
    weather = await get_weather(city[0] or '深圳')
    await session.send(weather)

async def get_weather(city):
    host = 'http://wthrcdn.etouch.cn/weather_mini?city='
    url = host + urllib.parse.quote(city)
    r = requests.get(url)
    jsons = json.loads(r.text)
    str = city + 'now的天气：\n'
    len = 0
    for i in jsons['data']['forecast']:
        if len < 2:
            if len == 0: str += '今日：'
            if len == 1: str += '明日：'
            str += i['date']
            str += '\n天气：'
            str += i['type']
            str += '\n最'
            str += i['low']
            str += '\n最'
            str += i['high']
            str += '\n'
            len += 1
    return str



@on_natural_language(keywords={'笑话'}, only_to_me=False, permission=per.EVERYBODY)
async def joke(session: CommandSession):
    pass
    # os.system(r'{py} E:\BaiduNetdiskDownload\wings\py\clockIn\clockOut.py'.format(py=sys.executable))
    # if clockOut.clockOut():
    #     await session.send('打卡成功')
    # else:
    #     await session.send('打卡失败')
