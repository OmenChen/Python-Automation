'''
###使用到的库:pyautogui、pillow、opencv-python

##异常处理
##python异常##
#1.异常报警:raise ImageNotFoundException  # Raise PyAutoGUI's ImageNotFoundException.
#  原因:调用pyautogui.locateOnScreen()函数时未找到匹配图片,引发PyautoGUI程序BUG;
#  解决:将Pyscreeze包更新成0.1.29版本(pip install Pyscreeze==0.1.29)

##git异常##
#1.异常报警:fatal: unable to access 'https://github.com/XXX/XXX.git/': SSL certificateproblem: unable to get local issuer certificate
#  原因:git拉取或提交时HTTPS验证报错,默认CURL被设为不信任CAS
#  解决:修改git配置文件(it config --global http.sslVerify false)
#2.异常报警：拉取代码时出现“在签出前，请先清理仓库工作树”的弹窗
#  原因:本地代码和git远程库代码存在冲突
#  解决:先对修改的文件进行储存(git stash),再拉取(git pull),最后弹出储存(git stash pop)
'''

import pyautogui
import time
from PIL import Image

# ##############1.采集实例样本#########################
def CJ():
    #截图整个屏幕
    x=691
    y=515
    w=710
    h=557
    scope = (x,y,w,h)
    #pyautogui.moveTo(802,576)
    im = pyautogui.screenshot()
    #扣取实例图像，可用pyautogui.moseInfo()获取坐标点位
    #pyautogui.mouseInfo()
    om = im.crop(scope)      #pyautogui.mouseInfo()
    #保存实列图像
    om.save(".\\img\\tigan.png")



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

###全局变量


###########################################################################################
###图片位置搜索定位###
def search_img(img_src, fc=1, rg=None):  #img_src:图片地址;fc图片搜索匹配系数默认1，越小越模糊;rg:搜索范围xywh;
    #打开样本图像
    img = Image.open(img_src) #'.\\img\\PT\\1.png'
    #获取图像宽高
    width = img.size[0]
    height = img.size[1]
    fw=1
    fh=1
    while True:
        n_img = img.resize((int(width*fw),int(height*fh)), Image.Resampling.LANCZOS)
        if pyautogui.locateOnScreen(n_img, confidence=fc,region=rg) == None:
            fw -= 0.01
            fh -= 0.01
            fw = round(fw,2)
            fh = round(fh,2)
            if fw == 0 or int(width*fw) < 10 or int(height*fh) < 10 :
                return False
        else:
            xy = pyautogui.locateCenterOnScreen(n_img, confidence=fc,region=rg)
            return xy


###########################
###1.1开始钓鱼###
def DY_access():
    tmp = search_img(".\\img\\start.png",0.7)
    if tmp == False:
        print("未找到")
    else:
        print("已找到开始钓鱼按钮，并点击")
        #pyautogui.moveTo(tmp)
        pyautogui.click(tmp)

###1.2抛竿###
def DY_start():
    # tmp = search_img(".\\img\\paogan.png",0.7)
    # if tmp == False:
    #     print("未找到")
    # else:
    #     print("已找到抛竿按钮，并点击")
    while True:
        if pyautogui.pixelMatchesColor(1218,299,(255,203,90)) == True:
            pyautogui.click(1218,299)
        if pyautogui.pixelMatchesColor(998,817,(173,170,165)) == True:
            pyautogui.moveTo(1562,823)
            pyautogui.dragRel(0,-300,duration=0.5)
            break


