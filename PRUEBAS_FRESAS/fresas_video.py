# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:08:41 2020

@author: Admin
"""

import fresas_rojas as fr
import cv2

captura = cv2.VideoCapture("fresas3.mp4")

if captura.isOpened()==False:
    print("Error al abrir el video")
    
while captura.isOpened():
    resultado, video =captura.read()
    video=fr.detectar_fresa(video)
    if resultado == True:
        cv2.imshow('Mi video',video)
        if cv2.waitKey(1)&0xFF== ord('q'):
            break
    else:
        break

cv2.destroyAllWindows()