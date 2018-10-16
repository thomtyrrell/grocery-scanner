from pdf2image import convert_from_path
import cv2


def convert_PDF(path):
    images = convert_from_path(path)

    for i in range(len(images)):
        images[i].save('images/receipt_' + str(i) + '.png', 'PNG')

    return images