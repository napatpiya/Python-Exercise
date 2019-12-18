print("")
print("Calculate your BMI to find whether you are too skinny or too fat")
print("Just put your weight and height")
w = float(input("Weight(kg.): "))
h = float(input("Height(cm.): "))
bmi = w / ((h/100) ** 2)
print("")
print("Your BMI is", bmi)
print("")
if bmi >= 18.5 and bmi <= 25 :
    print("Your body is perfect!!")
elif bmi < 18.5 :
    print("Oh....you are too skinny T^T ") 
else :
    print("Ummm you are too chubby =_='") 
print("")