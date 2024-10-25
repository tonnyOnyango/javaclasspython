# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)  # BMI formula: weight(kg) / height(m)^2
    return bmi


# Function to interpret the BMI result
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


# Get user input for weight (kg) and height (m)
try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Print BMI result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {interpret_bmi(bmi)}")

except ValueError:
    print("Invalid input. Please enter numeric values for weight and height.")
