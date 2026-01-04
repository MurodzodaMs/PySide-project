from PySide6.QtWidgets import QApplication

class Style:

    @staticmethod
    def set_style( app: QApplication):
        return """
QLabel{
    font-size: 14px;
    font-weight: 600;
    margin-left: 15px;
    margin-right: 15px;
}
QPushButton {
    background-color: #2d2d2d;
    border: 1px solid #444;
    border-radius: 6px;
    padding: 6px 10px;
    font-size: 14px;
    font-weight: 600;
}
QPushButton:hover {
    background-color: #3d3d3d;
}

QLineEdit, QTextEdit {
    background-color: #252525;
    border: 1px solid #444;
    border-radius: 5px;
    padding: 5px;
}

QTextEdit{
    height: 50px;
}
"""