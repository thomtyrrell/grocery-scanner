from urllib import request

from PIL import Image
import pytesseract
import cv2

#web source
#request.urlopen("https://i.stack.imgur.com/HWLay.gif")
#Image.open().convert('RGBA')

#image = Image.open("images/text_source.bmp")
#image.save('images/pillow_text_source.png','PNG')

image = cv2.imread("images/text_source.png")
print("Original Image:  ", pytesseract.image_to_string(image))

bw_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('images/bw_text_source.png',bw_image)
print("Black and White:  ", pytesseract.image_to_string(bw_image))

# bw_image = cv2.medianBlur(bw_image,5)
# cv2.imwrite('images/blurred_text_source.png',bw_image)
# print("Blurred:  ", pytesseract.image_to_string(bw_image))

ret,thresh_image = cv2.threshold(bw_image,127,255,cv2.THRESH_BINARY)
cv2.imwrite('images/thresh_text_source.png',thresh_image)
print("Global Threshold:  ", pytesseract.image_to_string(thresh_image))

mean_image = cv2.adaptiveThreshold(bw_image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
cv2.imwrite('images/mean_text_source.png',mean_image)
print("Mean Smoothing:  ", pytesseract.image_to_string(mean_image))

gaussian_image = cv2.adaptiveThreshold(bw_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
cv2.imwrite('images/gaussian_text_source.png',gaussian_image)
print("Gaussian Smoothing:  ", pytesseract.image_to_string(gaussian_image))