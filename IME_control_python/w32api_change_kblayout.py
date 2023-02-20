# 變更鍵盤佈局, set keyboard layout

from win32con import WM_INPUTLANGCHANGEREQUEST, KLF_REORDER
import win32gui
import win32api

# 語言代碼
# https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/available-language-packs-for-windows?view=windows-11
LID = {0x0404: "Chinese (Traditional, Taiwan)	zh-TW",
       0x0409: 'English (United States)	en-US',
       0x0411: 'Japanese (Japan)	ja-JP'}

# 獲取前景視窗控制碼
hwnd = win32gui.GetForegroundWindow()
print('GetForegroundWindow:', hex(hwnd))

# 獲取前景視窗標題, 非必要
title = win32gui.GetWindowText(hwnd)
print('當前視窗：' + title)

# 獲取鍵盤佈局列表, 非必要
im_list = win32api.GetKeyboardLayoutList()
im_list = list(map(hex, im_list))

# 載入英文鍵盤布局
ime=win32api.LoadKeyboardLayout('00000409', KLF_REORDER)

# 設定鍵盤佈局爲英文
win32api.SendMessage(hwnd, WM_INPUTLANGCHANGEREQUEST, 0, 0x0409)

