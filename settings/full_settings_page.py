from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class settings_window(QWidget):
    def __init__(self):
        super().__init__()

        # Objects
        self.hero_text = QLabel('Cutomize your app')

        # Designing
        self.main_layout = QVBoxLayout()

        self.hero_text.setStyleSheet('font-size: 30px; padding-top: 40px')
        self.main_layout.addWidget(self.hero_text)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        self.setLayout(self.main_layout)