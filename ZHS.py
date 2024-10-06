import pyautogui
import time

# ##############1.采集实例样本#########################
def CJ():
    #截图整个屏幕
    x=11
    y=948
    w=43
    h=977
    scope = (x,y,w,h)
    #pyautogui.moveTo(802,576)
    im = pyautogui.screenshot()
    #扣取实例图像，可用pyautogui.moseInfo()获取坐标点位
    #pyautogui.mouseInfo()
    om = im.crop(scope)      #pyautogui.mouseInfo()
    #保存实列图像
    om.save("SF3.png")


# ################2.识别实例样本#########################
# def zan():
#     #寻找实列图像
#     time.sleep(0.5)
#     xy = pyautogui.locateOnScreen('img.png')
#     print(xy)
#     #获取图像中心位置
#     center = pyautogui.center(xy)
#     #单击
#     pyautogui.click(center)
#     print("成功")

# while True:
#     try:
#         zan()
#     except:
#         pyautogui.scroll(-500)
#         print("未找到目标。")
#         quit()


#############1.书法##################
###1.1进入对应课程###
def SF_access():

    time.sleep(0.5)
    #搜索书法课程位置
    xy = pyautogui.locateOnScreen('.\\img\\SF\\SF.png')
    #获取中心坐标
    center = pyautogui.center(xy)
    #单击进入课程
    pyautogui.click(center)
    print('已进入书法课程')
###1.2搜索未完成课程并观看###
def SF_search():
    count = 1
    #XY宽高点位
    x = 1652
    y = 423
    w = 1907
    h = 465
    scope = (x,y,w,h)
    #X、h临时存放变量
    y2 = 0 
    h2 = 0
    #寻找未观看课程
    while count:
        time.sleep(0.01)
        try:
            xy2 = pyautogui.locateOnScreen('.\\img\\SF\\SF2.png', region=scope)
            y2 = y
            h2 = h
            print(scope)
            y += 50
            h += 50
            print(scope)
            if 966 < h < 1017:
                pyautogui.scroll(-745)
                x = 1652
                y = 423
                w = 1907
                h = 465
        except:
            try:
                xy1 = pyautogui.locateOnScreen('.\\img\\SF\\SF1.png', region=scope)
                center = pyautogui.center(xy1)
                pyautogui.click(center)
                time.sleep(1)
                pyautogui.moveTo(27,964)
                pyautogui.click()
                while True:
                    time.sleep(0.01)
                    try:
                        xy2 = pyautogui.locateOnScreen('.\\img\\SF\\SF2.png', region=scope)
                        print(scope)
                        y += 50
                        h += 50
                        print(scope)
                        print(xy2)
                        return
                    except:
                        time.sleep(0.01)
            except:
                y2 = y
                h2 = h
                y += 50
                h += 50


def text():
    pyautogui.moveTo(1788,570)
    pyautogui.scroll(-745)

SF_search()
#CJ()
#text()

