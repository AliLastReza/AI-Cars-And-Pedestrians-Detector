import cv2
from constants import *

pedestrians_detector = cv2.CascadeClassifier(PEDESTRIANS_CLASSIFIER_FILE)
cars_detector = cv2.CascadeClassifier(CARS_CLASSIFIER_FILE)


def detect_cars_and_pedestrians(source, content_path):
    if source == IMAGE:
        detect_cars_and_pedestrians_from_image(image_path=content_path)
    elif source == VIDEO:
        detect_cars_and_pedestrians_from_video(video_path=content_path)
    else:
        raise NotImplemented


def mark_pedestrians_in_image(image, grayscaled_image):
    pedestrians_coordinates = pedestrians_detector.detectMultiScale(grayscaled_image)

    for x, y, w, h in pedestrians_coordinates:
        # print((x, y), (x+w, y+h))
        cv2.rectangle(image, (x, y), (x+w, y+h), PEDESTRIANS_STROKE_COLOR, STROKE_THICKNESS)


def mark_cars_in_image(image, grayscaled_image):
    cars_coordinates = cars_detector.detectMultiScale(grayscaled_image)

    for x, y, w, h in cars_coordinates:
        # print((x, y), (x+w, y+h))
        cv2.rectangle(image, (x, y), (x+w, y+h), CARS_STROKE_COLOR, STROKE_THICKNESS)


def detect_cars_and_pedestrians_from_image(image_path: str):
    image = cv2.imread(image_path)

    grayscaled_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    mark_pedestrians_in_image(image, grayscaled_image)
    mark_cars_in_image(image, grayscaled_image)

    cv2.imshow(APP_NAME, image)

    DISPLAYING = True
    while DISPLAYING:
        key = cv2.waitKey(1)

        if key in ASCII_CODES_OF_EXIT_KEYS:
            break

    cv2.destroyAllWindows()


def detect_cars_and_pedestrians_from_video(video_path: str):
    video_capture = cv2.VideoCapture(video_path)

    while True:
        read, frame = video_capture.read()

        if read:
            grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            break

        mark_pedestrians_in_image(frame, grayscaled_frame)
        mark_cars_in_image(frame, grayscaled_frame)

        cv2.imshow(APP_NAME, frame)
        key = cv2.waitKey(1)

        if key in ASCII_CODES_OF_EXIT_KEYS:
            break

    video_capture.release()
    cv2.destroyAllWindows()
