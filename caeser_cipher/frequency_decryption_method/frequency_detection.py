import caeser_encrypt as ce
import string
import plot_frequency as pf

def frequency_detection(cipherText):
    # Define the alphabet (only lowercase & uppercase letters are relevant)
    ascii_lowercase = string.ascii_lowercase
    ascii_uppercase = string.ascii_uppercase
    ascii_whitespace = string.whitespace
    alphabet = ascii_whitespace + ascii_lowercase + ascii_uppercase
    
    # Store frequency of only alphabetic characters
    frequency = {}
    
    for letter in cipherText:
        if letter in alphabet:  # Only count alphabetic characters
            frequency[letter] = frequency.get(letter, 0) + 1
    
    # Sort frequency in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    # Most frequent character in ciphertext
    most_frequent_char = sorted_frequency[1][0]

    # Assume most frequent character corresponds to 'e' (common in English)
    assumed_plaintext_char = 'e'
    
    # Calculate shift key (works for both uppercase & lowercase)
    cipherKey = (ord(most_frequent_char) - ord(assumed_plaintext_char)) % 26

    print(f"Most frequent character: {most_frequent_char}")
    print(f"Assumed plaintext character: {assumed_plaintext_char}")
    print(f"Detected Caesar cipher key: {cipherKey}")

    return sorted_frequency, cipherKey


if __name__ == "__main__":
  
  plainText = "Python provides multiple ways to destructure function return values, making it easy to work with tuples, lists, and dictionaries. When a function returns multiple values as a tuple, they can be unpacked into separate variables directly. Similarly, lists can be destructured in the same way, with the ability to use the * operator to capture remaining elements. For dictionaries, unpacking can be done using .values(), though direct key access is often preferred for clarity. Additionally, when dealing with lists of tuples, loop destructuring allows easy iteration over structured data. These techniques improve code readability and efficiency by eliminating unnecessary indexing and enhancing maintainability."
  
  cipherText = ce(plainText, 3)
  print('Cipher Text: ', cipherText)
  
  frequencyList, cipherKey  = frequency_detection(cipherText)
  frequencyKeys = [item[0] for item in frequencyList]
  frequencyValues = [item[1] for item in frequencyList]
  pf(frequencyKeys,frequencyValues)

  
  
  
