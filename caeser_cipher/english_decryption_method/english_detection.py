#1. Read English words file -> Create an array of English words.

#2. Optain cipher text -> Brute force detect on cipher text.

#3. If English word is found -> Print the word and the key.

#4. Calculate percentage of occurence of English words in the cipher text.

import caeser_brute_force_decryption as cbfd
import caeser_encrypt as ce
import english_decryption_method.read_english_words as rew


def caeser_english_decrypt(cipherText,englishWords):
  decryptedStatementsArray = cbfd(cipherText)
  percentage = []
  for statement in decryptedStatementsArray:
    decryptedSplitWords = statement.split(" ")
    matches = 0
    for word in decryptedSplitWords:
      word = word.upper()
      if word in englishWords:
        
        matches += 1  
    percentage.append((matches/len(decryptedSplitWords))*100)
  max_percentage =  max(percentage)
  print("Max percentage: ", max_percentage, "with key: ", percentage.index(max_percentage))
      
      


if __name__ == "__main__":
  englishWords = rew('./english_words.txt')
  plainText = "Hello my name is John"
  encryptedText = ce(plainText, 3)
  caeser_english_decrypt(encryptedText, englishWords)

