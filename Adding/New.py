from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class NewButton(QWidget):
    def __init__(self):
        super().__init__()

        self.button_layout = QVBoxLayout(self)
        self.new_button = QPushButton("New")

        self.button_layout.addWidget(self.new_button)