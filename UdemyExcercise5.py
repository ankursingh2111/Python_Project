temperatures=[10,-20,-289,100]
def celtofah(temperatures):
    with open("CelToFah.txt","w") as file:
        for temp in temperatures:
            if temp>(-273.15):
                cel=str((9/5)*temp+32)
                file.write(cel)
                file.write("\n")
celtofah(temperatures)
