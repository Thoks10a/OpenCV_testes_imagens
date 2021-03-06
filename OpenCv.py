import cv2 as cv
import numpy as np
import os
from time import time
from win32 import win32gui
from win32 import win32ui
import win32con

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def window_capture():
    w = 1680 # set this
    h = 1050 # set this
    bmpfilenamename = "out.bmp" #set this

    hwnd = win32gui.FindWindow(None, 'Albion Online Client')
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
    
    # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype = "uint8")
    img.shape = (h, w,4)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle()) 
    
    img = img[...,:3]
    
    img = np.ascontiguousarray(img)
    
    
    return img

loop_time = time()

while True:
    
    screenshot = window_capture()
    # screenshot = np.array(screenshot)
    # screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
    # screenshot = screenshot[:, :, ::-1].copy()
    
    cv.imshow('Computer Vision ', screenshot)
    
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    
    

print('Done')       