###2.1钓鱼提干###
def DY_diao(x,y):
    while True:
        pyautogui.click(x,y)
        if pyautogui.pixelMatchesColor(1239,138,(99,77,66)) == True:
            break
        # if pyautogui.pixelMatchesColor(658,541,(222,97,74)) == True:
        #     if pyautogui.pixelMatchesColor(658,541,(222,97,74)) == False:
        #         pyautogui.click(x,y)
        #         break
        # if pyautogui.pixelMatchesColor(658,521,(222,97,74)) == True:
        #     if pyautogui.pixelMatchesColor(658,531,(222,97,74)) == False:
        #         pyautogui.click(x,y)
        #         break
        # if pyautogui.pixelMatchesColor(658,501,(222,97,74)) == True:
        #     if pyautogui.pixelMatchesColor(658,521,(222,97,74)) == False:
        #         pyautogui.click(x,y)
        #         break
        # if pyautogui.pixelMatchesColor(658,481,(222,97,74)) == True:
        #     if pyautogui.pixelMatchesColor(658,511,(222,97,74)) == False:
        #         pyautogui.click(x,y)
        #         break
        # if pyautogui.pixelMatchesColor(658,461,(222,97,74)) == True:
        #     if pyautogui.pixelMatchesColor(658,501,(222,97,74)) == False:
        #         pyautogui.click(x,y)
        #         break
        
        # if pyautogui.pixelMatchesColor(658,561,(222,97,74)) == True:
        #     if pyautogui.pixelMatchesColor(658,541,(222,97,74)) == False:
        #         pyautogui.click(x,y)
        #         break
        # if pyautogui.pixelMatchesColor(658,581,(222,97,74)) == True:
        #     if pyautogui.pixelMatchesColor(658,531,(222,97,74)) == False:
        #         pyautogui.click(x,y)
        #         break
        # if pyautogui.pixelMatchesColor(658,601,(222,97,74)) == True:
        #     if pyautogui.pixelMatchesColor(658,521,(222,97,74)) == False:
        #         pyautogui.click(x,y)
        #         break
        # if pyautogui.pixelMatchesColor(658,621,(222,97,74)) == True:
        #     if pyautogui.pixelMatchesColor(658,511,(222,97,74)) == False:
        #         pyautogui.click(x,y)
        #         break
        # if pyautogui.pixelMatchesColor(658,641,(222,97,74)) == True:
        #     if pyautogui.pixelMatchesColor(658,501,(222,97,74)) == False:
        #         pyautogui.click(x,y)
        #         break
        
    while True:
        if pyautogui.pixelMatchesColor(1239,138,(99,77,66)) == True:
            pyautogui.click(x,y)
        if pyautogui.pixelMatchesColor(1379,905,(255,195,90)) == True:
            #print("捕鱼完成")
            pyautogui.click(1379,905)
            return
        # xy = pyautogui.locateOnScreen(".\\img\\tigan.png",confidence=0.7)
        # #pyautogui.locateOnScreen(n_img, confidence=fc,region=rg)
        # if xy == None:
        #     a -= 1
        #     if a == 0:
        #         print("未找到")
        #         return False
        # else:
        #     pyautogui.moveTo(xy)
        #     print(xy[0])
        #     print(xy[1])
            
        #     while True:
        #         if pyautogui.pixelMatchesColor(int(xy[0]),int(xy[1]),(222,98,73), tolerance=50) == False:    #xy点位RGB颜色比较，tolerance误差范围，一样返回True,否则False
        #             pyautogui.click(tmp)
        #             return



###1.2搜索未完成课程并观看###sf1 .95  sf2 .98
def SF_search():
    xy = None
    a = 1
    while True:
        tmp = search_img(".\\img\\SF\\SF2.png",0.98,xy)
        if tmp == False:
            print("未找到")
            return
        else:
            if a == 1:
                tmp2= search_img(".\\img\\SF\\SF1.png",0.95,xy)
                x2 = tmp2[0]
                y2 = tmp2[1]
                x1 = tmp[0]
                y1 = tmp[1]
                h = x1 - x2 + 50
                w = y2 - y1 + 30
                xy = (tmp2[0]-50,tmp2[1]-50,tmp[0]+20,tmp[1]+40)
                print(xy)
                x,y=tmp
                pyautogui.moveTo(x-50    ,y)
                a -= 1
            
            pyautogui.scroll(-50)


def text():
    tmp = search_img(".\\img\\SF\\SF2.png",0.98)
    # pyautogui.moveTo(1788,570)
    # pyautogui.scroll(-745)


#开始钓鱼
#DY_access()
#time.sleep(1)
while True:
    time.sleep(5)
    if pyautogui.pixelMatchesColor(1277,884,(140,138,140),tolerance=10) == True :
        print("捕鱼完成")
        break
    #抛竿
    DY_start()
    #钓鱼
    DY_diao(1562,823)

#SF_search()
#CJ()
# text()

