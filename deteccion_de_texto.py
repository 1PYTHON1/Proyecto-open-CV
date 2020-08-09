# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 21:09:03 2020

@author: Admin
"""

import cv2
import pytesseract


imagen = cv2.imread("texto_largo.png")
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
texto=pytesseract.image_to_string(imagen)
print(texto)