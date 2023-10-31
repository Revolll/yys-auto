#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time      :2023/10/30 17:31
# @Author    :Joy
# @FileName  :spy.py
import win32api
import win32con
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import win32gui


class SpyLabel(QLabel):
    sig_spy = Signal(object)

    def __init__(self, parent=None):
        super(SpyLabel, self).__init__(parent)
        self.parent = parent
        self.spying = False
        self.rectanglePen = win32gui.CreatePen(win32con.PS_SOLID, 3, win32api.RGB(255, 0, 0))
        self.prevWindow = None
        # self.setCursor(Qt.SizeAllCursor)

        self.sig_spy.connect(self.parent.out_put)
        self.pixmap = QPixmap('./image/finderf.bmp')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.spying = True
            self.pixmap = QPixmap('./image/findere.bmp')
            self.update()

            # 加载自定义鼠标图片
            cursor_image = QPixmap("./image/searchw.cur")

            # 调整鼠标图片大小
            cursor_image = cursor_image.scaledToWidth(32)

            # 创建自定义的 QCursor 对象
            custom_cursor = QCursor(cursor_image)

            # 设置窗口的鼠标样式为自定义样式
            self.setCursor(custom_cursor)

    def mouseReleaseEvent(self, event):
        if self.spying:
            if self.prevWindow:
                self.refreshWindow(self.prevWindow)

            win32gui.ReleaseCapture()
            self.spying = False

            self.pixmap = QPixmap('./image/finderf.bmp')
            self.setCursor(Qt.ArrowCursor)
            self.update()


    def mouseMoveEvent(self, event):
        if self.spying:
            curX, curY = win32gui.GetCursorPos()
            hwnd = win32gui.WindowFromPoint((curX, curY))

            if self.checkWindowValidity(hwnd):
                if self.prevWindow:
                    self.refreshWindow(self.prevWindow)

                self.prevWindow = hwnd
                self.highlightWindow(hwnd)
                self.displayWindowInformation(hwnd)

    def highlightWindow(self, hwnd):
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        windowDc = win32gui.GetWindowDC(hwnd)
        if windowDc:
            prevPen = win32gui.SelectObject(windowDc, self.rectanglePen)
            prevBrush = win32gui.SelectObject(windowDc, win32gui.GetStockObject(win32con.HOLLOW_BRUSH))

            win32gui.Rectangle(windowDc, 0, 0, right - left, bottom - top)

            win32gui.SelectObject(windowDc, prevPen)
            win32gui.SelectObject(windowDc, prevBrush)
            win32gui.ReleaseDC(hwnd, windowDc)

    def refreshWindow(self, hwnd):
        try:
            win32gui.InvalidateRect(hwnd, None, True)
        except:
            self.sig_spy.emit("访问被拒绝需管理员身份运行")
        win32gui.UpdateWindow(hwnd)
        win32gui.RedrawWindow(hwnd, None, None,
                              win32con.RDW_FRAME | win32con.RDW_INVALIDATE | win32con.RDW_UPDATENOW | win32con.RDW_ALLCHILDREN)

    def checkWindowValidity(self, hwnd):
        if not hwnd:
            return False
        if not win32gui.IsWindow(hwnd):
            return False
        if self.prevWindow == hwnd:
            return False
        if self.parent == hwnd:
            return False
        return True

    def displayWindowInformation(self, hwnd):
        className = win32gui.GetClassName(hwnd)
        windowText = win32gui.GetWindowText(hwnd)
        message = ['Handle:' + str(hwnd),
                   'Class Name:' + className,
                   'Window Text:' + windowText]
        self.sig_spy.emit(message)
