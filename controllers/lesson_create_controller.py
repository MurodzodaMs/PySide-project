from PySide6.QtWidgets import QMessageBox
from ui.lesson_create_page import LessonCreateWindow
from db import create_lesson, check_lesson


class LessonCreateController:
    def __init__(self, window:LessonCreateWindow):
        self.window = window
        self.window.button.clicked.connect(self.create_lesson)
        self.window.line.returnPressed.connect(self.create_lesson)

    def create_lesson(self):
        title = self.window.line.text()
        if title:
            if check_lesson(title):
                QMessageBox.information(self.window, 'Error', 'this title is already exists')
                return None
            create_lesson(title)
            QMessageBox.information(self.window, 'Success', 'lesson was created successfully')
            self.window.lesson_created.emit()
        else:
            QMessageBox.information(self.window, 'Error', 'please full all line')
        
        self.window.line.clear()
        