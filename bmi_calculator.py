##--BMI CALCULATOR--
while True:
	print(" ---Welcome to BMI calculator---")

	name = input("Enter your Name : ")
	age = int(input("Enter your age :"))
	gender = input("Enter your Gender :") 
	weight = int(input("Enter your weight(in kg) : "))
	height = float(input("Enter your Height(in cm) : "))


	height_meter = height / 100
	bmi = weight/(height_meter **2)
	bmi = round(bmi,1)

	print()
	print("----------BMI REPORT----------")
	print(f"Name    : {name}")
	print(f"Age     : {age}")
	print(f"Gender  : {gender}")
	print(f"Weight  : {weight}kg")
	print(f"Height  : {height}cm")
	print(f"Your BMI is {bmi}")

	if bmi < 18.5:
		category = "Underweight"
		print(f"Category : {category}")
		print()
		print("Try eating more meals regularly.")
	elif bmi < 25:
		category = "Healthy"
		print(f"Category : {category}")
		print()
		print("Keep up your health habits.")
	elif bmi < 30:
		category = "Overweight"
		print(f"Category : {category}")
		print()
		print("Try regular exercise and healthy eating.")
	else:
		category = "Obese"
		print(f"Category : {category}")
		print()
		print("Focus on a healthier lifestyle.")

	print("-----------------------------------")
	print()

	again = input("Do you want to calculate another BMI report(yes or no)? ")

	if again.lower() == "no":
		break