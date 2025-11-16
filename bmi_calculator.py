print("Body Mass Index Calculator")
height = float(input("enter height (m):"))
weight = int(input("enter weight (kg):"))

index = weight/(height*height)

if index <= 18.5:
    print("/n underweight BMI:" , index)
elif index >= 25.0 and index <= 29.9:
    print("/n overweight BMI:" , index)
elif index > 30:           
    print("/n obese BMI:" , index)
elif index >= 18.5 and index <=24.9:
    print("/n healthy BMI:" , index)
elif index > 30:           
    print("/n severely obese BMI:" , index)