import sys
import string

ascii_lowercase = string.ascii_lowercase
ascii_uppercase = string.ascii_uppercase
ascii_whitespace = string.whitespace
alphabet = ascii_whitespace + ascii_lowercase + ascii_uppercase

def caeserDecrypt(text,shift=3):
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            decrypted_text += alphabet[(char_index - shift) % len(alphabet)]
        else:
            decrypted_text += char
    return decrypted_text


sys.modules[__name__] = caeserDecrypt