height = float(input("Enter your height in inches:"))
weight = float(input("Enter your weight in lbs: "))

def BMI (height, weight):
  bmi = weight / (height ** 2) * 703

  if (bmi < 16):
    return "Severely underweight", bmi
  elif (bmi >= 16 and bmi < 18.5):
    return "Underweight", bmi
  elif (bmi >= 18.5 and bmi < 25):
    return "healthy", bmi
  elif(bmi >= 25 and bmi < 30):
    return "Overweight", bmi
  elif(bmi >= 30):
    return "Obesse", bmi

quote, bmi = BMI(height = height, weight= weight)
print (f"Your bmi is: {bmi} and you are: {quote}")


