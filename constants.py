import os

APP_NAME = "Cars & Pedestrians Detector"
CARS_CLASSIFIER_FILE = 'haarcascades/haarcascade_cars.xml'
PEDESTRIANS_CLASSIFIER_FILE = 'haarcascades/haarcascade_fullbody.xml'

WELCOME_MESSAGE = f"""Hey, Welcome to {APP_NAME}"""

MENU_TEXT = """\nSelect SOURCE type from menu:
1. Image
2. Video
0. Exit
"""

IMAGE = 'image'
VIDEO = 'video'
EXIT = 'Exit'

SOURCES = {
    '1': IMAGE,
    '2': VIDEO,
    '0': EXIT
}

ASK_CONTENT_PATH_TEXT = """\nPlease enter relative or absolute path of {content_type}, or press
Enter to use sample data.
{content_type} path (press Enter to use sample data): """

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

IMAGE_SAMPLE_CONTENT = 'sample_data/image1.jpg'
VIDEO_SAMPLE_CONTENT = 'sample_data/video1.mp4'

BEFORE_PREVIEW_TEXT = """\nYou will see the preview in moments.
Press Esc to exit."""

FIRST_TIME_PREVIEWING = True

STROKE_THICKNESS = 3
PEDESTRIANS_STROKE_COLOR = (0, 255, 0)  # Green
CARS_STROKE_COLOR = (0, 0, 255)  # Red

ASCII_CODES_OF_EXIT_KEYS = (27, 81, 113)  # (Esc, Q, q) ascii codes
