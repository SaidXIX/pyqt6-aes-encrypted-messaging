# Secure Messaging Application

This application provides a secure messaging system where users can encrypt and send messages using the AES encryption algorithm. It consists of two windows: the Sender window for encrypting and sending messages, and the Receiver window for decrypting and viewing received messages.

## Features

- **Sender Window:** Allows users to enter messages, encrypt them using AES encryption, and send them to recipients.
- **Receiver Window:** Enables recipients to decrypt and view the received encrypted messages.
- **AES Encryption:** Utilizes the AES encryption algorithm with Cipher Block Chaining (CBC) mode for secure message encryption.
- **Padding:** Automatically applies padding to messages to ensure they are a multiple of the block size before encryption.
- **User Interface:** Built with PyQt6 to provide a user-friendly graphical interface.

## Installation

1. Clone the repository to your local machine.

2. Install the required dependencies. Ensure that you have PyQt6 and the Python Cryptography library (Crypto) installed.

3. Run the application 


## Usage

1. Launch the application.

2. In the Sender window, enter your message in the text box.

3. Click the "Encrypt and Send" button to encrypt and send the message.

4. The Receiver window will display the encrypted message.

5. Click the "Decrypt" button in the Receiver window to decrypt and view the message.

## UI
![11](https://github.com/SaidXIX/pyqt6-aes-encrypted-messaging/assets/94231271/225a5dd8-e326-44f3-900d-b3c9cab61843)


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request

## Credit
Developed by [Said Bouziani]


