#永杰四项自动挂机

import win32api
import win32con
import time   #时间
import keyboard   #键盘监测
import threading    #线程

runing = True
mouseColor = 255255255
count = 1   # 计数
content = 0

#游戏操作
class game:
    #四项
    def sx():
        mouse.mouse_RIGHTDOWN(0.2)
        mouse.mouse_LEFTDOWN(0.1)
        mouse.mouse_RIGHTUP(0.1)
        mouse.mouse_LEFTUP(0.55)


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



def gj():
    while True:
        win32api.Sleep(200)
        # if content == 1 : 
            # win32api.Sleep(50)
        game.sx()
        # while content==1:
        #     game.sx()



#创建多线程
thread_game = threading.Thread(target=gj)  #鼠标监听加入线程
thread_game.daemon = True
thread_game.start()  #启动线程

#主线程
while runing:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == '=':
        runing = False
    # if event.event_type == keyboard.KEY_DOWN and event.name == '-':
    #     content = 1
    # if event.event_type == keyboard.KEY_DOWN and event.name == ']':
    #     content = 0
