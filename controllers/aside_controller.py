from ui.aside_page import AsideWindow
from db import read_lesson


class AsideController:
    def __init__(self, window: AsideWindow):
        self.window = window
        self.lessons = self.give_lesson_list()
        self.window.show_lessons(self.lessons)

    def give_lesson_list(self):
        lessons = read_lesson()
        return lessons
