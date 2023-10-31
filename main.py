from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from duixiang import Ui_MainWindow
from spy import SpyLabel
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


class Win(QMainWindow):
    sig = Signal(object)

    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.obj_list = []
        self.flag = False
        self.ed = QLineEdit(self)
        self.ed.resize(50, 20)
        self.ed.setText('20')
        self.aa = self.ed.text()

        self.btn = QPushButton(self)
        self.btn.setGeometry(520, -5, 80, 35)
        self.btn.setText('截屏')
        self.btn.setStyleSheet('background-color: rgba(255, 255, 255, 50);')
        self.btn.clicked.connect(self.prtsc)

        self.add_com()

        self.ui.pushButton.clicked.connect(self.add_com)
        self.ui.comboBox.activated.connect(self.show_group)
        self.pixmap = QPixmap('./image/background.jpg')

    def paintEvent(self, event):
        painter = QPainter(self)
        # pixmap = QPixmap('./image/background.jpg')
        painter.drawPixmap(self.rect(), self.pixmap)

    def get_handle(self):
        all_handle = []
        win32gui.EnumChildWindows(None, lambda handle, param: param.append(hex(handle)), all_handle)
        handle = [i for i in all_handle if win32gui.GetWindowText(eval(i)) == '阴阳师-网易游戏']
        for j in handle:
            x, y, w, h = win32gui.GetWindowRect(eval(j))
            win32gui.MoveWindow(eval(j), x, y, 800, 480, True)
        return handle

    def add_com(self):
        handle = self.get_handle()
        self.ui.comboBox.clear()
        if not self.flag:
            self.flag = True
            if len(handle) > 0:
                for i in handle:
                    info = {
                        'handle': i,
                        'gbox': gbox(self),
                        'name': f'设备{i}'
                    }
                    self.obj_list.append(info)
            else:
                info = {
                    'handle': '未检测到',
                    'gbox': gbox(self),
                    'name': '设备未检测到'
                }
                self.obj_list.append(info)
        else:
            handle_list = []
            for j in self.obj_list:
                handle_list.append(j['handle'])
            if len(handle) > 0:
                for k in handle:
                    if k not in handle_list:
                        info = {
                            'handle': k,
                            'gbox': gbox(self),
                            'name': f'设备{k}'
                        }
                        self.obj_list.append(info)
                for l in handle_list:
                    if l not in handle:
                        for m in self.obj_list:
                            if m['handle'] == l:
                                m['gbox'].deleteLater()
                                del m['gbox']
                                self.obj_list.remove(m)
            else:
                for n in self.obj_list:
                    n['gbox'].deleteLater()
                    del n['gbox']
                self.obj_list.clear()
                info = {
                    'handle': '未检测到',
                    'gbox': gbox(self),
                    'name': '设备未检测到'
                }
                self.obj_list.append(info)
        for o in self.obj_list:
            self.ui.comboBox.addItem(o['name'])
            o['gbox'].setTitle(o['name'])
            o['gbox'].setGeometry(10, 110, 580, 410)
            o['gbox'].setHidden(True)
        self.ui.comboBox.setCurrentIndex(0)
        self.obj_list[0]['gbox'].setHidden(False)

    def show_group(self):
        if self.ui.comboBox.activated:
            text = self.ui.comboBox.currentText()
            for i in self.obj_list:
                if i['name'] == text:
                    handle = i['handle']
                    if handle != '未检测到':
                        try:
                            win32gui.SetForegroundWindow(eval(handle))  # 窗口置顶
                            i['gbox'].setHidden(False)
                        except:
                            self.add_com()
                else:
                    i['gbox'].setHidden(True)


