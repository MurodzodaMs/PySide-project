from ui.lesson_update_page import LessonUpdateWindow
from PySide6.QtWidgets import QMessageBox
from db import *


class lessonUpdateController:
    def __init__(self, window: LessonUpdateWindow):
        self.window = window
        self.window.delete_block_signal.connect(
            self.delete_block_cont
        )

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

    def delete_block_cont(self, block_id):
        delete_block(block_id)
        self.lesson_page_by_id(self.window.lesson_id)
        QMessageBox.information(self.window, 'success',
                                'Block was deleted successfully'
                                )
