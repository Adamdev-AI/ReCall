from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLineEdit
from PySide6.QtCore import Qt
from groq import Groq, RateLimitError, APIConnectionError
from dotenv import load_dotenv
from home_page.conversation_history import conversation_history
import json
import os

load_dotenv(dotenv_path='api.env')

groq_api_key=os.getenv('GROQ')

groq_client = Groq(api_key=groq_api_key)

class InputBar(QWidget):
    def __init__(self, chat):
        super().__init__()

        self.conversation_history = conversation_history

        # Objects

        self.chat = chat

        self.input_bar = QLineEdit()
        self.input_bar.setFixedWidth(700)
        self.input_bar.setPlaceholderText('Talk to the AI')

        send_btn = QPushButton("➤")
        send_btn.setShortcut(Qt.Key.Key_Return) # If enter key is clicked

        send_btn.clicked.connect(self.on_clicked)
        
        # Design
        main_layout = QHBoxLayout()

        self.setStyleSheet("""
        QWidget {
            border: 2px solid white;
            height: 50px;
            border-radius: 25px
        }
                           
        QPushButton {
            width: 50px;
            border-radius: 25px
        }
        QPushButton:hover {
            background-color: white;
            color: black
        }
        QLineEdit {
            padding-left: 15px;
            font-size: 15px
        }""")

        main_layout.addWidget(self.input_bar, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(send_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(main_layout)

    def on_clicked(self):
        input_bar_text = self.input_bar.text() # See the text inside the input bar
        self.input_bar.setFocus()

        if not input_bar_text.strip(): # If it empty it will return False but `not` reverse it and make it true
            return None
        
        else:

            
            self.conversation_history.append({'role': 'user', 'content': input_bar_text})
            self.chat.show_user_message(text=input_bar_text)

            try:
                completion = groq_client.chat.completions.create(
                    model="qwen/qwen3-32b",
                    messages=self.conversation_history,
                    temperature=1,
                    max_completion_tokens=4096,
                    top_p=1,
                    stream=False,
                    stop=None,
                    reasoning_format='hidden'
                )
            except RateLimitError:
                self.chat.show_user_message(text='Rate limit reached')
                return
            except APIConnectionError:
                self.chat.show_ai_response(text='Connection error')
                return


            response_message = completion.choices[0].message

            full_response = response_message.content
            
            self.conversation_history.append({'role': 'assistant', 'content': full_response})

            self.chat.show_ai_response(text=full_response)
            self.input_bar.clear()