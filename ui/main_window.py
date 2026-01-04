from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout
from ui.aside_page import AsideWindow

class MainScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        self.resize(900,600)
        
        self.aside = AsideWindow()
        self.stack = QStackedWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.aside, 3)
        layout.addWidget(self.stack, 7)
        self.setLayout(layout)