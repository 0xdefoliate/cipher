from cryptography.fernet import Fernet
from tkinter import messagebox, simpledialog, Tk
import pyperclip

encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

def encrypt_with_cryptography(message):
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt_with_cryptography(encrypted_message):
    decrypted_message = cipher_suite.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

def copy_to_clipboard(message):
    pyperclip.copy(message)
    messagebox.showinfo('Success', 'Message copied to clipboard!')

def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

root = Tk()

while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = encrypt_with_cryptography(message)
        messagebox.showinfo('Ciphertext of the secret message is: ', encrypted)
        copy_choice = messagebox.askyesno('Copy?', 'Do you want to copy this to clipboard?')
        if copy_choice:
            copy_to_clipboard(encrypted)
    elif task == 'decrypt':
        message = get_message()
        decrypted = decrypt_with_cryptography(message)
        messagebox.showinfo('Plaintext of the secret message is: ', decrypted)
    else:
        break
    root.mainloop

