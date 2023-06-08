import sys
import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

class SenderWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle("Sender")

        self.message_textbox = QTextEdit(self)
        self.encrypt_button = QPushButton("Encrypt and Send", self)
        self.encrypt_button.clicked.connect(self.encrypt_message)

        central_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Type your message below:"))
        main_layout.addWidget(self.message_textbox)
        main_layout.addWidget(self.encrypt_button)
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

    def encrypt_message(self):
        key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC)

        message = self.message_textbox.toPlainText()
        message = message.encode()

        # padding message to 16 bytes boundary
        length = 16 - (len(message) % 16)
        message += bytes([length]) * length

        ciphertext = cipher.encrypt(message)
        iv = b64encode(cipher.iv).decode('utf-8')
        ciphertext = b64encode(ciphertext).decode('utf-8')

        receiver_window = ReceiverWindow(iv, ciphertext, key)
        receiver_window.show()


class ReceiverWindow(QMainWindow):
    def __init__(self, iv, ciphertext, key):
        super().__init__()

        self.setGeometry(600, 100, 500, 300)
        self.setWindowTitle("Receiver")

        self.encrypted_message_label = QLabel("Encrypted Message:", self)
        self.encrypted_message_textbox = QTextEdit(self)
        self.encrypted_message_textbox.setReadOnly(True)
        self.encrypted_message_textbox.setText(ciphertext)

        self.decrypted_message_label = QLabel("Decrypted Message:", self)
        self.decrypted_message_textbox = QTextEdit(self)
        self.decrypted_message_textbox.setReadOnly(True)

        decrypt_button = QPushButton("Decrypt", self)
        decrypt_button.clicked.connect(lambda: self.decrypt_message(iv, ciphertext, key))

        central_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.encrypted_message_label)
        main_layout.addWidget(self.encrypted_message_textbox)
        main_layout.addWidget(decrypt_button)
        main_layout.addWidget(self.decrypted_message_label)
        main_layout.addWidget(self.decrypted_message_textbox)
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

    def decrypt_message(self, iv, ciphertext, key):
        cipher = AES.new(key, AES.MODE_CBC, b64decode(iv))

        ciphertext = b64decode(ciphertext)

        message = cipher.decrypt(ciphertext)

        # remove padding
        pad_len = message[-1]
        message = message[:-pad_len]

        self.decrypted_message_textbox.setText(message.decode('utf-8'))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    sender_window = SenderWindow()
    sender_window.show()

    sys.exit(app.exec())
