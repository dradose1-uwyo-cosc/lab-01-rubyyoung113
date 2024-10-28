# Ruby Young 
# UWYO COSC 1010
# Submission Date: 10/29/24
# HW 02
# Lab Section: 16
# Sources, people worked with, help given to: Nile Young 

# For this homework assignment you will be writing a program that translates between plaintext and Morse Code.

# When your program first starts it should ask the user for the input string. If plaintext alphabet cahracters is entered output the Morse Code equivalent.

#You may assume that only alphabet characters will be entered, and may ignore other input characters.

#You can use the equivalencies below.





morse_dict = { 
'A': '.-',      'N': '-.',
'B': '-...',    'O': '---', 
'C': '-.-.',    'P': '.--.',
'D': '-..',     'Q': '--.-',
'E': '.',       'R': '.-.',
'F': '..-.',    'S': '...',
'G': '--.',     'T': '-',
'H': '....',    'U': '..-',
'I': '..',      'V': '...-',
'J': '.---',    'W': '.--',
'K': '-.-',     'X': '-..-',
'L': '.-..',    'Y': '-.--',
'M': '--',      'Z': '--..',
}

question = input("Input a string: ")


my_string = ""

for character in question:
    if character == ' ':
        my_string += '  '
    elif character.isalpha():
        my_string += morse_dict[character.upper()] + ' '


print(my_string)
