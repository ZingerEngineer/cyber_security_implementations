import sys

def read_english_words(path):
   file_text = open(path, "r")
   english_words = []
   for text in file_text:
        english_words.append(text.split("\n")[0])
   file_text.close()
   return english_words

sys.modules[__name__] = read_english_words