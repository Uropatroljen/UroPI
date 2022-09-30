import cv2
import numpy as np
from urllib.request import urlopen

class c_Camera:

#This sample code can get a video stream from the ESP32-cam by HTTP request
#We would like to push this stream of bytearrys to the android app
#Change method name to get stream data
    url = "http://192.168.43.161/capture"
    def GetStream(self):
        while True:
            img_resp = urlopen(self.url)
            imgnp = np.asarray(bytearray(img_resp.read()), dtype="uint8")
            print(imgnp)
            print(len(imgnp))
            img = cv2.imdecode(imgnp, -1)
            cv2.imshow("Camera", img)
            if cv2.waitKey(1) == 113:
                break