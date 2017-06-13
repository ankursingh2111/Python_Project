def ConvertTemp(C_degree):
    temp_fhnt=(9*C_degree/5)+32
    return temp_fhnt

c_temp=float(input("Please enter the temperature in Celsius: "))
if c_temp > (-273.15):
    print("Temperature in Fahrenheit is: ", ConvertTemp(c_temp))
else:
    print("Temperature cannot be less than -273.15")

money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
print(money["under_bed"][1])

temperatures=[10,-20,-289,100]
for temp in temperatures:
     if temp> (-273.15):
         print("Temperature in Fahrenheit is: ", ConvertTemp(temp))
     else:
         print("Temperature cannot be less than -273.15")
