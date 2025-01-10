#原神游戏

import pyautogui as py   #键鼠控制
import win32api
import win32con
import keyboard   #键盘监测
from pynput import mouse   #鼠标监测
import threading    #线程
import tkinter.messagebox     #弹窗


py.FAILSAFE=False  #禁用鼠标移动到屏幕角落保护
runing = True
runing_game = False
count = 1
count2 = 2



class game():
    #龙王旋转
    def xz():
        while True:
            while count & 1 == 0:   #判断是否为偶数
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,100,0,0,0)
            win32api.Sleep(200)

#剧情自动点击
def mouse_click():
    while True:
        while count2 & 1 != 0:  #判断是否为奇数
            while py.pixelMatchesColor(313,47,(59,67,84)) and py.pixelMatchesColor(326,61,(236,229,216)):
                # print('点击开始')
                py.moveTo(1418,806)
                py.click()
                win32api.Sleep(5)
        win32api.Sleep(200)

#鼠标监听
def mouse_lesit():
    try:
        global runing_game
        global count
        global count2
        with mouse.Events() as events:
            for event in events:
                if hasattr(event, 'button'):
                    if event.button == mouse.Button.x1:   #鼠标下侧键控制龙王旋转
                        if event.pressed:
                            for i in range(1):
                                count += 1
                                # print('点击'+str(runing_click))
                            
                    if event.button == mouse.Button.x2:    #鼠标上侧键控制自动剧情点击
                        if event.pressed:
                            for l in range(1):
                                count2 += 1
                                # print('关闭'+str(runing_click))
    except Exception as e:
        tkinter.messagebox.showinfo('鼠标',e)  #弹窗提示


#创建多线程
thread_mouse = threading.Thread(target=mouse_lesit)  #鼠标监听加入线程
thread_mouse.daemon = True
thread_mouse.start()
thread_mouse2 = threading.Thread(target=mouse_click)  #鼠标监听加入线程
thread_mouse2.daemon = True
thread_mouse2.start()
thread_mouse3 = threading.Thread(target=game.xz)  #游戏加入线程
thread_mouse3.daemon = True
thread_mouse3.start()

#min
while runing:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'p':
        runing = False
    # event = keyboard.read_event()
    # if event.event_type == keyboard.KEY_DOWN and event.name == 'p':
    #     runing = False
