import re
def count_occurance(filename,regex):
    count=0
    with open(filename, "r") as file:
        for line in file:
            if re.search(regex,line):
                count=count+1
    print("mbox.txt had" , count, " lines that matched ", regex)

filen=input("Enter file name: ")
rege=input("Enter the regext be searched: ")

#count_occurance(filen,rege)

def average_line(filename):
    count=0
    num=[]
    num1=0
    with open(filename, "r") as file:
        for line in file:
            if re.search('New Revision: ([0-9]+)',line):
                num = re.findall('New Revision: ([0-9]+)',line)
                for item in num:
                    num1=num1+float(item)
                count+=1
    print("Average:", num1/count)

average_line(filen)
