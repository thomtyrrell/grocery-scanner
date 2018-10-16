import numpy as np

from PIL import Image

import pytesseract
import cv2

import pdf2list


#######################################
# Receipt Scanning
#######################################

images = pdf2list.convert_PDF('images/SS receipts.pdf')

for i in images:
    bw_i = cv2.cvtColor(np.array(i), cv2.COLOR_BGR2GRAY)
    _, th_i = cv2.threshold(bw_i, 210, 255, cv2.THRESH_BINARY)
    cv2.imwrite('images/receipt' + str(np.random.random(1)) + '.png', th_i)
    print(pytesseract.image_to_string(th_i))