from PIL import Image
import pytesseract
import cv2
import numpy as np


#######################################
# Receipt Scanning
#######################################

# import
image = cv2.imread("images/receipt.png")

# convert to black and white
bw_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('images/bw_receipt.png',bw_image)

# global threshold
ret,th1 = cv2.threshold(bw_image,225,255,cv2.THRESH_BINARY)
cv2.imwrite('images/thresh_receipt.png',th1)

# extract items
th1_receipt_text = pytesseract.image_to_string(th1)
print(th1_receipt_text.split("DAILY")[1].split("SUB")[0].strip().split("\n"))

# Get bounding box estimates
#print(pytesseract.image_to_boxes(bw_image))

# Get verbose data including boxes, confidences, line and page numbers
#print(pytesseract.image_to_data(bw_image))

# Get information about orientation and script detection
#print(pytesseract.image_to_osd(bw_image))

th2 = cv2.adaptiveThreshold(bw_image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(bw_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

# extract items
cv2.imwrite('images/th2_receipt.png',th2)
th2_receipt_text = pytesseract.image_to_string(th2)
print(th2_receipt_text)

# extract items
cv2.imwrite('images/th3_receipt.png',th3)
th3_receipt_text = pytesseract.image_to_string(th3)
print(th3_receipt_text)