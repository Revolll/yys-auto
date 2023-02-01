from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from duixiang import Ui_MainWindow
from multctrl import MulCtrl
import ini
import compare
import win32gui
import win32api
import win32con
import sys
import time
import random
from PIL import Image, ImageGrab, ImageQt
import io
import threading


def get_handle():
    all_handle = []
    win32gui.EnumChildWindows(None, lambda handle, param: param.append(hex(handle)), all_handle)
    handle = [i for i in all_handle if win32gui.GetWindowText(eval(i)) == '阴阳师 - MuMu模拟器']
    for j in handle:
        x, y, w, h = win32gui.GetWindowRect(eval(j))
        # win32gui.MoveWindow(eval(j), x, y, 800, 480, True)
    return handle


def prtsc():
    pwnd = get_handle()
    print(pwnd)
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(eval(pwnd[0])).toImage()
    t = time.strftime('%Y%m%d%H%M%S', time.localtime())
    img.save(f'./image/screenshots/截图_{t}.jpg')
    print("截图已保存")


# prtsc()