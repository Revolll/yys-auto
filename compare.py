import random
import cv2
import numpy as np
import time
from PySide2.QtWidgets import *
import win32gui
import win32api
import win32con
import threading
from PIL import Image, ImageGrab, ImageQt


def get_handle():
    all_handle = []
    win32gui.EnumChildWindows(None, lambda handle, param: param.append(hex(handle)), all_handle)
    handle = [i for i in all_handle if win32gui.GetWindowText(eval(i)) == '阴阳师-网易游戏']
    for j in handle:
        x, y, w, h = win32gui.GetWindowRect(eval(j))
        win32gui.MoveWindow(eval(j), x, y, 800, 480, True)
    return handle


def prtsc():
    pwnd = get_handle()
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(eval(pwnd[0])).toImage()
    img.save(f'./image/screenshots/2.jpg')
    # return img


def print_img(pwnd):
    sreen = QApplication.primaryScreen()
    img = sreen.grabWindow(pwnd).toImage()
    return img


def qimg2cv(img):
    img1 = ImageQt.fromqimage(img)
    img2 = cv2.cvtColor(np.asarray(img1), cv2.COLOR_RGB2BGR)
    return img2


def pil2cv(img):
    img1 = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    return img1


def cv_r_img(img):
    arr = cv2.imread(img)
    return arr


def pil_r_img():
    tz1 = './image/screenshots/1.jpg'
    img = Image.open(tz1)
    return img


def cv_resize():
    tz1 = './image/phone.jpg'
    img = cv2.imread(tz1)
    # print(img.shape)
    img2 = cv2.resize(img, (784, 442))
    cv2.imwrite('./image/phone1.jpg', img2)
    # img2.imshow(img)
    # return img2


def pil_resize():
    tz1 = './image/phone.jpg'
    img = Image.open(tz1)
    img2 = img.resize((16, 16), Image.ANTIALIAS).convert('L')  # 抗锯齿 灰度
    return img2


def image_recognition(img, template):
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.85  # 匹配度
    gps = []

    loc = np.where(res >= threshold)  # 匹配程度大于threshold的坐标y,x
    for pt in zip(*loc[::-1]):  # *号表示可选参数
        gps.append(pt)
    for i in gps:
        for j in gps:
            if abs(i[0] - j[0]) < 10 and abs(i[1] - j[1]) < 10:
                gps[gps.index(j)] = i
    gps2 = list(set(gps))
    return gps2


def run_ts(self, obj):
    t1 = threading.Thread(target=run,
                          args=(self, obj))
    t2 = threading.Thread(target=self.victory,
                          args=(obj, 265, 95, 65, 45, 630, 780, 320, 390, self.yyh_v))  # 胜利 260, 60, 70, 45
    t3 = threading.Thread(target=self.account,
                          args=(obj, 350, 310, 80, 55, 630, 780, 320, 390, self.yyh_a))  # 结算 350, 310, 80, 55

    t1.setDaemon(True)
    t1.start()
    t2.setDaemon(True)
    t2.start()
    t3.setDaemon(True)
    t3.start()


def run(self, obj):
    pwnd = eval(obj['handle'])
    while self.flag_run:
        time.sleep(random.randrange(150, 250)/100)
        sreen = qimg2cv(print_img(pwnd))
        if not click_enter(self, obj, sreen):
            if not click_boss(self, obj, sreen):
                if not click_monster(self, obj, sreen):
                    if not click_gift(self, obj, sreen):
                        click_move(self, obj, sreen)


def click_enter(self, obj, sreen):
    pwnd = eval(obj['handle'])
    enter = './image/tansuo/enter.jpg'
    pos_enter = image_recognition(cv_r_img(enter), sreen)
    if pos_enter:
        x, y = random.choice(pos_enter)
        obj['gbox'].sig.emit('点击探索！')
        # print(f'enter:{x}, {y}')
        self.click(pwnd, x + 5, x + 75, y + 5, y + 35)
        time.sleep(random.randrange(70, 180) / 100)
        return True
    else:
        return False


def click_boss(self, obj, sreen):
    pwnd = eval(obj['handle'])
    boss = './image/tansuo/boss.jpg'
    pos_boss = image_recognition(cv_r_img(boss), sreen)
    if pos_boss:
        x, y = random.choice(pos_boss)
        obj['gbox'].sig.emit('点击领主！')
        # print(f'boss:{x}, {y}')
        self.click(pwnd, x - 5, x + 27, y - 5, y + 27)
        time.sleep(random.randrange(70, 180)/100)
        return True
    else:
        return False


def click_monster(self, obj, sreen):
    pwnd = eval(obj['handle'])
    monster = './image/tansuo/monster.jpg'
    pos_monster = image_recognition(cv_r_img(monster), sreen)
    if pos_monster:
        x, y = random.choice(pos_monster)
        obj['gbox'].sig.emit('点击怪物！')
        # print(f'monster:{x}, {y}')
        self.click(pwnd, x - 5, x + 27, y - 5, y + 27)
        time.sleep(random.randrange(70, 180)/100)
        return True
    else:
        return False


def click_gift(self, obj, sreen):
    pwnd = eval(obj['handle'])
    house = './image/tansuo/gift.jpg'
    pos_move = image_recognition(cv_r_img(house), sreen)
    if pos_move:
        for i in pos_move:
            x, y = i
            obj['gbox'].sig.emit('点击扫地工！')
            # print(f'gift:{x}, {y}')
            self.click(pwnd, x - 5, x + 35, y - 5, y + 30)
            time.sleep(random.randrange(70, 180) / 100)
            self.click(pwnd, 750, 800, 200, 350)
            time.sleep(random.randrange(70, 180) / 100)
        return True
    else:
        return False


def click_move(self, obj, sreen):
    pwnd = eval(obj['handle'])
    house = './image/tansuo/move.jpg'
    pos_move = image_recognition(cv_r_img(house), sreen)
    if pos_move:
        x = random.randrange(571, 762)
        y = random.randrange(262, 362)
        obj['gbox'].sig.emit('点击移动！')
        # print(f'move:{x}, {y}')
        self.click_pos(pwnd, x, y)
        time.sleep(random.randrange(400, 600)/100)
        return True
    else:
        return False


def click_pos():
    """鼠标单击坐标（pos_x, pos_y）"""
    pwnd = eval(get_handle()[0])
    win32api.SendMessage(pwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(750, 300))
    t = random.randrange(100, 250)/1000
    time.sleep(t)
    win32api.SendMessage(pwnd, win32con.WM_MOUSEMOVE,win32api.MAKELONG(750, 350))
    win32api.SendMessage(pwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, win32api.MAKELONG(750, 350))

# click_pos()
# pil2cv()

# def ppp():
#     img = Image.open('D:/JetBrains/Projects/面向对象/icon.ico')
#     img = img.resize((256, 256), Image.ANTIALIAS).convert('L')  # 抗锯齿 灰度
#     img.save('D:/JetBrains/Projects/面向对象/icon1.ico')
#     img.show()
#
# ppp()