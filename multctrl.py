import win32gui
import win32con
import win32api
import time
import threading


class MulCtrl:
    # sig = Signal(object)

    def __init__(self, sig):
        self.sig = sig
        self.handle = []
        self.s_handle = None
        self.flag = False
        # self.sig.connect(self._click)

    def get_pos(self):
        while self.flag:
            if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
                while True:
                    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
                        pos = win32api.GetCursorPos()
                        self.sig.emit(pos)
                        break

    def s_game(self, flag):
        self.flag = flag
        if not self.flag:
            self.handle = []
        else:
            self.handle = self.pwnd()
            t1 = threading.Thread(target=self.get_pos)
            t1.setDaemon(True)
            t1.start()

    def pwnd(self):
        all_handle = []
        handle = []
        x_y = []
        win32gui.EnumChildWindows(None, lambda handle, param: param.append(hex(handle)), all_handle)

        for i in all_handle:
            soft_name = win32gui.GetWindowText(eval(i))  # 获取该句柄所对应的程序名称
            if soft_name == '阴阳师-网易游戏':
                # win32gui.MoveWindow(eval(i), 0, 0, 880, 800, True)
                handle.append(i)

        if len(handle) > 1:
            for j in handle:
                x, y, w, h = win32gui.GetWindowRect(eval(j))
                x_y.append(x+y)
            index = x_y.index(min(x_y))
            s_handle = handle[index]
            handle.remove(s_handle)
            self.s_handle = s_handle
            return handle

    def _click(self, pos):
        if self.s_handle:
            x0, y0, w0, h0 = win32gui.GetWindowRect(eval(self.s_handle))
            x = pos[0] - x0
            y = pos[1] - y0
            if x in range(w0+1) and y in range(h0+1):
                if self.handle:
                    for i in self.handle:
                        click_pos = win32api.MAKELONG(x-8, y-30)
                        win32api.SendMessage(eval(i), win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click_pos)
                        time.sleep(0.2)
                        win32api.SendMessage(eval(i), win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, click_pos)
