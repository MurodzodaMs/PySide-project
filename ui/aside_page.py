from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QPushButton
from PySide6.QtCore import Signal


class AsideWindow(QWidget):
    lesson_clicked = Signal(int)

    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout(self)

        self.title = QLabel('<h1>Lessons')
        self.main_layout.addWidget(self.title)
        self.main_layout.addSpacing(15)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.container = QWidget()
        self.lessons_layout = QVBoxLayout(self.container)

        self.scroll_area.setWidget(self.container)
        self.main_layout.addWidget(self.scroll_area)
        self.main_layout.addStretch()

    def show_lessons(self, lessons: list[tuple]):
        # delete old items
        while self.lessons_layout.count():
            item = self.lessons_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()  # type: ignore


        for lesson in lessons:
            l_id = lesson[0]
            l_title = lesson[1]

            btn = QPushButton(l_title)
            btn.clicked.connect(lambda _, x=l_id: self.lesson_clicked.emit(x))
            self.lessons_layout.addWidget(btn)

        self.lessons_layout.addStretch()
