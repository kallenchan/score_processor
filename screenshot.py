import cv2
import pyscreenshot as ImageGrab
import datetime
import numpy as np
import pytesseract
# from PIL import ImageGrab

# Capturing the Image
# img=ImageGrab.grab(bbox=(1400,-280,1800,-140))

class screenshot_process:
    def __init__(self,targetDir=None):
        self.dt_start =datetime.datetime.utcnow()
        self.targetDir=targetDir
        # self.pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    def capture_screenshot(self,bbox=(1000,600,1600,750)):
        img=ImageGrab.grab(bbox=bbox)
        dt_now=datetime.datetime.utcnow()
        file_name='./screenshots/screenshot{}.png'.format(np.round((dt_now-self.dt_start).total_seconds(),0))
        img.save(file_name)
        
        #Text Recognition
        source=cv2.imread(file_name)
        scaleX=0.6
        scaleY=0.6
        scaleUp=cv2.resize(source,None,
                    fx= scaleX*3, 
                    fy= scaleY*3, 
                    interpolation= cv2.INTER_LINEAR)
        img = cv2.cvtColor(scaleUp, 
                    cv2.COLOR_BGR2GRAY)
        print(file_name)
        print(pytesseract.image_to_string(img))

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
application=screenshot_process()
application.capture_screenshot(bbox=(1400,-280,1800,-140))