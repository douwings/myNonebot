import os
import time
from use.test.qq.plugins.work.object_recognize import ImgRecognize

def clockOut():
    unlock()
    # 截图
    os.system('adb exec-out screencap -p > d:/dingimg/1.png')
    time.sleep(2)

    source = r'D:\dingimg\1.png'
    clock = r'D:\dingimg\clock.png'
    clockOut = r'D:\dingimg\clockOut.png'
    work = r'D:\dingimg\work.png'

    try:
        flag = False
        for i in range(10):
            if getCoordinates(source,clockOut):
                coClockOut = getCoordinates(source, clockOut)
                os.system('adb shell input tap {} {}'.format(coClockOut[0], coClockOut[1]))
                time.sleep(2)
                flag = True
                break
                # time.sleep(1)
                # os.system('adb exec-out screencap -p > d:/dingimg/1.png')
                # time.sleep(2)
                # if not getCoordinates(source,clockOut):
                #     break
            elif getCoordinates(source,clock):
                coClock = getCoordinates(source, clock)
                os.system('adb shell input tap {} {}'.format(coClock[0], coClock[1]))
                time.sleep(3)
                os.system('adb exec-out screencap -p > d:/dingimg/1.png')
                time.sleep(1)
            elif getCoordinates(source,work):
                coWork = getCoordinates(source, work)
                os.system('adb shell input tap {} {}'.format(coWork[0], coWork[1]))
                time.sleep(3)
                os.system('adb exec-out screencap -p > d:/dingimg/1.png')
                time.sleep(1)
            else:
                os.system('adb shell input keyevent 26')
                time.sleep(2)
                unlock()
                os.system('adb exec-out screencap -p > d:/dingimg/1.png')
                time.sleep(2)


        # 关闭钉钉进程
        os.system('adb shell am force-stop com.alibaba.android.rimet')
        time.sleep(1)
        os.system('adb shell input keyevent 26')
        return flag
    except Exception as e:
        print(e)
        os.system('adb shell input keyevent 26')
        return False





def unlock():
    # 解锁手机
    os.system('adb shell input keyevent 26')
    time.sleep(1)
    os.system('adb shell input swipe 500 1500 500 800')
    time.sleep(1)

    # 关闭钉钉进程
    os.system('adb shell am force-stop com.alibaba.android.rimet')
    time.sleep(1)

    # 打开钉钉
    os.system('adb shell am start -n com.alibaba.android.rimet/.biz.LaunchHomeActivity')
    time.sleep(3)

def getCoordinates(source,search):
    ir = ImgRecognize(im_source=source, im_search=search)
    rect = ir.find_one_template()
    # print(search)
    # print(rect)
    if len(rect):
        # ir.mark_in_source(rect)
        return rect[0]['result']
    else:
        return False