from nonebot import on_command, CommandSession,on_natural_language,NLPSession
import os
import sys
from use.test.qq.plugins.work import clockIn
from use.test.qq.plugins.work import clockOut
from use.test.qq.plugins.work import clear
from nonebot import permission as per

@on_natural_language(keywords={'紫翼上班打卡'}, only_to_me=True, permission=per.SUPERUSER)
async def clockInF(session: CommandSession):
    if clockIn.clockIn():
        await session.send('打卡成功')
    else:
        await session.send('打卡失败')


@on_natural_language(keywords={'紫翼下班打卡'}, only_to_me=True, permission=per.SUPERUSER)
async def clockOutF(session: CommandSession):
    # os.system(r'{py} E:\BaiduNetdiskDownload\wings\py\clockIn\clockOut.py'.format(py=sys.executable))
    if clockOut.clockOut():
        await session.send('打卡成功')
    else:
        await session.send('打卡失败')


@on_natural_language(keywords={'点击home'}, only_to_me=True, permission=per.SUPERUSER)
async def clockOutF(session: CommandSession):
    os.system('adb shell input keyevent 26')
    # if clockOut.clockOut():
    #     await session.send('打卡成功')
    # else:
    #     await session.send('打卡失败')

@on_natural_language(keywords={'清除障碍信息'}, only_to_me=True, permission=per.SUPERUSER)
async def clearErr(session: CommandSession):
    if clear.clear():
        await session.send('已清除')
    else:
        await session.send('未发现已知障碍，已截图，请手动录入')
        os.system('adb exec-out screencap -p > d:/dingimg/2.png')