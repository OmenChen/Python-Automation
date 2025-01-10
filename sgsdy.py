###三国杀自动钓鱼###

import pyautogui as py   #键鼠控制
import win32api
import pydirectinput #键盘控制
import keyboard   #键盘监测
from pynput import mouse   #鼠标监测
import threading    #线程
import tkinter.messagebox     #弹窗
import wxauto     #微信自动化
import time   #时间

py.FAILSAFE=False  #禁用鼠标移动到屏幕角落保护
runing = True
# runing_game = False
count = 1

#自动点击
def mouse_click():
    global runing
    while True:
        while count & 1 == 0:  #判断是否为奇数
            # while py.pixelMatchesColor(313,47,(59,67,84)) and py.pixelMatchesColor(326,61,(236,229,216)):
                # print('点击开始')
                # py.moveTo(1418,806)
                # py.click()
                # win32api.Sleep(5)
            if py.pixelMatchesColor(1361,886,(99,78,59)):
                py.moveTo(1562,823)
                py.dragRel(0,-300,duration=0.5)
            if py.pixelMatchesColor(629,188,(107,77,66)):
                py.moveTo(1562,823)
                win32api.Sleep(760)
                py.click()
                while True:
                    if py.pixelMatchesColor(1229,138,(99,77,66)) != True:
                        win32api.Sleep(200)
                    else:
                        # py.moveTo(1562,823)
                        py.click(1562,823)
                    if py.pixelMatchesColor(1374,848,(255,203,90)):
                        py.moveTo(1386,874)
                        win32api.Sleep(500)
                        py.click()
                        break
            #补充饵料
            if py.pixelMatchesColor(1214,300,(255,203,90)):
                win32api.Sleep(500)
                py.moveTo(1159,302)
                py.click()
            if py.pixelMatchesColor(953,740,(140,190,132)):
                print('捕鱼完成')
                pydirectinput.press('p')
        win32api.Sleep(200)

#鼠标监听
def mouse_lesit():
    try:
        # global runing_game
        global count
        with mouse.Events() as events:
            for event in events:
                if hasattr(event, 'button'):
                    if event.button == mouse.Button.x1:   #鼠标下侧键控制龙王旋转
                        if event.pressed:
                            for i in range(1):
                                count += 1
                                # print('点击'+str(runing_click))
                            
                    # if event.button == mouse.Button.x2:    #鼠标上侧键控制自动剧情点击
                    #     if event.pressed:
                    #         for l in range(1):
                    #             count2 += 1
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

#min
while runing:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'p':
        runing = False
