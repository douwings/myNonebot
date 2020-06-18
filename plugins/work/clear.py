import os
import time
from use.test.qq.plugins.work.object_recognize import ImgRecognize

def clear():
    unlock()
    # 截图
    os.system('adb exec-out screencap -p > d:/dingimg/1.png')
    time.sleep(2)

    source = r'D:\dingimg\1.png'
    shaohou = r'D:\dingimg\shaohou.png'
    quxiao = r'D:\dingimg\quxiao.png'

    try:
        flag = False
        for i in range(10):
            if getCoordinates(source,shaohou):
                coShaohou = getCoordinates(source, shaohou)
                os.system('adb shell input tap {} {}'.format(coShaohou[0], coShaohou[1]))
                time.sleep(2)
                flag = True
                break
            elif getCoordinates(source,quxiao):
                coQuxiao = getCoordinates(source, quxiao)
                os.system('adb shell input tap {} {}'.format(coQuxiao[0], coQuxiao[1]))
                time.sleep(2)
                flag = True
                break

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


def getCoordinates(source,search):
    ir = ImgRecognize(im_source=source, im_search=search)
    rect = ir.find_one_template()
    if len(rect):
        # ir.mark_in_source(rect)
        return rect[0]['result']
    else:
        return False