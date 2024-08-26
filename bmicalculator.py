def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"According to the BMI scale, you are classified as: {category}")

if __name__ == "__main__":
    main()
