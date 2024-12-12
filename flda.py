import pyautogui as py   #键鼠控制
import time   #时间
import keyboard   #键盘监测
from pynput import mouse   #鼠标监测
import threading    #线程
import tkinter.messagebox
'''

采用多线程技术解决键鼠在监听时导致游戏卡顿的问题

'''

py.FAILSAFE=False  #禁用鼠标移动到屏幕角落保护

#游戏脚本
class Game:
    def __init__(self):
        self.runing = True
        self.mouseColor = 255255255

    def lz(self):   #连招轻刀起手接重刀
        g.qj()
        for i in range(6):
            event = keyboard.read_event()  #创建监听
            if event.event_type == keyboard.KEY_DOWN and event.name == '`':
                return
            else:
                g.zj()

    def qj(self):  #轻刀
        mouse_color(x=107, y=920)
        if g.mouseColor == str(255255255):
            py.click()
            time.sleep(0.5)
            py.press('r')
            py.press('r')
            time.sleep(0.2)

        else:
            py.press('r')
            py.click()
            time.sleep(0.5)
            py.press('r')
            time.sleep(0.2)

    def zj(self):   #重刀
        mouse_color(x=107, y=920)
        if g.mouseColor == str(255255255):
            py.click(button='right')
            time.sleep(0.6)
            py.press('r')
            py.press('r')
            time.sleep(0.1)

        else:
            py.press('r')
            py.click(button='right')
            time.sleep(0.6)
            py.press('r')
            time.sleep(0.1)
        
g = Game()

#鼠标位置颜色识别
def mouse_color(x=0, y=0):
    try:
        pix = py.screenshot().getpixel((x, y))  # 获取鼠标所在屏幕点的RGB颜色
        positionStr = str(pix[0]).rjust(3) + str(pix[1]).rjust(3) + str(pix[2]).rjust(3)
        g.mouseColor = positionStr
    except Exception as e:
        tkinter.messagebox.showinfo('光标位置颜色',e)  #弹窗提示

#鼠标监听
def mouse_lesit():
    try:
        with mouse.Events() as events:
            for event in events:
                if hasattr(event, 'button'):
                    if event.button == mouse.Button.x1:
                        if event.pressed:
                            for i in range(1):
                                g.qj()
                            
                    if event.button == mouse.Button.x2:
                        if event.pressed:
                            for l in range(1):
                                g.zj()
    except Exception as e:
        tkinter.messagebox.showinfo('鼠标',e)  #弹窗提示

#键盘监听
def key_lesit():
    try:
        while True:
            event = keyboard.read_event()  #创建监听
            if event.event_type == keyboard.KEY_DOWN and event.name == 'f':
                g.lz()
    except Exception as e:
        tkinter.messagebox.showinfo('键盘',e)  #弹窗提示


tkinter.messagebox.showinfo('开始','鼠标上侧键重刀,下侧键轻刀,F连招,P关闭软件')  #弹窗提示

#创建多线程
thread_mouse = threading.Thread(target=mouse_lesit)  #鼠标监听加入线程
thread_mouse.daemon = True
thtead_key = threading.Thread(target=key_lesit)   #键盘监听加入线程
thtead_key.daemon = True
thread_mouse.start()  #启动线程
thtead_key.start()  #启动线程

#主线程

while g.runing:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'p':
        g.runing = False


#键盘监听
# while g.runing: 
#     event = keyboard.read_event()
    # if event.event_type == keyboard.KEY_DOWN and event.name == 'f':
    #     g.qj()
    # if event.event_type == keyboard.KEY_DOWN and event.name == 'p':
    #     g.runing = False