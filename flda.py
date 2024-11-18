import pyautogui as py   #键鼠控制
import time   #时间
import keyboard   #键盘监测
from pynput import mouse   #鼠标监测
import threading    #线程
'''

采用多线程技术解决键鼠在监听时导致游戏卡顿的问题

'''



#游戏脚本
class Game:
    def __init__(self):
        self.runing = True

    def lz(self):   #连招轻刀起手接重刀
        py.press('r')
        py.click()
        time.sleep(0.2)
        py.press('r')
        time.sleep(0.6)

        py.press('r')
        py.click(button='right')
        time.sleep(0.6)
        py.press('r')
        time.sleep(0.2)

        py.press('r')
        py.click(button='right')
        time.sleep(0.6)
        py.press('r')
        time.sleep(0.2)

        py.press('r')
        py.click(button='right')
        time.sleep(0.6)
        py.press('r')
        time.sleep(0.2)

        py.press('r')
        py.click(button='right')
        time.sleep(0.6)
        py.press('r')
        time.sleep(0.2)

        py.press('r')
        py.click(button='right')
        time.sleep(0.6)
        py.press('r')
        time.sleep(0.2)

        py.press('r')
        py.click(button='right')
        time.sleep(0.6)
        py.press('r')
        time.sleep(0.2)

        py.press('r')
        py.click(button='right')
        time.sleep(0.6)
        py.press('r')
        time.sleep(0.2)

        py.press('r')
        py.click(button='right')
        time.sleep(0.6)
        py.press('r')
        time.sleep(0.2)

    def qj(self):  #轻刀
        py.press('r')
        py.click()
        time.sleep(0.2)
        py.press('r')
        time.sleep(0.6)

    def zj(self):   #重刀
        py.press('r')
        py.click(button='right')
        time.sleep(0.6)
        py.press('r')
        time.sleep(0.2)
        


g = Game()
#鼠标监听
def mouse_lesit():
    with mouse.Events() as events:
        for event in events:
            if hasattr(event, 'button'):
                if event.button == mouse.Button.x1:
                    if event.pressed:
                        g.qj()
                        
                if event.button == mouse.Button.x2:
                    if event.pressed:
                        g.zj()

#键盘监听
def key_lesit():
    while True:
        event = keyboard.read_event()  #创建监听
        if event.event_type == keyboard.KEY_DOWN and event.name == 'f':
            g.lz()

#创建多线程
thread = threading.Thread(target=mouse_lesit)  #鼠标监听加入线程1
thread.daemon = True
thtead2 = threading.Thread(target=key_lesit)   #键盘监听加入线程2
thtead2.daemon = True
thread.start()  #启动线程1
thtead2.start()  #启动线程2

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