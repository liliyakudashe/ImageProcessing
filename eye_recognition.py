import cv2

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


def process_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(eyes) > 0:
        min_x = min(eyes[:, 0])
        min_y = min(eyes[:, 1])
        max_x = max(eyes[:, 0] + eyes[:, 2])
        max_y = max(eyes[:, 1] + eyes[:, 3])


        eye_region_gray = gray[min_y:max_y, min_x:max_x]

        blurred_eye_region = cv2.GaussianBlur(eye_region_gray, (25, 25), 7)

        eye_region_bgr = cv2.cvtColor(blurred_eye_region, cv2.COLOR_GRAY2BGR)

        frame[min_y:max_y, min_x:max_x] = eye_region_bgr

    return frame

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    processed_frame = process_frame(frame)

    cv2.imshow('Processed Frame', processed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

