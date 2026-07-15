Weight = float(input("Yours Weight in kg:"))
Height = float(input("Yours height in meter:"))
BMI = Weight/(Height*Height)
print("BMI:", BMI)
if BMI<18.5:
    print("Underwieght")
elif 18.5 <=BMI<=24.9:
    print("Normal")
elif 25 <=BMI<29.9:
    print("Overweight")
else :
    print("Obese")