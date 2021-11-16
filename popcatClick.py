import win32api
import win32con
import time


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


time.sleep(5)  # Time to wait before start clicking
for i in range(1000):  # 1000 is the number of desired clicks
    click(960, 540)  # Clicks location (x,y) and these coordinates are the middle of screen in case of 1920 * 1080 resolution
