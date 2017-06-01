def computegrade(grade): 
  try:
    score=float(grade)
    if score<0.1 or score>1.0:
      print("Bad Score")
  except:
    print("Bad Score")
    exit(0)
  if 1.0>=score>=0.9:
    print("A")
  elif 0.8<=score<0.9:
    print("B")
  elif 0.7<=score<0.8:
    print("C")
  elif 0.6<=score<0.7:
    print("D")
  elif score<0.6:
    print("No Grade")

computegrade(1.1)
