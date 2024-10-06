###使用到的库：pyautogui、pillow、opencv-python
##异常处理
#1.异常报警：raise ImageNotFoundException  # Raise PyAutoGUI's ImageNotFoundException.
#  原因：调用pyautogui.locateOnScreen()函数时未找到匹配图片，引发PyautoGUI程序BUG；
#  解决：将Pyscreeze包更新成0.1.29版本（pip install Pyscreeze==0.1.29）
#


import pyautogui
import time

# ##############1.采集实例样本#########################
def CJ():
    #截图整个屏幕
    x=327
    y=728
    w=542
    h=858
    scope = (x,y,w,h)
    #pyautogui.moveTo(802,576)
    im = pyautogui.screenshot()
    #扣取实例图像，可用pyautogui.moseInfo()获取坐标点位
    #pyautogui.mouseInfo()
    om = im.crop(scope)      #pyautogui.mouseInfo()
    #保存实列图像
    om.save("SF.png")



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

#寻找样本图片
def SZ(img,tmp=1,*tmp1):  #img:图片地址；region:搜索范围；confidence:模糊搜索值
    try:
        xy = pyautogui.locateOnScreen(img,confidence=tmp,region=tmp1)
        print(1)
        return xy
    except Exception as e:
        print(2)
        return e

#############1.书法##################
###1.1进入对应课程###
def SF_access():
    time.sleep(0.5)
    #搜索书法课程位置
    xy = pyautogui.locateOnScreen('.\\img\\SF\\SF.png')
    if xy == None:
        print("未找到图片")
    else:
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
            xy2 = pyautogui.locateOnScreen('.\\img\\SF\\SF2.png')
            center = pyautogui.center(xy2)
            #xy2 = pyautogui.locateOnScreen('.\\img\\SF\\SF2.png', region=scope)
            print(center)
            count -= 1
        except:
            print("未找到目标")
            count -= 1


def text():
    pyautogui.moveTo(1788,570)
    pyautogui.scroll(-745)

SF_access()
#SF_search()
#CJ()
#text()

