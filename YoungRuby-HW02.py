# Ruby Young 
# UWYO COSC 1010
# Submission Date: 10/29/24
# HW 02
# Lab Section: 16
# Sources, people worked with, help given to: Nile Young, Isabella 

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
        my_string += ' '
    elif character.isalpha():
        my_string += morse_dict[character.upper()] + ' '

print(my_string)
