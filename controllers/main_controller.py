from ui.main_window import MainScreen
from ui.main_page import MainWindow

from ui.block_create_page import BlockWindow
from .block_controller import BlockController

from ui.lesson_page import LessonWindow
from .lesson_controller import lessonController

from ui.lesson_create_page import LessonCreateWindow
from .lesson_create_controller import LessonCreateController

from ui.aside_page import AsideWindow
from .aside_controller import AsideController

from ui.lesson_update_page import LessonUpdateWindow
from .lesson_update_controller import lessonUpdateController
from db import get_block_by_id


class MainController:
    def __init__(self, window: MainScreen):
        self.window = window

        self.main_page = MainWindow()
        self.block_page = BlockWindow()
        self.lesson_page = LessonWindow()
        self.lesson_create_page = LessonCreateWindow()
        self.lesson_update_page = LessonUpdateWindow()

        self.window.stack.addWidget(self.main_page)
        self.window.stack.addWidget(self.block_page)
        self.window.stack.addWidget(self.lesson_page)
        self.window.stack.addWidget(self.lesson_create_page)
        self.window.stack.addWidget(self.lesson_update_page)

        self.aside_controller = AsideController(self.window.aside)
        self.block_controller = BlockController(self.block_page)
        self.lesson_controller = lessonController(self.lesson_page)
        self.lesson_create_controller = LessonCreateController(
            self.lesson_create_page
        )
        self.lesson_update_controller = lessonUpdateController(
            self.lesson_update_page
        )

        self.window.aside.lesson_clicked.connect(self.open_lesson)
        self.lesson_create_page.lesson_created.connect(self.update_aside)
        self.lesson_page.delete_lesson_signal.connect(self.update_aside)
        self.lesson_page.delete_lesson_signal.connect(
            lambda: self.window.stack.setCurrentWidget(self.main_page)
        )
        self.lesson_page.add_block_signal.connect(self.go_to_add_block)
        self.lesson_page.update_lesson_signal.connect(self.open_update_lesson)
        self.lesson_update_page.update_block_signal.connect(
            self.open_update_block_page)

        self.main_page.create_lesson.clicked.connect(
            lambda: self.window.stack.setCurrentWidget(self.lesson_create_page)
        )

        self.lesson_page.back_button.clicked.connect(
            lambda: self.window.stack.setCurrentWidget(self.main_page)
        )

        self.block_page.back_button.clicked.connect(
            lambda: self.window.stack.setCurrentWidget(self.main_page)
        )

        self.lesson_create_page.back_button.clicked.connect(
            lambda: self.window.stack.setCurrentWidget(self.main_page)
        )

        self.lesson_update_page.back_button.clicked.connect(
            lambda: self.window.stack.setCurrentWidget(self.lesson_page)
        )

    def open_lesson(self, lesson_id):
        self.lesson_controller.find_lesson_id_and_title(lesson_id)
        self.lesson_controller.lesson_page_by_id(lesson_id)
        self.window.stack.setCurrentWidget(self.lesson_page)

    def update_aside(self):
        self.aside_controller.window.show_lessons(
            self.aside_controller.give_lesson_list()
        )

    def go_to_add_block(self, lesson_id):
        self.block_page.clear_data()
        self.block_page.get_lesson_id(lesson_id)
        self.window.stack.setCurrentWidget(self.block_page)

    def open_update_lesson(self, lesson_id):
        self.lesson_update_controller.find_lesson_id_and_title(lesson_id)
        self.lesson_update_controller.lesson_page_by_id(lesson_id)
        self.window.stack.setCurrentWidget(self.lesson_update_page)

    def open_update_block_page(self, block_id):
        block_data = get_block_by_id(block_id)
        if block_data:
            self.block_page.set_block_data(block_data)
            self.window.stack.setCurrentWidget(self.block_page)
