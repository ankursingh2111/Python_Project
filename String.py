import sys,string
def reverseString():
    str=input("Enter the requierd string:")
    i=len(str)
    while(i>0):
      i=i-1
      print(str[i])

#reverseString()

def findWord(word,letter):
    count = 0
    for letter in word:
      if letter == 'a':
        count = count + 1
    print("The number of character",letter, "in", word, "is",count)

word=sys.argv[1]
letter=sys.argv[2]
print(word.count(letter))

#findWord(word,letter)

str = 'X-DSPAM-Confidence:0.8475'
index1=str.find(':')
str2=str[index1+1:]
print(float(str2))
