from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QScrollArea
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal, Qt


class LessonUpdateWindow(QWidget):
    add_block_signal = Signal(int)
    delete_lesson_signal = Signal()
    delete_block_signal = Signal(int)
    update_block_signal = Signal(int)

    def __init__(self):
        super().__init__()
        # self.setWindowTitle('Block List')
        # self.resize(500, 300)

        self.lesson_id = 0
        self.title = QLabel('<h2>Lesson</h2>')
        self.back_button = QPushButton('Back')

        self.block_list = QScrollArea()
        self.block_list.setWidgetResizable(True)
        self.container = QWidget()
        self.block_layout = QVBoxLayout(self.container)
        self.block_list.setWidget(self.container)

        buttons = QHBoxLayout()
        buttons.addWidget(self.back_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title)
        main_layout.addSpacing(15)
        main_layout.addWidget(self.block_list)
        main_layout.addLayout(buttons)

        self.setLayout(main_layout)

    def show_blocks(self, blocks: list):
        self.clear_layout(self.block_layout)

        for block in blocks:
            s1, s2 = '', ''
            match block[1]:
                case 'h1': s1 = '<h1>'; s2 = '</h1>'
                case 'h2': s1 = '<h2>'; s2 = '</h2>'
                case 'h3': s1 = '<h3>'; s2 = '</h3>'
                case 'h4': s1 = '<h4>'; s2 = '</h4>'
                case 'h5': s1 = '<h5>'; s2 = '</h5>'
                case 'h6': s1 = '<h6>'; s2 = '</h6>'
                case 'p': s1 = '<p>'; s2 = '</p>'
                case 'strong': s1 = '<strong>'; s2 = '</strong>'
                case 'i': s1 = '<i>'; s2 = '</i>'
                case 'url':
                    ready_block = QLabel(
                        f'<a href="{block[4]}">{block[2]}</a>')
                    ready_block.setWordWrap(True)
                    ready_block.setOpenExternalLinks(True)
                    self.block_layout.addWidget(ready_block)

                    self.add_command_buttons(block[0])
                    continue
                case 'media':
                    pixmap = QPixmap(block[3])
                    if not pixmap.isNull():
                        pixmap = pixmap.scaledToWidth(
                            400, Qt.TransformationMode.SmoothTransformation)
                        img_label = QLabel()
                        img_label.setPixmap(pixmap)
                        self.block_layout.addWidget(img_label)

                    if block[2]:
                        caption = QLabel(block[2])
                        caption.setStyleSheet(
                            "color: gray; font-style: italic;")
                        self.block_layout.addWidget(caption)

                    self.add_command_buttons(block[0])
                    continue
                case _: s1 = '<p>'; s2 = '</p>'

            ready_block = QLabel(str(s1+block[2]+s2))
            ready_block.setWordWrap(True)
            self.block_layout.addWidget(ready_block)

            self.add_command_buttons(block[0])

        self.block_layout.addStretch()

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())
                item.layout().deleteLater()

    def add_command_buttons(self, block_id):
        buttons_layout = QHBoxLayout()

        update_btn = QPushButton('Update')
        delete_btn = QPushButton('Delete')

        buttons_layout.addWidget(update_btn)
        buttons_layout.addWidget(delete_btn)
        buttons_layout.addStretch()

        delete_btn.clicked.connect(
            lambda _, x=block_id: self.delete_block_signal.emit(x)
        )
        update_btn.clicked.connect(
            lambda _, x=block_id: self.update_block_signal.emit(x)
        )

        self.block_layout.addLayout(buttons_layout)
        self.block_layout.addSpacing(10)

    def give_block(self, block):
        pass

    def send_add_block_signal(self):
        self.add_block_signal.emit(self.lesson_id)

    def send_delete_lesson_signal(self):
        self.delete_lesson_signal.emit()
