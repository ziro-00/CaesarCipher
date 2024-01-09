import tkinter as tk
from art import art
from cipher import encrypt, decrypt, bruteforce

def encrypt_decrypt():
    plaintext = entry.get()

    try:
        shift = int(shift_entry.get())
    except ValueError:
        result_label.config(text="Invalid. Please enter an integer.")
        return

    encrypted_text = encrypt(plaintext, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    result_label.config(text=f'\nPlaintext: {plaintext}\nEncrypted: {encrypted_text}\nDecrypted: {decrypted_text}')


def on_bruteforce():
    plaintext = entry.get()
    result = bruteforce(plaintext)

    if not any(result.values()):
        result_label.config(text="Invalid. Please check your input.")
        return

    result_label.config(text="")

    for shift, text in result.items():
        result_label.config(text=result_label.cget("text") + f'Shift {shift}: {text}\n')


window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("1250x850")
window.configure(bg="black")

art
ascii_label = tk.Label(window, text=art, fg="white", bg="black", font=("Courier", 10))
ascii_label.pack()

label = tk.Label(window, text="Enter a phrase:", fg="white", bg="black")
label.pack()

entry = tk.Entry(window, fg="white", bg="black")
entry.pack()

tk.Label(window, text="", bg="black").pack()

shift_label = tk.Label(window, text="Enter the shift amount:", fg="white", bg="black")
shift_label.pack()

shift_entry = tk.Entry(window, fg="white", bg="black")
shift_entry.pack()

tk.Label(window, text="", bg="black").pack()

button_encrypt_decrypt = tk.Button(window, text="Encrypt/Decrypt", command=encrypt_decrypt, fg="white", bg="black")
button_encrypt_decrypt.pack()

tk.Label(window, text="", bg="black").pack()

button_bruteforce = tk.Button(window, text="Bruteforce", command=on_bruteforce, fg="white", bg="black")
button_bruteforce.pack()

result_label = tk.Label(window, fg="white", bg="black", justify="left")
result_label.pack()

window.mainloop()