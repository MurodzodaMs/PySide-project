from PySide6.QtWidgets import QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle('Main')
        # self.resize(600, 400)


        self.title = QLabel('<h1>Main Page')
        self.create_lesson = QPushButton('Create Lesson')

        buttons = QHBoxLayout()
        buttons.addWidget(self.create_lesson)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title)
        main_layout.addSpacing(15)
        main_layout.addLayout(buttons)
        main_layout.addStretch()

        self.setLayout(main_layout)