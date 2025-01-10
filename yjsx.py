#永杰四项辅助

import win32api
import win32con
import time   #时间
import keyboard   #键盘监测
from pynput import mouse as ms  #鼠标监测
import threading    #线程
import tkinter.messagebox

runing = True
mouseColor = 255255255
count = 0   # 计数
content = 0
control_mouse = ms.Controller()

#游戏操作
class game:
    #四项
    def sx():
        if content & 1 != 0:  #判断是否为奇数
            mouse.mouse_LEFT(0.8)
        elif count & 1 != 0:  #判断是否为奇数
            mouse.mouse_RIGHT(0.8)
        # elif count == 0 and content == 0:
        else:
            mouse.mouse_RIGHTDOWN(0.2)
            mouse.mouse_LEFTDOWN(0.1)
            mouse.mouse_RIGHTUP(0.1)
            mouse.mouse_LEFTUP(0.8)
        # else:
        #     # pydirectinput.press('space')
        #     control_mouse.press(ms.Button.x1)        # 按下鼠标侧键
        #     # win32api.Sleep(60)
        #     win32api.Sleep(140)
        #     mouse.mouse_RIGHTDOWN(0.2)
        #     control_mouse.release(ms.Button.x1)     # 释放鼠标侧键
        #     # win32api.Sleep(500)
        #     mouse.mouse_LEFTDOWN(0.1)
        #     mouse.mouse_RIGHTUP(0.1)
        #     mouse.mouse_LEFTUP(0.55)


#鼠标操作
class mouse:
    def mouse_LEFTDOWN(t=0.2):
        global content
        global count
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(t)
        count = 0   # 计数
        content = 0

    def mouse_LEFTUP(t=0.2):
        global content
        global count
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(t)
        count = 0   # 计数
        content = 0

    def mouse_RIGHTDOWN(t=0.2):
        global content
        global count
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(t)
        count = 0   # 计数
        content = 0

    def mouse_RIGHTUP(t=0.2):
        global content
        global count
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        time.sleep(t)
        count = 0   # 计数
        content = 0

    def mouse_LEFT(t1=0.2,t2=0.2):
        global content
        global count
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(t1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(t2)
        count = 0   # 计数
        content = 0

    def mouse_RIGHT(t1=0.2,t2=0.2):
        global content
        global count
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(t1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0 )
        time.sleep(t2)
        count = 0   # 计数
        content = 0

#鼠标监听
def mouse_lesit():
    try:
        global content
        global count
        with ms.Events() as events:
            for event in events:
                if hasattr(event, 'button'):
                    # if event.button == ms.Button.x1:
                    #     if event.pressed:
                    #         for i in range(1):
                    #             print()
                    if event.button == ms.Button.right:
                        content += 1
                    if event.button == ms.Button.left:
                        count += 1
                    # if event.button == ms.Button.x2:
                    #     if event.pressed:
                    #         for l in range(1):
                    #             game.sx()
    except Exception as e:
        tkinter.messagebox.showinfo('鼠标',e)  #弹窗提示

#创建多线程
thread_game = threading.Thread(target=mouse_lesit)  #鼠标监听加入线程
thread_game.daemon = True
thread_game.start()  #启动线程

#主线程

while runing:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == '=':
        runing = False
    if event.event_type == keyboard.KEY_DOWN and event.name == 'c':
        game.sx()
