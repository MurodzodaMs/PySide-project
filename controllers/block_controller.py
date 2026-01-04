from PySide6.QtWidgets import QMessageBox, QFileDialog
from db import create_block
from ui.block_create_page import BlockWindow
import shutil
import os


class BlockController:
    def __init__(self, view: BlockWindow):
        self.view = view
        self.view.type_line.currentTextChanged.connect(self.change_type)
        self.view.button.clicked.connect(self.on_click)
        self.view.browse_button.clicked.connect(self.open_file_dialog)

    def change_type(self, current_type):
        if current_type == 'media':
            self.view.show_media()
        elif current_type == 'url':
            self.view.show_url()
        else:
            self.view.show_default()

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self.view,
            "Select Image",
            "",
            "Images (*.png *.xpm *.jpg *.jpeg *.bmp)"
        )
        if file_name:
            if not os.path.exists('media'):
                os.makedirs('media')

            # Extract filename and create destination path
            base_name = os.path.basename(file_name)
            destination = os.path.join('media', base_name)

            # Copy file
            try:
                shutil.copy(file_name, destination)
                self.view.media_line.setText(destination)
            except Exception as e:
                QMessageBox.critical(self.view, "Error",
                                     f"Failed to copy file: {str(e)}")

    def on_click(self):
        block_type = self.view.type_line.currentText()
        comment = self.view.comment_line.toPlainText()
        media = self.view.media_line.text()
        url = self.view.url_line.text()
        lesson_id = self.view.lesson_id

        create_block(
            block_type=block_type,
            comment=comment,
            media_url=media,
            url=url,
            lesson=lesson_id
        )
        QMessageBox.information(self.view, 'Success',
                                'Block was added successfully'
                                )


        self.view.comment_line.clear()
        self.view.media_line.clear()
        self.view.url_line.clear()
