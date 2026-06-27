import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget
from PySide6.QtCore import Qt
from home_page.input_bar import InputBar
from home_page.chat import Chat
from home_page.nav_bar import top_NavBar
from Adding.main_adding_page import MainAddingPage
from settings.full_settings_page import settings_window
from PySide6.QtGui import QFont

with open('ReCallForge informations', 'a', encoding='utf-8') as f:
    f.write('')
    

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: black;')

        # Objects

        # Top navigation bar
        nav_bar = top_NavBar()

        # The chat 
        chat = Chat()

        # The input bar
        self.Input_Bar = InputBar(chat)

        # Design
        main_layout = QVBoxLayout()
        self.stacked_widget = QStackedWidget()

        # ------- Home page ----------
        home_page = QWidget()
        home_layout = QVBoxLayout()

        # The chat
        home_layout.addWidget(chat) 


        # The input bar
        home_layout.addWidget(self.Input_Bar, alignment=Qt.AlignmentFlag.AlignCenter)
        home_layout.addSpacing(10)

        home_page.setLayout(home_layout)

        # ------- Adding page ----------
        adding_page = MainAddingPage()

        # ------- Settings page ----------
        settings_page = settings_window()

        main_layout.addWidget(nav_bar)

        self.stacked_widget.addWidget(home_page) # Index 0
        self.stacked_widget.addWidget(adding_page) # Index 1
        self.stacked_widget.addWidget(settings_page) # Index 2

        nav_bar.home.clicked.connect(self.showing_home_page)
        nav_bar.add.clicked.connect(self.showing_add_page)
        nav_bar.settings.clicked.connect(self.showing_settings_page)

        main_layout.addWidget(self.stacked_widget)

        self.setLayout(main_layout)

    def showing_home_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def showing_add_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def showing_settings_page(self):
        self.stacked_widget.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 11))
    window = MainWindow()

    window.show()
    app.exec()