class gbox(QGroupBox):
    sig = Signal(str)

    def __init__(self, parent=None):
        super(gbox, self).__init__(parent)
        self.sig.connect(self.update_text)
        self.count = 0
        self.tp_count = 0
        self.tp_status = [[0, 0, 0], [0, 0, 0], [0, 0, 0],
                          [0, 0, 0], [0, 0, 0], [0, 0, 0],
                          [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.setupUi()

    def setupUi(self):
        self.groupBox_2 = QGroupBox(self)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 20, 521, 51))
        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(30, 20, 91, 16))
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(130, 20, 61, 16))
        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(210, 20, 51, 16))

        self.radioButton_tp = QRadioButton(self.groupBox_2)
        self.radioButton_tp.setObjectName(u"radioButton_5")
        self.radioButton_tp.setGeometry(QRect(290, 20, 51, 16))

        self.radioButton_ts = QRadioButton(self.groupBox_2)
        self.radioButton_ts.setObjectName(u"radioButton_6")
        self.radioButton_ts.setGeometry(QRect(370, 20, 51, 16))

        self.radioButton_hd = QRadioButton(self.groupBox_2)
        self.radioButton_hd.setObjectName(u"radioButton_7")
        self.radioButton_hd.setGeometry(QRect(450, 20, 51, 16))

        self.groupBox_3 = QGroupBox(self)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 90, 521, 51))
        self.radioButton_2 = QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(30, 20, 61, 16))
        self.radioButton_5 = QRadioButton(self.groupBox_3)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(110, 20, 61, 16))
        self.radioButton_6 = QRadioButton(self.groupBox_3)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(190, 20, 61, 16))
        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 150, 521, 241))
        self.retranslateUi()

    def retranslateUi(self):
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u526f\u672c", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5fa1\u9b42/\u65e5\u8f6e", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4e1a\u539f\u706b", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5fa1\u7075", None))
        self.radioButton_tp.setText('突破')
        self.radioButton_ts.setText('探索')
        self.radioButton_hd.setText('活动')
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5355\u5237", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u6253\u624b", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\u53f8\u673a", None))

        self.textBrowser.setText('祝您生活愉快！！！')
        self.textBrowser.setStyleSheet('background-color: rgba(255, 255, 255, 50);')
        for i in [self.radioButton, self.radioButton_3, self.radioButton_4,
                  self.radioButton_tp, self.radioButton_hd, self.radioButton_ts]:
            i.clicked.connect(lambda: self._tp())

    def _tp(self):
        if self.radioButton_tp.isChecked():
            self.radioButton_2.setText('为了赢')
            self.radioButton_5.setText('为了输')
            self.radioButton_6.setHidden(True)
        else:
            self.radioButton_2.setText('单刷')
            self.radioButton_5.setText('打手')
            self.radioButton_6.setHidden(False)

    def update_text(self, msg):
        t = time.strftime('%H:%M:%S', time.localtime())
        leng0 = len(msg)
        leng1 = sum(i.isalpha() for i in msg)
        leng2 = leng0 - leng1
        self.textBrowser.append(f"{msg}{'.' * (30 - (2 * leng1 + leng2))}{t}")


