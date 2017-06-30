import random, string
vowel='aeiou'
consonants='bcdfghjklmnpqrstwxyz'
letter=vowel+consonants

def randomgen_text():
    letter_input1=input("Enter 'v' for vowel, 'c' for consonants, 'l' for letter: ")
    letter_input2=input("Enter 'v' for vowel, 'c' for consonants, 'l' for letter: ")
    letter_input3=input("Enter 'v' for vowel, 'c' for consonants, 'l' for letter: ")

    if letter_input1=='v':
        letter1=random.choice(vowel)
    elif letter_input1=='c':
        letter1=random.choice(consonants)
    elif letter_input1=='l':
        letter1=random.choice(letter)
    else :
        letter1=letter_input1
    if letter_input2=='v':
        letter2=random.choice(vowel)
    elif letter_input2=='c':
        letter2=random.choice(consonants)
    elif letter_input2=='l':
        letter2=random.choice(letter)
    else :
        letter2=letter_input2
    if letter_input3=='v':
        letter3=random.choice(vowel)
    elif letter_input3=='c':
        letter3=random.choice(consonants)
    elif letter_input3=='l':
        letter3=random.choice(letter)
    else :
        letter3=letter_input3
    letter_add=letter1+letter2+letter3
    return letter_add   

print(randomgen_text())
