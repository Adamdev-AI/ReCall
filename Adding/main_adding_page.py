from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from Adding.qoutes import random_qoute
from PySide6.QtCore import Qt
from Adding.adding_widget import adding_widget

class MainAddingPage(QWidget):
    def __init__(self):
        super().__init__()

        # Objects
        self.hero_text = QLabel(random_qoute())
        self.adding_place = adding_widget()

        # Designing
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.addStretch(3)
        self.main_layout.addWidget(self.hero_text, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addStretch(20)
        self.main_layout.addWidget(self.adding_place, alignment=Qt.AlignmentFlag.AlignTop)
        self.main_layout.addStretch(40)


        self.hero_text.setStyleSheet(
            """
                font-size: 30px
            """
        )

        self.setLayout(self.main_layout)