print("Body Mass Index Calculator")
height = float(input("enter height (m):"))
weight = int(input("enter weight (kg):"))

index = weight/(height*height)
rounded_index = round(index,1)

if index <= 18.5:
    print("Underweight BMI:" , rounded_index )
elif index >= 25.0 and index <= 29.9:
    print("Overweight BMI:" , rounded_index)
elif index > 30:           
    print("Obese BMI:" , rounded_index )
elif index >= 18.5 and index <=24.9:
    print("Healthy BMI:" , rounded_index)
