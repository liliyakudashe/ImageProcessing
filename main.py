import numpy as np
import cv2


size = 600
image = np.zeros((size, size, 3), dtype=np.uint8)
image.fill(0)

start_color = (255, 255, 255)
end_color = (0, 0, 255)

for i in range(size):
    current_color = [int(start_color[c] + (end_color[c] - start_color[c]) * i / size) for c in range(3)]
    image[:, i] = current_color

# cv2.circle(image, (300, 300), 200, (255, 255, 255), 5)


cv2.line(image, (350, 300), (350, 250), (255, 0, 0), 3)
cv2.line(image, (320, 300), (320, 250), (255, 0, 0), 3)
cv2.line(image, (270, 300), (270, 250), (255, 0, 0), 3)
cv2.line(image, (240, 300), (240, 250), (255, 0, 0), 3)

cv2.line(image, (240, 250), (270, 250), (0, 0, 255), 3)
cv2.line(image, (320, 250), (350, 250), (0, 0, 255), 3)

cv2.ellipse(image, (295, 300), (55, 60), 0, 0, 180, (0, 255, 0), 3)
cv2.ellipse(image, (295, 300), (25, 30), 0, 0, 180, (0, 255, 0), 3)


cv2.imshow('Urban Logo', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