class Main(Win):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.flag_run = False
        self.ui.pushButton_2.clicked.connect(self.sel_mode)
        self.init_hash()

        self.m_ctrl = MulCtrl(self.sig)
        self.sig.connect(self.m_ctrl._click)

        self.model = '0'  # 0为前台模式，1为后台模式

        self._spy = SpyLabel(self)
        self._spy.setGeometry(30, 40, 30, 30)
        self.stat = QStatusBar(self)
        self.stat.setGeometry(0, 520, 600, 20)

    def out_put(self, message):
        self.stat.showMessage(",".join(message))

    # def leaveEvent(self, event):
    #     self.setWindowOpacity(0.01)
    #     print(f"出：{time.time()}")
    #
    # def enterEvent(self, event):
    #     self.setWindowOpacity(0.1)
    #     print(f"入：{time.time()}")

    def prtsc(self):
        hwnd = self.stat.currentMessage().split(',')[0][7:]
        if hwnd:
            screen = QApplication.primaryScreen()
            img = screen.grabWindow(int(hwnd)).toImage()
        else:
            x, y, w, h = ini.coordinates()
            pwnd = self.get_handle()
            if pwnd:
                screen = QApplication.primaryScreen()
                if x == y == w == h:
                    img = screen.grabWindow(eval(pwnd[0])).toImage()
                else:
                    img = screen.grabWindow(eval(pwnd[0]), x, y, w, h).toImage()
            else:
                self.stat.showMessage('未检测到窗口', 3000)
                return
        t = time.strftime('%Y%m%d%H%M%S', time.localtime())
        img.save(f'./image/screenshots/截图_{t}.jpg')
        self.stat.showMessage('截屏已保存', 3000)

    def config(self):
        with open('config.txt', 'r') as f:
            content = f.read().split('\n')
            model = content[1][-1]
            f.close()
        return model

    def init_hash(self):
        # 业原火、御灵相关
        yyh_c = Image.open('./image/yyh_c.jpg')  # 685, 370, 50, 40
        self.yyh_c = self.get_hash(yyh_c)
        yyh_v = Image.open('./image/yyh_v.jpg')  # 265, 95, 65, 45
        self.yyh_v = self.get_hash(yyh_v)
        yyh_f = Image.open('./image/yyh_f.jpg')  # 250, 85, 75, 45
        self.yyh_f = self.get_hash(yyh_f)
        yyh_a = Image.open('./image/yyh_a.jpg')  # 350, 310, 80, 55
        self.yyh_a = self.get_hash(yyh_a)
        yulin = Image.open('./image/yulin.jpg')  # 670, 365, 70, 50
        self.yulin = self.get_hash(yulin)

        # 御魂、日轮相关
        yh_c = Image.open('./image/yh_c.jpg')  # 720, 380, 60, 30
        self.yh_c = self.get_hash(yh_c)
        yh_v = Image.open('./image/yh_v.jpg')  # 260, 60, 70, 45
        self.yh_v = self.get_hash(yh_v)
        yh_f = Image.open('./image/yh_f.jpg')  # 250, 85, 75, 45
        self.yh_f = self.get_hash(yh_f)
        yh_a = Image.open('./image/yh_a.jpg')  # 350, 310, 80, 55
        self.yh_a = self.get_hash(yh_a)
        yh_num = Image.open('./image/yh_num.jpg')  # 360, 270, 70, 30
        self.yh_num = self.get_hash(yh_num)

        # 各类中断
        tl = Image.open('./image/tl.jpg')  # 340, 205, 105, 45  575, 120, -+10
        self.tl = self.get_hash(tl)
        xs = Image.open('./image/xs.jpg')  # 345, 95, 80, 25    520, 315, -+10
        self.xs = self.get_hash(xs)
        # 御魂已满
        o_flow = Image.open('./image/o_flow.jpg')  # 355, 185, 70, 40
        self.o_flow = self.get_hash(o_flow)

        # 活动
        hd_c = Image.open('./image/hd_c.jpg')
        self.hd_c = self.get_hash(hd_c)

        # 突破
        tp_true = Image.open('./image/break/tp_true.jpg')  # 460, 175, 25, 25
        self.tp_true = self.get_hash(tp_true)
        tp_c = Image.open('./image//break/tp_c.jpg')
        self.tp_c = self.get_hash(tp_c)
        # tp_zero = Image.open('./image//break/tp_zero.jpg')
        # self.tp_zero = self.get_hash(tp_zero)
        # tp_zero1 = Image.open('./image//break/tp_zero1.jpg')
        # self.tp_zero1 = self.get_hash(tp_zero1)

        tp_main = Image.open('./image//break/tp_main.jpg')
        self.tp_main = self.get_hash(tp_main)

        tp_back1 = Image.open('./image//break/tp_back1.jpg')
        self.tp_back1 = self.get_hash(tp_back1)
        tp_back2 = Image.open('./image//break/tp_back2.jpg')
        self.tp_back2 = self.get_hash(tp_back2)

        tp_fresh1 = Image.open('./image//break/tp_fresh1.jpg')
        self.tp_fresh1 = self.get_hash(tp_fresh1)
        tp_fresh2 = Image.open('./image//break/tp_fresh2.jpg')
        self.tp_fresh2 = self.get_hash(tp_fresh2)

    def sel_mode(self):
        self.model = ini.model()
        if self.ui.comboBox_3.currentIndex() == 0:
            self.get_check()
        elif self.ui.comboBox_3.currentIndex() == 1:
            if not self.flag_run:
                self.flag_run = True
                self.ui.pushButton_2.setText('停止')
                self.m_ctrl.s_game(self.flag_run)
            else:
                self.flag_run = False
                self.ui.pushButton_2.setText('开始')
                self.m_ctrl.s_game(self.flag_run)

    def get_check(self):
        if not self.flag_run:
            self.flag_run = True
            self.ui.pushButton_2.setText('停止')
            for i in self.obj_list:
                i['gbox'].count = 0
                if i['name'] != '设备未检测到':
                    self.global_thread(i)
                    self.aa = self.ed.text()
                    if i['gbox'].radioButton.isChecked():
                        # threading.Thread(target=self.run_yh, args=(i, )).start()
                        self.run_yh(i)

                    if i['gbox'].radioButton_3.isChecked():
                        # threading.Thread(target=self.run_yyh, args=(i,)).start()
                        self.run_yyh(i)

                    if i['gbox'].radioButton_4.isChecked():
                        # threading.Thread(target=self.run_yl, args=(i,)).start()
                        self.run_yl(i)

                    if i['gbox'].radioButton_hd.isChecked():
                        self.run_hd(i)

                    if i['gbox'].radioButton_tp.isChecked():
                        self.run_tp(i)

                    if i['gbox'].radioButton_ts.isChecked():
                        compare.run_ts(self, i)
        else:
            self.flag_run = False
            self.ui.pushButton_2.setText('开始')

    def global_thread(self, obj):
        """全局线程，自动模式开启就运行"""
        t_xs = threading.Thread(target=self.offer,
                                args=(obj, 345, 95, 80, 25, 510, 530, 305, 325, self.xs))  # 悬赏任务
        t_o_flow = threading.Thread(target=self.over_flow,
                                    args=(obj, 355, 185, 70, 40, self.o_flow))  # 御魂溢出

        t_xs.setDaemon(True)
        t_xs.start()
        t_o_flow.setDaemon(True)
        t_o_flow.start()

    def run_yh(self, obj):
        def run_ds(self, obj):
            pass
            # size = win32gui.GetWindowRect(eval(obj['handle']))
            # img = ImageGrab.grab((685+size[0]+8, 370+size[1]+30, 685+size[0]+50+8, 370+size[1]+40+30))
            # # img = ImageGrab.grab(size)
            # img.save('业原火.jpg')  # 800 * 480

            # screen = QApplication.primaryScreen()
            # img = screen.grabWindow(eval(obj['handle'])).toImage()
            # img.save('后台.jpg')  # 784 * 442

            # x+8, y+30

        def run_dz(self, obj):
            t1 = threading.Thread(target=self.victory,
                                  args=(obj, 260, 60, 70, 45, 630, 780, 320, 460, self.yh_v))  # 胜利 260,60,70,45
            t2 = threading.Thread(target=self.account,
                                  args=(obj, 350, 310, 80, 55, 630, 780, 320, 460, self.yh_a))  # 结算 350,310,80,55

            t1.setDaemon(True)
            t1.start()
            t2.setDaemon(True)
            t2.start()

        def run_dy(self, obj):
            t1 = threading.Thread(target=self.victory,
                                  args=(obj, 260, 60, 70, 45, 630, 780, 320, 460, self.yh_v))  # 胜利 260, 60, 70, 45
            t2 = threading.Thread(target=self.account,
                                  args=(obj, 350, 310, 80, 55, 630, 780, 320, 460, self.yh_a))  # 结算 350,310,80,55
            t3 = threading.Thread(target=self.challenge,
                                  args=(obj, 720, 380, 60, 30, 725, 785, 395, 445, self.yh_c))  # 挑战 720,380,60,30

            t1.setDaemon(True)
            t1.start()
            t2.setDaemon(True)
            t2.start()
            t3.setDaemon(True)
            t3.start()

        if obj['gbox'].radioButton_2.isChecked():
            run_ds(self, obj)
        if obj['gbox'].radioButton_5.isChecked():
            run_dz(self, obj)
        if obj['gbox'].radioButton_6.isChecked():
            run_dy(self, obj)

    def run_yyh(self, obj):
        t1 = threading.Thread(target=self.victory,
                              args=(obj, 265, 95, 65, 45, 630, 780, 320, 460, self.yyh_v))  # 胜利 260, 60, 70, 45
        t2 = threading.Thread(target=self.account,
                              args=(obj, 350, 310, 80, 55, 630, 780, 320, 460, self.yyh_a))  # 结算 350, 310, 80, 55
        t3 = threading.Thread(target=self.challenge,
                              args=(obj, 685, 370, 50, 40, 686, 752, 392, 455, self.yyh_c))  # 挑战 720, 380, 60, 30
        # t3 = threading.Thread(target=self.challenge,
        #                       args=(obj, 665, 355, 80, 70, 686, 752, 392, 455, self.yyh_c2))  # 挑战 720, 380, 60, 30
        t5 = threading.Thread(target=self.power,
                              args=(obj, 340, 205, 105, 45, 565, 585, 110, 130, self.tl))  # 关闭购买体力窗口

        t1.setDaemon(True)
        t1.start()
        t2.setDaemon(True)
        t2.start()
        t3.setDaemon(True)
        t3.start()
        t5.setDaemon(True)
        t5.start()

    def run_yl(self, obj):
        t1 = threading.Thread(target=self.victory,
                              args=(obj, 265, 95, 65, 45, 630, 780, 320, 460, self.yyh_v))  # 胜利 260, 60, 70, 45
        t2 = threading.Thread(target=self.account,
                              args=(obj, 350, 310, 80, 55, 630, 780, 320, 460, self.yyh_a))  # 结算 350, 310, 80, 55
        t3 = threading.Thread(target=self.challenge,
                              args=(obj, 670, 365, 70, 50, 686, 752, 392, 455, self.yulin))  # 挑战 720, 380, 60, 30

        t1.setDaemon(True)
        t1.start()
        t2.setDaemon(True)
        t2.start()
        t3.setDaemon(True)
        t3.start()

    def run_tp(self, obj):
        if not obj['gbox'].radioButton_6.isChecked():

            t1 = threading.Thread(target=self._run_tp,
                                  args=(obj,))
            t2 = threading.Thread(target=self.victory,
                                  args=(obj, 265, 95, 65, 45, 630, 780, 320, 460, self.yyh_v))  # 胜利 260, 60, 70, 45
            t3 = threading.Thread(target=self.account,
                                  args=(obj, 350, 310, 80, 55, 550, 720, 200, 340, self.yh_a))  # 结算 350,310,80,55
            t4 = threading.Thread(target=self.failure,
                                  args=(obj, 250, 85, 75, 45, 630, 720, 200, 340, self.yyh_f))  # 失败
            # t5 = threading.Thread(target=self.if_zero,
            #                       args=(obj,))  # 查询突破券是否用完

            t1.setDaemon(True)
            t1.start()
            t2.setDaemon(True)
            t2.start()
            t3.setDaemon(True)
            t3.start()
            t4.setDaemon(True)
            t4.start()
            # t5.setDaemon(True)
            # t5.start()

            if obj['gbox'].radioButton_5.isChecked():
                t_f = threading.Thread(target=self._run_tp_failure,
                                       args=(obj,))

                t_f.setDaemon(True)
                t_f.start()

    def if_zero(self, obj):
        # pwnd = eval(obj['handle'])
        while self.flag_run:
            if obj['gbox'].tp_count >= 3:
                obj['gbox'].sig.emit('突破券为0,停止突破！')
                self.sel_mode()
            else:
                obj['gbox'].tp_count = 0
            time.sleep(40)
            # time.sleep(random.randrange(150, 250) / 100)
            # img_zero = self.prtsr(pwnd, 700, 8, 34, 22)
            # if self.hamming(self.get_hash(img_zero), self.tp_zero, 5)\
            #         or self.hamming(self.get_hash(img_zero), self.tp_zero1, 5):  # 查询突破券是否为0
            #     self.sel_mode()
            #     obj['gbox'].sig.emit('突破券为0,停止突破！')

    def _run_tp_failure(self, obj):
        pwnd = eval(obj['handle'])
        while self.flag_run:
            t = random.randrange(70, 130) / 100
            time.sleep(t)
            tp_back1 = self.prtsr(pwnd, 12, 9, 21, 21)
            if self.hamming(self.get_hash(tp_back1), self.tp_back1, int(self.aa)):  # 查询是否有可突破结界
                self.click(pwnd, 12, 33, 9, 30)
                obj['gbox'].sig.emit('点击返回！')
                t1 = random.randrange(120, 220) / 100
                time.sleep(t1)

            tp_back2 = self.prtsr(pwnd, 435, 240, 41, 41)
            if self.hamming(self.get_hash(tp_back2), self.tp_back2, int(self.aa)):  # 查询是否有进攻按钮
                self.click(pwnd, 440, 470, 245, 275)
                obj['gbox'].sig.emit('确认返回！')
                time.sleep(random.randrange(300, 400) / 100)

    def _run_tp(self, obj):
        pwnd = eval(obj['handle'])
        f_num = 0
        # obj['gbox'].tp_count = 0
        while self.flag_run:
            t = random.randrange(70, 130) / 100
            time.sleep(t)
            img_main = self.prtsr(pwnd, 80, 385, 33, 33)
            if self.hamming(self.get_hash(img_main), self.tp_main, int(self.aa)):  # 是否在突破界面
                t_main = random.randrange(100, 250) / 100
                time.sleep(t_main)
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if self.flag_run:
                            f_num += 1  # 若识别到可突破结节则置0，否则+1，循环判断，当值大于18时，说明两轮循环均未检测到可突破结界，则操作刷新突破
                            if f_num < 36:
                                x1, y1 = 474 + (j * 204), 171 + (i * 83)
                                img1 = self.prtsr(pwnd, x1, y1, 16, 16)
                                if self.hamming(self.get_hash(img1), self.tp_true, int(self.aa)):  # 查询是否有可突破结界
                                    f_num = 0
                                    obj['gbox'].sig.emit('点击突破！')
                                    self.click(pwnd, x1 - 100, x1, y1, y1 + 45)
                                    t1 = random.randrange(150, 250) / 100
                                    time.sleep(t1)
                                x2, y2 = 398 + (j * 204), 301 + (i * 83)
                                img2 = self.prtsr(pwnd, x2, y2, 83, 42)
                                if self.hamming(self.get_hash(img2), self.tp_c, int(self.aa)):  # 查询是否有进攻按钮
                                    f_num = 0
                                    obj['gbox'].sig.emit('点击进攻！')
                                    # obj['gbox'].tp_count += 1
                                    # print(obj['gbox'].tp_count)
                                    self.click(pwnd, x2 + 10, x2 + 73, y2 + 5, y2 + 37)
                                    time.sleep(random.randrange(250, 350) / 100)
                                    for k in range(3):
                                        img3 = self.prtsr(pwnd, x2, y2, 83, 42)
                                        if k == 2:
                                            if self.hamming(self.get_hash(img3), self.tp_c, int(self.aa)):
                                                obj['gbox'].sig.emit('突破券为0,停止突破！')
                                                self.sel_mode()
                                        else:
                                            if self.hamming(self.get_hash(img3), self.tp_c, int(self.aa)):  # 查询是否有进攻按钮
                                                self.click(pwnd, x2 + 10, x2 + 73, y2 + 5, y2 + 37)
                                                time.sleep(random.randrange(20, 50) / 100)

                            else:
                                img_fresh1 = self.prtsr(pwnd, 623, 348, 41, 41)
                                if self.hamming(self.get_hash(img_fresh1), self.tp_fresh1, int(self.aa)):  # 查询是否可刷新突破
                                    obj['gbox'].sig.emit('点击刷新！')
                                    self.click(pwnd, 610, 680, 348, 389)
                                    t_fresh = random.randrange(120, 220) / 100
                                    time.sleep(t_fresh)
                                img_fresh2 = self.prtsr(pwnd, 445, 245, 41, 41)
                                if self.hamming(self.get_hash(img_fresh2), self.tp_fresh2, int(self.aa)):  # 确定刷新
                                    obj['gbox'].sig.emit('确定刷新！')
                                    self.click(pwnd, 445, 486, 245, 286)
                                    f_num = 0

    def run_hd(self, obj):
        t1 = threading.Thread(target=self.victory,
                              args=(obj, 265, 95, 65, 45, 630, 780, 320, 460, self.yyh_v))  # 胜利 260, 60, 70, 45
        t2 = threading.Thread(target=self.account,
                              args=(obj, 350, 310, 80, 55, 630, 780, 320, 460, self.yyh_a))  # 结算 350, 310, 80, 55
        t3 = threading.Thread(target=self.challenge,
                              args=(obj, 700, 370, 50, 50, 700, 750, 370, 420, self.hd_c))  # 挑战 720, 380, 60, 30

        t1.setDaemon(True)
        t1.start()
        t2.setDaemon(True)
        t2.start()
        t3.setDaemon(True)
        t3.start()

    def victory(self, obj, x, y, w, h, x1, x2, y1, y2, img_hash):
        pwnd = eval(obj['handle'])
        while self.flag_run:
            t = random.randrange(70, 130) / 100
            time.sleep(t)
            img = self.prtsr(pwnd, x, y, w, h)
            if self.hamming(self.get_hash(img), img_hash, int(self.aa)):
                obj['gbox'].count += 1
                text = f"已完成副本{obj['gbox'].count}次！"
                obj['gbox'].sig.emit(text)
                self.creat_click(pwnd, x1, x2, y1, y2, 2, 5)
                time.sleep(random.randrange(80, 130) / 100)

    def failure(self, obj, x, y, w, h, x1, x2, y1, y2, img_hash):
        pwnd = eval(obj['handle'])
        while self.flag_run:
            t = random.randrange(70, 130) / 100
            time.sleep(t)
            img = self.prtsr(pwnd, x, y, w, h)
            if self.hamming(self.get_hash(img), img_hash, int(self.aa)):
                obj['gbox'].sig.emit('点击失败！')
                self.creat_click(pwnd, x1, x2, y1, y2, 2, 5)

    def mate_image(self, pwnd, x, y, w, h):
        img = self.prtsr(pwnd, x, y, w, h)
        if self.hamming(self.get_hash(img), self.yh_num, int(self.aa)):
            return False
        else:
            return True

    def challenge(self, obj, x, y, w, h, x1, x2, y1, y2, img_hash):
        pwnd = eval(obj['handle'])
        while self.flag_run:
            t = random.randrange(70, 130) / 100
            time.sleep(t)
            img = self.prtsr(pwnd, x, y, w, h)
            if self.mate_image(pwnd, 360, 270, 70, 30):
                if self.hamming(self.get_hash(img), img_hash, int(self.aa)):
                    obj['gbox'].sig.emit("点击挑战！")
                    self.creat_click(pwnd, x1, x2, y1, y2, 1, 3)

    def account(self, obj, x, y, w, h, x1, x2, y1, y2, img_hash):
        pwnd = eval(obj['handle'])
        while self.flag_run:
            t = random.randrange(70, 130) / 100
            time.sleep(t)
            img = self.prtsr(pwnd, x, y, w, h)
            if self.hamming(self.get_hash(img), img_hash, int(self.aa)):
                obj['gbox'].sig.emit("点击结算！")
                self.creat_click(pwnd, x1, x2, y1, y2, 2, 6)

    def over_flow(self, obj, x, y, w, h, img_hash):
        pwnd = eval(obj['handle'])
        while self.flag_run:
            time.sleep(random.randrange(300, 500) / 100)
            img = self.prtsr(pwnd, x, y, w, h)
            if self.hamming(self.get_hash(img), img_hash, int(self.aa)):
                obj['gbox'].sig.emit('御魂上限， 请及时清理！')
                self.sel_mode()

    def offer(self, obj, x, y, w, h, x1, x2, y1, y2, img_hash):
        pwnd = eval(obj['handle'])
        while self.flag_run:
            time.sleep(random.randrange(300, 500) / 100)
            img = self.prtsr(pwnd, x, y, w, h)
            if self.hamming(self.get_hash(img), img_hash, int(self.aa)):
                obj['gbox'].sig.emit('取消悬赏任务！')
                self.click(pwnd, x1, x2, y1, y2)

    def power(self, obj, x, y, w, h, x1, x2, y1, y2, img_hash):
        pwnd = eval(obj['handle'])
        while self.flag_run:
            time.sleep(random.randrange(300, 500) / 100)
            img = self.prtsr(pwnd, x, y, w, h)
            if self.hamming(self.get_hash(img), img_hash, int(self.aa)):
                obj['gbox'].sig.emit('关闭购买体力窗口！')
                self.click(pwnd, x1, x2, y1, y2)

    def creat_click(self, pwnd, x1, x2, y1, y2, m, n):
        for i in range(random.randrange(m, n)):
            time.sleep(random.randrange(100, 250) / 1000)
            pos_x = random.randrange(x1, x2)
            pos_y = random.randrange(y1, y2)
            self.click_pos(pwnd, pos_x, pos_y)
        t = random.randrange(50, 200) / 100
        time.sleep(t)

    def click(self, pwnd, x1, x2, y1, y2):
        time.sleep(random.randrange(250, 500) / 1000)
        pos_x = random.randrange(x1, x2)
        pos_y = random.randrange(y1, y2)
        self.click_pos(pwnd, pos_x, pos_y)

    def q_for_p(self, img):
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, 'jpg')
        pil_im = Image.open(io.BytesIO(buffer.data()))
        return pil_im

    def prtsr(self, pwnd, x, y, w, h):
        if self.model == '0':
            x0, y0, w0, h0 = win32gui.GetWindowRect(pwnd)
            img = ImageGrab.grab((x0 + x + 8, y0 + y + 30, x0 + x + w + 8, y0 + y + h + 30))
        else:
            screen = QApplication.primaryScreen()
            scr = screen.grabWindow(pwnd, x, y, w, h).toImage()
            img = ImageQt.fromqimage(scr)
            # img = self.q_for_p(scr)
        return img

    def click_pos(self, pwnd, pos_x, pos_y):
        """鼠标单击坐标（pos_x, pos_y）"""
        win32api.SendMessage(pwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(pos_x, pos_y))
        t = random.randrange(100, 250) / 1000
        time.sleep(t)
        win32api.SendMessage(pwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, win32api.MAKELONG(pos_x, pos_y))

    # 获得图像的hash值
    def get_hash(self, img):
        # img = img.resize((16, 16), Image.ANTIALIAS).convert('L')  # 抗锯齿 灰度
        img = img.resize((16, 16)).convert('L')  # 抗锯齿 灰度
        avg = sum(list(img.getdata())) / 256  # 计算像素平均值
        s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))  # 每个像素进行比对,大于avg为1,反之为0
        return ''.join(map(lambda j: '%x' % int(s[j:j + 4], 2), range(0, 256, 4)))
        # def bin_hex(s):
        #     a = []
        #     for j in range(0, 256, 4):
        #         b = int(s[j]) * 8 + int(s[j + 1]) * 4 + int(s[j + 2]) * 2 + int(s[j + 3])
        #         c = str(hex(b))[2:]
        #         a.append(c)
        #     e = ''.join(a)
        #     return e
        # k = bin_hex(s)
        # return k

    # 计算两个图像的汉明距离
    def hamming(self, hash1, hash2, n=20):
        b = False
        assert len(hash1) == len(hash2)
        # print(sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)))
        if sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)) < n:
            b = True
        return b


#
# class Th(QThread):
#     def __init__(self, target, args=()):
#         super().__init__()
#         self.target = target
#         self.args = args
#
#     def run(self):
#         self.target(*self.args)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.setWindowTitle('大公举V3.01')
    mainWindow.show()
    sys.exit(app.exec_())

# # 获取到text光标
# textCursor = gbox.textBrowser.textCursor()
# # 滚动到底部
# textCursor.movePosition(textCursor.End)
# # 设置光标到text中去
# gbox.textBrowser.setTextCursor(textCursor)
