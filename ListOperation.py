def fileread():
    list=[]
    filename=input("Enter the filename: ")
    filehandle=open(filename)
    for line in filehandle:
        list1=line.split()
        for item in list1:
            if not item in list:
                list.append(item)

    list.sort()
    print(list)
#fileread()

def fromfirst():
    list=[]
    count=0
    filename=input("Enter the filename: ")
    filehandle=open(filename)
    for line in filehandle:
        if line.startswith("From"):
            count=count+1
            list1=line.split()
            print(list1[1])
    print("There were" ,count, "lines in the file with From as the first word")

fromfirst()
