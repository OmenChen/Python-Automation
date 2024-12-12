import win32api
import win32con
import win32gui
import win32com.client
import time   #时间
import pyautogui as py   #键鼠控制
import pydirectinput #键盘控制

import keyboard   #键盘监测
import threading    #线程
import tkinter.messagebox

'''
界面大小1600*900
无边窗口
'''

runing = True
mouseColor = 255255255
count = 0   # 计数

class game:
    #滑步左键蓄力接破罡
    def left_Z():
        pydirectinput.keyDown('shift')
        if py.pixelMatchesColor(1027,484,(255,255,255)) != True:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,1020,0,0,0)
        win32api.Sleep(500)
        pydirectinput.press('`')
        # if py.pixelMatchesColor(664,356,(255,253,233)) == True or py.pixelMatchesColor(637,358,(243,241,222)) == True or py.pixelMatchesColor(635,359,(253,249,231)) == True or py.pixelMatchesColor(638,354,(255,251,233)) == True:
        # pydirectinput.keyUp('shift')
        # else:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        pydirectinput.keyUp('shift')
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        time.sleep(0.5)

    #四项
    def sx():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.2)

    def money():
        win32api.SetCursorPos((1623,467))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        time.sleep(0.2)


#鼠标操作
class mouse:
    def mouse_LEFTDOWN():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.2)

    def mouse_LEFTUP():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.2)

    def mouse_RIGHTDOWN():
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(0.2)

    def mouse_RIGHTUP():
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        time.sleep(0.2)

    def mouse_LEFT():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.2)

    def mouse_RIGHT():
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0 )
        time.sleep(0.2)



# win32api.Sleep(3000)
# win32api.SetCursorPos((1623,467))
# pydirectinput.middleClick(1623,467)
# while True:
#     win32api.Sleep(60000)
#     pydirectinput.press('w')
#     mouse.mouse_LEFT()
#     mouse.mouse_RIGHT()
#     mouse.mouse_LEFT()
#     mouse.mouse_RIGHT()
#     mouse.mouse_LEFT()
#     mouse.mouse_RIGHT()
    # if py.pixelMatchesColor(1027,484,(255,255,255)) != True:
    #     print('锁定')
    #     pydirectinput.press('`')
    # pydirectinput.press('`')
    # win32api.Sleep(60000)
    # pydirectinput.press('w')
    # if py.pixelMatchesColor(227,786,(231,231,231)) == True and py.pixelMatchesColor(227,859,(234,233,233)) == True:
    #     pydirectinput.press('esc')
    #     win32api.Sleep(200)
    #     win32api.SetCursorPos((959,721))
    #     mouse.mouse_LEFT()
    #     win32api.Sleep(200)
    #     pydirectinput.press('space')
    # if py.pixelMatchesColor(227,786,(233,231,231)) == True and py.pixelMatchesColor(227,859,(234,233,233)) == True:
    #     pydirectinput.press('esc')
    #     win32api.Sleep(200)
    #     win32api.SetCursorPos((959,721))
    #     mouse.mouse_LEFT()
    #     win32api.Sleep(200)
    #     pydirectinput.press('space')
    # pydirectinput.keyUp('`')
    # game.left_Z()
    # game.left_Z()
    # count += 1
    # print(count)
    # if count == 6:
    #     break

