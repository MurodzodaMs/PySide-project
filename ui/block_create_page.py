from PySide6.QtWidgets import (
    QWidget, QPushButton, QLabel, QLineEdit,
    QVBoxLayout, QHBoxLayout, QTextEdit,
    QComboBox
)


class BlockWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.type_label = QLabel('Type')
        self.comment_label = QLabel('Text')
        self.media_label = QLabel('Media')
        self.url_label = QLabel('Url')

        self.type_line = QComboBox()
        self.type_line.addItems(
            ['p', 'h1', 'h2', 'h3', 'h4', 'h5',
             'h6', 'strong', 'url', 'media', 'i']
        )
        self.comment_line = QTextEdit(placeholderText='Enter Text')

        self.media_line = QLineEdit(placeholderText='Select Image')
        self.media_line.setReadOnly(True)
        self.browse_button = QPushButton('Browse')

        self.url_line = QLineEdit(placeholderText='Enter Url')

        self.button = QPushButton('click')
        self.back_button = QPushButton('Back')

        self.main_layout = QVBoxLayout()

        # Type Row
        self.type_layout = QHBoxLayout()
        self.type_layout.addWidget(self.type_label)
        self.type_layout.addWidget(self.type_line)
        self.main_layout.addLayout(self.type_layout)

        # Media Row (Hidden by default)
        self.media_widget = QWidget()
        self.media_row = QHBoxLayout(self.media_widget)
        self.media_row.setContentsMargins(0, 0, 0, 0)
        self.media_row.addWidget(self.media_label)
        self.media_row.addWidget(self.media_line)
        self.media_row.addWidget(self.browse_button)
        self.main_layout.addWidget(self.media_widget)
        self.media_widget.hide()

        # URL Row (Hidden by default)
        self.url_widget = QWidget()
        self.url_row = QHBoxLayout(self.url_widget)
        self.url_row.setContentsMargins(0, 0, 0, 0)
        self.url_row.addWidget(self.url_label)
        self.url_row.addWidget(self.url_line)
        self.main_layout.addWidget(self.url_widget)
        self.url_widget.hide()

        # Comment Row
        self.comment_layout = QHBoxLayout()
        self.comment_layout.addWidget(self.comment_label)
        self.comment_layout.addWidget(self.comment_line)
        self.main_layout.addLayout(self.comment_layout)

        self.main_layout.addStretch()

        # Buttons Row
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.button)
        self.button_layout.addWidget(self.back_button)
        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)

    def get_lesson_id(self, lesson_id):
        self.lesson_id = lesson_id

    def show_media(self):
        self.media_widget.show()
        self.url_widget.hide()

    def show_url(self):
        self.url_widget.show()
        self.media_widget.hide()

    def show_default(self):
        self.media_widget.hide()
        self.url_widget.hide()
