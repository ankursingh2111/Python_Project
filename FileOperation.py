import string
count=0
sum=0.0
filename=input("Enter the filename: ")
file=open(filename)

for line in file:
    if line.startswith("X-DSPAM-Confidence"):
        count+=1
        list=line.split(":")
        list[1]=float(list[1].strip())
        sum=sum+list[1]

print("Average spam confidence:", sum/count)
