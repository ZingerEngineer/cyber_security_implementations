import string
import sys

ascii_lowercase = string.ascii_lowercase
ascii_uppercase = string.ascii_uppercase
ascii_whitespace = string.whitespace
alphabet = ascii_whitespace + ascii_lowercase + ascii_uppercase

def caeserEncrypt(text,shift=3):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            encrypted_text += alphabet[(char_index + shift) % len(alphabet)]
        else:
            encrypted_text += char
    return encrypted_text

sys.modules[__name__] = caeserEncrypt