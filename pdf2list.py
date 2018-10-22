from pdf2image import convert_from_path
import cv2


def convert_PDF(path, store = ''):
    images = convert_from_path(path)

    for i in range(len(images)):
        images[i].save('images/' + store + '_receipt_' + str(i) + '.png', 'PNG')

    return images
