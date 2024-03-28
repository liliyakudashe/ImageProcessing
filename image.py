import cv2
import numpy as np

image = cv2.imread('note.jpg')
black_bg = np.zeros_like(image, dtype='uint8')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
ed = cv2.Canny(blurred, 30, 30)

contours, _ = cv2.findContours(ed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

upper_contours = []
middle_contours = []
lower_contours = []

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if y < image.shape[0] / 4.8:
        upper_contours.append(contour)
    elif y < 2 * image.shape[0] / 4.8:
        middle_contours.append(contour)
    else:
        lower_contours.append(contour)

cv2.drawContours(black_bg, upper_contours, -1, (0, 255, 0), 2)
cv2.drawContours(black_bg, middle_contours, -1, (0, 0, 255), 2)
cv2.drawContours(black_bg, lower_contours, -1, (255, 0, 255), 2)

cv2.imshow('Processed Image', black_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
