import sys
import caeser_decrypt as cd

def bruteForceDecrypt(text):
    decryptedStatementsArray = []
    for shift in range(26):
      decrypted_text = cd(text,shift)
      decryptedStatementsArray.append(decrypted_text)
    return decryptedStatementsArray

sys.modules[__name__] = bruteForceDecrypt