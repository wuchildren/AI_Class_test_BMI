"""
BMI (Body Mass Index) Calculator
Calculates BMI using metric or imperial units and categorizes the result.
"""

def get_positive_float(prompt: str) -> float:
    """Prompt the user for a positive floating point number with error handling."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")

def calculate_bmi_metric(weight_kg: float, height_cm: float) -> float:
    """Calculate BMI using metric units (kg and cm)."""
    height_m = height_cm / 100.0
    return weight_kg / (height_m ** 2)

def calculate_bmi_imperial(weight_lbs: float, height_inches: float) -> float:
    """Calculate BMI using imperial units (lbs and inches)."""
    return (weight_lbs / (height_inches ** 2)) * 703

def get_bmi_category(bmi: float) -> tuple[str, str]:
    """Return BMI category and recommendation based on WHO standards."""
    if bmi < 18.5:
        return "Underweight", "Consider consulting a healthcare provider or nutritionist for advice on healthy weight gain."
    elif 18.5 <= bmi < 25.0:
        return "Normal weight", "Great job! Maintain a balanced diet and regular exercise to stay healthy."
    elif 25.0 <= bmi < 30.0:
        return "Overweight", "Consider regular physical activity and adopting balanced eating habits."
    elif 30.0 <= bmi < 35.0:
        return "Obese (Class 1)", "It is recommended to consult a doctor or nutritionist for guidance."
    elif 35.0 <= bmi < 40.0:
        return "Obese (Class 2)", "High health risk. Please consult a healthcare professional."
    else:
        return "Obese (Class 3 / Severe)", "Very high health risk. Seeking professional medical support is strongly advised."

def calculate_healthy_weight_range(height_cm: float) -> tuple[float, float]:
    """Calculate healthy weight range (BMI 18.5 to 24.9) in kg for a given height in cm."""
    height_m = height_cm / 100.0
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 24.9 * (height_m ** 2)
    return min_weight, max_weight

def run_calculator():
    print("=" * 45)
    print("        WELCOME TO BMI CALCULATOR")
    print("=" * 45)

    while True:
        print("\nChoose your measurement system:")
        print("1. Metric (Kilograms & Centimeters)")
        print("2. Imperial (Pounds & Inches)")
        print("3. Exit")

        choice = input("\nEnter choice (1/2/3): ").strip()

        if choice == "1":
            print("\n--- Metric System ---")
            weight = get_positive_float("Enter your weight in kg (e.g., 70): ")
            height = get_positive_float("Enter your height in cm (e.g., 175): ")
            bmi = calculate_bmi_metric(weight, height)
            min_w, max_w = calculate_healthy_weight_range(height)
            height_cm = height
            weight_unit = "kg"
        elif choice == "2":
            print("\n--- Imperial System ---")
            weight = get_positive_float("Enter your weight in lbs (e.g., 154): ")
            height = get_positive_float("Enter your height in inches (e.g., 69): ")
            bmi = calculate_bmi_imperial(weight, height)
            height_cm = height * 2.54
            min_w, max_w = calculate_healthy_weight_range(height_cm)
            # convert healthy range to lbs for display
            min_w_lbs = min_w * 2.20462
            max_w_lbs = max_w * 2.20462
            weight_unit = "lbs"
        elif choice == "3":
            print("\nThank you for using the BMI Calculator. Stay healthy!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        category, recommendation = get_bmi_category(bmi)

        print("\n" + "-" * 45)
        print("                 RESULTS")
        print("-" * 45)
        print(f"Your BMI:         {bmi:.2f}")
        print(f"Category:         {category}")
        if choice == "1":
            print(f"Healthy Weight:   {min_w:.1f} kg - {max_w:.1f} kg")
        else:
            print(f"Healthy Weight:   {min_w_lbs:.1f} lbs - {max_w_lbs:.1f} lbs")
        print(f"Recommendation:   {recommendation}")
        print("-" * 45)

        again = input("\nWould you like to calculate another BMI? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThank you for using the BMI Calculator. Goodbye!")
            break

if __name__ == "__main__":
    run_calculator()
