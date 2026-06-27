from PySide6.QtWidgets import (
   QLabel,
   QVBoxLayout,
   QHBoxLayout,
   QWidget,
   QScrollArea
)
from PySide6.QtCore import Qt
import markdown

class Chat(QWidget):
    def __init__(self):
        super().__init__()
        # Objects

        # Designing
        self.main_layout = QVBoxLayout()
        self.scroll_area = QScrollArea()
        self.messages_widget = QWidget() # Contain all messages
        self.messages_layout = QVBoxLayout()

        self.messages_widget.setLayout(self.messages_layout)
        self.messages_layout.setContentsMargins(0, 0, 0, 0)
        self.messages_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_area.setWidget(self.messages_widget)
        self.scroll_area.setWidgetResizable(True)

        self.main_layout.addWidget(self.scroll_area)

        self.setStyleSheet("""
        QWidget {
            border: 1px solid white;
            border-radius: 3px;
        }
        QLabel {
            font-size: 17px;
            padding-top: 20px;
            padding-bottom: 20px;
        }
        """)

        self.setLayout(self.main_layout)
   
    def show_user_message(self, text: str):
        self.user_widget = QWidget()
        self.user_layout = QVBoxLayout()
        self.user_widget.setLayout(self.user_layout)
        self.messages_layout.addWidget(self.user_widget, alignment=Qt.AlignmentFlag.AlignRight)
        self.user_widget.setStyleSheet('''border: none''')

        self.user_message = QLabel(text, wordWrap=True, alignment=Qt.AlignmentFlag.AlignRight)
        self.user_layout.addWidget(self.user_message)
        self.user_message.setFixedWidth(1000)


    def show_ai_response(self, text: str):
        self.ai_widget = QWidget()
        self.ai_layout = QVBoxLayout()
        self.ai_widget.setLayout(self.ai_layout)
        self.messages_layout.addWidget(self.ai_widget, alignment=Qt.AlignmentFlag.AlignLeft)
        self.ai_widget.setStyleSheet('''border: none''')

        # Convert the Markdown response into HTML because QLabel does not support Markdown directly.
        markdowned = markdown.markdown(
            text,
            extensions=["fenced_code", "tables", "nl2br"]
        )

        self.ai_response = QLabel(wordWrap=True)
        self.ai_response.setFixedWidth(1000)
        self.ai_response.setTextFormat(Qt.TextFormat.RichText)  # Force QLabel to interpret the text as rich HTML instead of plain text.
        self.ai_response.setText(markdowned)  # Set the generated HTML text on the QLabel for rendering.
        self.ai_layout.addWidget(self.ai_response)