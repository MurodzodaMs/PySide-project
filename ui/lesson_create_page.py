from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, 
    QLabel, QLineEdit, QPushButton
) 
from PySide6.QtCore import Signal

class LessonCreateWindow(QWidget):
    lesson_created = Signal(name='lesson_created')

    def __init__(self):
        super().__init__()
        # self.setWindowTitle('Create Lesson')
        # self.resize(400,500)

        
        self.title = QLabel('<H1>Create Lesson')
        
        self.label = QLabel('Title')
        self.line = QLineEdit(placeholderText='Enter title')
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line)

        self.button = QPushButton('create')
        self.back_button = QPushButton('Back')

        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title)
        main_layout.addSpacing(15)
        main_layout.addLayout(layout)
        main_layout.addWidget(self.button)
        main_layout.addStretch()
        main_layout.addWidget(self.back_button)

        self.setLayout(main_layout)
        
    

        
        
        