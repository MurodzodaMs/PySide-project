from ui.lesson_page import LessonWindow
from PySide6.QtWidgets import QMessageBox
from db import *



class lessonController:
    def __init__(self, window: LessonWindow):
        self.window = window
        self.window.add_block_button.clicked.connect(self.to_add_block)
        self.window.delete_button.clicked.connect(self.delete_lesson)

    def lesson_page_by_id(self, lesson_id: int):
        table = read_blocks_by_lesson(lesson_id)
        self.window.show_blocks(table)

    def to_add_block(self):
        self.window.send_add_block_signal()

    def find_lesson_id_and_title(self, lesson_id):
        self.window.lesson_id = lesson_id
        title = get_title_by_lesson_id(lesson_id)
        self.window.title.setText(f'<h1>{title[0]}</h1>')

    def delete_lesson(self):
        lesson_id = self.window.lesson_id
        delete_lesson(lesson_id)
        self.window.send_delete_lesson_signal()
        QMessageBox.information(self.window, 'Success',
            'Lesson was deleted successfully'
        )
