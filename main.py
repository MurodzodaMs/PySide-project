import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainScreen
from controllers.main_controller import MainController
from style import Style

def main():
    app = QApplication(sys.argv)

    app.setStyleSheet(Style.set_style(app))

    window = MainScreen()
    controller = MainController(window)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()





# import sys
# from PySide6.QtWidgets import QApplication
# from ui.block_window import BlockWindow



# app = QApplication(sys.argv)
# window = BlockWindow()
# window.show()
# app.exec()
