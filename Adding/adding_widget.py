from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea
from PySide6.QtCore import Qt
from Adding.New import NewButton
from home_page.conversation_history import conversation_history

class adding_widget(QWidget):
    def __init__(self):
        super().__init__()

        self.conversation_history = conversation_history

        # Objects 
        self.New_Button = NewButton()
        self.has_clicked = False

        # Designing
        self.main_widget_layout = QVBoxLayout(self)
        self.main_widget_layout.insertWidget(0, self.New_Button, alignment=Qt.AlignmentFlag.AlignRight)
        self.New_Button.new_button.clicked.connect(self.when_clicked_New)

        self.adding_info = QWidget()
        self.adding_info_layout = QHBoxLayout(self.adding_info)
        self.main_widget_layout.insertWidget(1, self.adding_info)

        self.all_info = QWidget()
        self.all_info_layout = QVBoxLayout(self.all_info)
        self.all_info_layout.setSpacing(30)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedHeight(self.height())
        self.scroll_area.setStyleSheet('border: none')

        self.scroll_area.setWidget(self.all_info)
        self.main_widget_layout.insertWidget(2, self.scroll_area, alignment=Qt.AlignmentFlag.AlignTop)

        with open('ReCallForge informations', 'r', encoding='utf-8') as file:
            for line in file:   
                if line.strip():
                    cleaned_line = line.strip()
                    self.info = QLabel(cleaned_line, alignment=Qt.AlignmentFlag.AlignCenter, wordWrap=True)

                    self.all_info.setStyleSheet('border: 1px solid white; border-radius: 50px; padding-right: 15px; padding-left: 15px')
                    self.all_info_layout.addWidget(self.info)
                    self.info.setMinimumHeight(100)
                    self.info.setStyleSheet('font-size: 20px;')

    def when_clicked_New(self):

        # Objects
        if self.has_clicked:
            return
         
        self.input_text = QLineEdit()
        self.add_button = QPushButton('Add')
        self.cancel_button = QPushButton('Cancel')

        # Designing 
        
        self.adding_info_layout.addWidget(self.input_text)
        self.adding_info_layout.addWidget(self.add_button)
        self.adding_info_layout.addWidget(self.cancel_button)

        self.add_button.clicked.connect(self.add_clicked)   
        self.cancel_button.clicked.connect(self.cancel_add_info) 

        self.adding_info.show()
        
        self.has_clicked = True

    def add_clicked(self):
        self.input_bar_text = self.input_text.text() 

        if not self.input_bar_text.strip():
            return 
        
        # Objects

        line = self.input_bar_text.strip()
        self.info = QLabel(line, alignment=Qt.AlignmentFlag.AlignCenter, wordWrap=True)

        self.all_info.setStyleSheet('border: 1px solid white; border-radius: 50px; padding-right: 15px; padding-left: 15px')
        self.all_info_layout.addWidget(self.info)
        self.info.setMinimumHeight(100)
        self.info.setStyleSheet('font-size: 20px;')

        self.input_text.clear()
        self.input_text.setFocus()

        cleaned_line = ' '.join(line.split())

        # Save it in a file
        with open('ReCallForge informations', 'a', encoding='utf-8') as f:
            f.write(f'{cleaned_line}\n')

        self.conversation_history.append({'role': 'user', 'content': f'new user info: {cleaned_line}'})

    def cancel_add_info(self):
        self.adding_info.hide()

        self.input_text.deleteLater()
        self.add_button.deleteLater()
        self.cancel_button.deleteLater()

        self.has_clicked = False