while runing:
    win32api.Sleep(10)
    #开始游戏
    while True:
        # if py.pixelMatchesColor(951,863,(255,255,255)) == True and py.pixelMatchesColor(910,878,(255,255,255)) == True:
        #     win32api.SetCursorPos((951,863))
        #     mouse.mouse_LEFT()
        if py.pixelMatchesColor(1661,926,(255,255,255)) == True and py.pixelMatchesColor(1509,935,(255,255,255)) == True:
            win32api.SetCursorPos((1590,923))
            mouse.mouse_LEFT()
            if py.pixelMatchesColor(917,607,(158,38,36)) == True:
                exit(0)
            break
    #角色选择
    while True:
        if py.pixelMatchesColor(1569,870,(160,39,38)) == True:
            win32api.SetCursorPos((257,375))
            mouse.mouse_LEFT()
            win32api.SetCursorPos((1569,870))
            mouse.mouse_LEFT()
            count = 0
            break
    #游戏界面1
    while True:
        try:
            if py.pixelMatchesColor(664,356,(255,253,233)) == True or py.pixelMatchesColor(637,358,(243,241,222)) == True or py.pixelMatchesColor(635,359,(253,249,231)) == True or py.pixelMatchesColor(638,354,(255,251,233)) == True:
                win32api.SetCursorPos((664,468))
                win32api.Sleep(1000)
                mouse.mouse_LEFT()
                count += 1
                # print('count='+str(count))
            if py.pixelMatchesColor(1698,382,(245,245,245)) == True or py.pixelMatchesColor(1698,386,(241,241,241)) == True:
                win32api.Sleep(3000)
                # pydirectinput.keyDown('w')
                # win32api.Sleep(2500)
                # pydirectinput.keyUp('w')
                pydirectinput.press('tab')
                # count += 1
                # print('count='+str(count))
                # win32api.Sleep(200)
                # pydirectinput.keyUp('tab')
                while True:
                    if py.pixelMatchesColor(1622,453,(229,229,229)) == True:
                        game.money()
                    else:
                        break 
            if count != 0:
            #     if count != 7:
            #         if count !=14:
            #             if count != 21:
                if py.pixelMatchesColor(253,950,(229,246,255)) == True and py.pixelMatchesColor(1021,577,(0,0,0)) != True and py.pixelMatchesColor(1698,382,(245,245,245)) != True and py.pixelMatchesColor(1698,386,(241,241,241)) != True:
                    if py.pixelMatchesColor(402,951,(229,246,255)) != True and py.pixelMatchesColor(965,974,(222,222,222)) == True:
                        pydirectinput.press('v')
                        # win32api.Sleep(200)
                        # pydirectinput.keyUp('v')
                    if py.pixelMatchesColor(1027,484,(255,255,255)) != True:
                        pydirectinput.press('`')
                    # win32api.Sleep(200)
                    # pydirectinput.keyUp('`')
                    game.left_Z()
                                # win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,1420,0,0,0)
            if py.pixelMatchesColor(227,786,(231,231,231)) == True and py.pixelMatchesColor(227,859,(234,233,233)) == True:
                pydirectinput.press('esc')
                win32api.Sleep(200)
                win32api.SetCursorPos((959,721))
                mouse.mouse_LEFT()
                win32api.Sleep(200)
                pydirectinput.press('space')
            if py.pixelMatchesColor(227,786,(233,231,231)) == True and py.pixelMatchesColor(227,859,(234,233,233)) == True:
                pydirectinput.press('esc')
                win32api.Sleep(200)
                win32api.SetCursorPos((959,721))
                mouse.mouse_LEFT()
                win32api.Sleep(200)
                pydirectinput.press('space')
            if py.pixelMatchesColor(948,316,(255,255,255)) == True and py.pixelMatchesColor(948,330,(255,255,255)) == True and py.pixelMatchesColor(253,949,(229,246,255)) == True:  #979,305
                pydirectinput.press('esc')
                win32api.Sleep(200)
                win32api.SetCursorPos((959,721))
                mouse.mouse_LEFT()
                win32api.Sleep(200)
                pydirectinput.press('space')
            if py.pixelMatchesColor(911,931,(164,52,45)) == True or py.pixelMatchesColor(1167,927,(130,98,78)) == True or py.pixelMatchesColor(1138,926,(128,97,81)) == True:
                while True:
                    if py.pixelMatchesColor(1661,926,(255,255,255)) == True and py.pixelMatchesColor(1509,935,(255,255,255)) == True:
                        break
                    else:
                        pydirectinput.press('space')
                        # win32api.Sleep(200)
                        # pydirectinput.keyUp('space')
                    if py.pixelMatchesColor(915,409,(235,194,117)) == True:
                        win32api.SetCursorPos((913,845))
                        mouse.mouse_LEFT()
                    win32api.Sleep(2000)
                    
            if py.pixelMatchesColor(1661,926,(255,255,255)) == True and py.pixelMatchesColor(1509,935,(255,255,255)) == True:
                win32api.Sleep(1000)
                if py.pixelMatchesColor(1661,926,(255,255,255)) == True and py.pixelMatchesColor(1509,935,(255,255,255)) == True:
                    # exit(0)
                    break

                # win32api.SetCursorPos((943,956))
                # mouse.mouse_LEFT()
            # if py.pixelMatchesColor(911,931,(164,50,44)) == True or py.pixelMatchesColor(911,931,(163,49,52)) == True:
            #     print('结束场景2')
            #     win32api.SetCursorPos((842,931))
            #     mouse.mouse_LEFT()

            # if py.pixelMatchesColor(917,931,(165,53,45)) == True:
            #     win32api.SetCursorPos((842,931))
            #     mouse.mouse_LEFT()

            # if py.pixelMatchesColor(951,863,(255,255,255)) == True and py.pixelMatchesColor(910,878,(255,255,255)) == True:
            #     win32api.SetCursorPos((951,863))
            #     mouse.mouse_LEFT()
            #     print('游戏结束')
            #     break

            # win32api.Sleep(1000)    # 1000 = 1s
            # 按下并释放F
            # pydirectinput.keyDown('f')
            # time.sleep(0.2)
            # pydirectinput.keyUp('f')
        except Exception as e:
            print(e)
    # mouse.click(Button.left,2)
    # py.doubleClick(x=798,y=203)
    # print('点击一次')
    # time.sleep(2)
    # if py.pixelMatchesColor(1540,878,(255,255,255)) == True:
    #         print('点击成功')
    #         mouse.position = (1540,878)
    #         mouse.click(Button.left,1)
    #         print('返回')
    # else:
    #      print('点击失败')
    # event = keyboard.read_event()
    # if event.event_type == keyboard.KEY_DOWN and event.name == 'p':
    #     runing = False

#1.进入角色选择界面
# py.pixelMatchesColor(1557,868,(158,38,37)) == True:  
# mouse.mouse_LEFTUP()   
#2.天赋选择
# py.pixelMatchesColor(644,334,(255,255,255)) == True:

