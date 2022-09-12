#Program to print text extracted from image
import pytesseract # this is tesseract module
import numpy as np
import cv2 # this is opencv module
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\saura\AppData\Local\Tesseract-OCR\tesseract.exe'
path= r"./images/*.jpg" #provide path to image here
img = cv2.imread(path,0)
img =cv2.threshold(np.array(img), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
img = cv2.medianBlur(img, 5)
text1 = pytesseract.image_to_string(Image.open(path),config="--psm 8")
text2 = pytesseract.image_to_string(Image.open(path),config="--psm 7")
text3 = pytesseract.image_to_string(Image.open(path),config="--psm 6")
print(text1 + '\n' + text2 + '\n'+ text3)
cv2.imshow('image',img) #displaying formatted image
cv2.waitKey()
