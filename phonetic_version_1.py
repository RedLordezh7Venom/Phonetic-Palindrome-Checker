import phonetics
import string

def is_palindrome(s):
    s = s.lower()
    #Removing whitespaces
    s = s.replace(" ","")
    #Removing punctuators
    punctuators = set(string.punctuation)
    rect = ''.join(char for char in s if char not in punctuators)
    return rect == rect[::-1]

def is_phonetic(s):
    #Using phonetics metaphone algorithm to create phonetic key
    #Based on Lawrence Philips’ Metaphone Algorithm.
    phonetic_string = phonetics.metaphone(s)

    reversed_phonetic_string = phonetic_string[::-1]

    return phonetic_string == reversed_phonetic_string

if __name__ == "__main__":
    in_str = input("Enter string to check: ")
    if is_palindrome(in_str):
        print(f'Given string "{in_str}" is a phonetic palindrome')#if it is a palindrome, then it is a phonetic palindrome as well
    elif is_phonetic(in_str):
        print(f'Given string "{in_str}" is a phonetic palindrome')
    else:
        print(f'Given string "{in_str}" is not a phonetic palindrome')