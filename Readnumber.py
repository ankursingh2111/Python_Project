def printnumber():
    num=0
    count=0
    sum1=0
    while 1:
      try:
         num=input("Enter a number:")
         num1=int(num)
         count=count+1
         sum1=sum1+num1
      except:
       if num=='done':
         print("Total", sum1 ,count, sum1/count)
         break
       else:
         print("Invalid data",end='\n')


#printnumber()

def minmax():
    min=0
    max=9999
    num=0
    while 1:
      try:
         num=input("Enter a number:")
         num1=int(num)
         if min == 0 or min>num1:
            min=num1
         if max == 9999  or max<num1:
            max=num1
      except:
       if num=='done':
         print("Minimum", min, "Maximum", max)
         break
       else:
         print("Invalid data",end='\n')

minmax()
