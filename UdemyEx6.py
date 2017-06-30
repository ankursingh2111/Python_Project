import datetime
file1=["Sample-Files/file1.txt","Sample-Files/file2.txt","Sample-Files/file3.txt"]

def writefile():

    with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"), "w") as filename:
        for filename1 in file1:
            fh=open(filename1,"r")
            for line in fh:
                filename.write(line)
                filename.write("\n")
            fh.close()

writefile()
