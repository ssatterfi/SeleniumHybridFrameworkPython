import os


def screenshot_path(filename):
    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    SCREENSHOTS = os.path.join(ROOT_DIR, 'Screenshots')
    return os.path.join(SCREENSHOTS, filename)
