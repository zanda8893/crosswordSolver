#!/usr/bin/python3
# Alexander Hallard - OCR to get clues for crossword
import re
import cv2
import pytesseract

patten = r"\(\d+((\-|\,)\d+){0,2}\)"

img = cv2.imread("clues.jpg")

config = ('--oem 3 --psm 3')

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

text = pytesseract.image_to_string(img, config=config)

text = text.replace('\n','')

#print (text)

#clues = re.findall(patten, text)
#clues = re.split(patten, text)
for m in re.finditer(patten, text):
    print(m[0])
    print(m.start(g))

#print (clues)
