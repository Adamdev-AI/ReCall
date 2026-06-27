from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton


class top_NavBar(QWidget):
    def __init__(self):
        super().__init__()
        # Objects
        self.home = QPushButton('Home')
        self.add = QPushButton('add')
        self.settings = QPushButton('settings')

        # Design
        main_layout = QHBoxLayout()

        main_layout.addWidget(self.home)
        main_layout.addWidget(self.add)
        main_layout.addWidget(self.settings)

        main_layout.setContentsMargins(0, 0, 0, 0)

        self.setStyleSheet("""
        QPushButton {
            border: none;
            font-size: 20px;
        } 
        QPushButton:hover {
            color: grey;
        }""")

        self.setLayout(main_layout)