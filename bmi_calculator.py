"""
Bilingual BMI (Body Mass Index) Calculator / 雙語 BMI 身體質量指數計算機
Supports English and Traditional Chinese (zh-TW).
"""

import sys

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

TRANSLATIONS = {
    "en": {
        "title": "WELCOME TO BMI CALCULATOR",
        "menu_system": "\nChoose your measurement system:",
        "option_metric": "1. Metric (Kilograms & Centimeters)",
        "option_imperial": "2. Imperial (Pounds & Inches)",
        "option_switch_lang": "3. Switch Language / 切換語言",
        "option_exit": "4. Exit",
        "enter_choice": "Enter choice (1/2/3/4): ",
        "invalid_choice": "Invalid choice. Please select 1, 2, 3, or 4.",
        "metric_header": "\n--- Metric System ---",
        "imperial_header": "\n--- Imperial System ---",
        "prompt_weight_kg": "Enter your weight in kg (e.g., 70): ",
        "prompt_height_cm": "Enter your height in cm (e.g., 175): ",
        "prompt_weight_lbs": "Enter your weight in lbs (e.g., 154): ",
        "prompt_height_in": "Enter your height in inches (e.g., 69): ",
        "err_positive": "Please enter a number greater than 0.",
        "err_invalid_num": "Invalid input. Please enter a valid numerical value.",
        "results_header": "RESULTS",
        "label_bmi": "Your BMI:        ",
        "label_category": "Category:        ",
        "label_healthy_weight": "Healthy Weight:  ",
        "label_recommendation": "Recommendation:  ",
        "calc_again": "\nWould you like to calculate another BMI? (y/n): ",
        "goodbye": "\nThank you for using the BMI Calculator. Stay healthy! Goodbye!",
        "categories": {
            "underweight": ("Underweight", "Consider consulting a healthcare provider or nutritionist for advice on healthy weight gain."),
            "normal": ("Normal weight", "Great job! Maintain a balanced diet and regular exercise to stay healthy."),
            "overweight": ("Overweight", "Consider regular physical activity and adopting balanced eating habits."),
            "obese_1": ("Obese (Class 1)", "It is recommended to consult a doctor or nutritionist for guidance."),
            "obese_2": ("Obese (Class 2)", "High health risk. Please consult a healthcare professional."),
            "obese_3": ("Obese (Class 3 / Severe)", "Very high health risk. Seeking professional medical support is strongly advised.")
        }
    },
    "zh-tw": {
        "title": "歡迎使用 BMI 身體質量指數計算機",
        "menu_system": "\n請選擇測量單位系統：",
        "option_metric": "1. 公制 Metric（公斤 & 公分）",
        "option_imperial": "2. 英制 Imperial（磅 & 英吋）",
        "option_switch_lang": "3. 切換語言 / Switch Language",
        "option_exit": "4. 退出程式",
        "enter_choice": "請輸入選項 (1/2/3/4): ",
        "invalid_choice": "無效的選項，請選擇 1、2、3 或 4。",
        "metric_header": "\n--- 公制系統 ---",
        "imperial_header": "\n--- 英制系統 ---",
        "prompt_weight_kg": "請輸入體重（公斤 kg，例如：70）: ",
        "prompt_height_cm": "請輸入身高（公分 cm，例如：175）: ",
        "prompt_weight_lbs": "請輸入體重（磅 lbs，例如：154）: ",
        "prompt_height_in": "請輸入身高（英吋 inches，例如：69）: ",
        "err_positive": "請輸入大於 0 的數值。",
        "err_invalid_num": "輸入格式錯誤，請輸入有效的數字。",
        "results_header": "計算結果",
        "label_bmi": "您的 BMI 指數:    ",
        "label_category": "體重判定:        ",
        "label_healthy_weight": "理想健康體重:    ",
        "label_recommendation": "健康建議:        ",
        "calc_again": "\n是否要再次計算 BMI？(y/n): ",
        "goodbye": "\n感謝使用 BMI 計算機，祝您身體健康！再見！",
        "categories": {
            "underweight": ("體重過輕 (Underweight)", "建議諮詢醫師或營養師，以健康的方式適度增加體重與營養吸收。"),
            "normal": ("正常範圍 (Normal weight)", "太棒了！請繼續保持均衡飲食與規律運動的生活習慣。"),
            "overweight": ("體重過重 (Overweight)", "建議增加日常體能活動量，並適當調整飲食結構。"),
            "obese_1": ("輕度肥胖 (Obese Class 1)", "建議尋求專業醫師或營養師協助，規劃體重控制計畫。"),
            "obese_2": ("中度肥胖 (Obese Class 2)", "健康風險較高，強烈建議諮詢醫療專業人員進行健康管理。"),
            "obese_3": ("重度肥胖 (Obese Class 3)", "健康風險極高，請務必尋求專業醫療團隊的診斷與協助。")
        }
    }
}


def get_positive_float(prompt: str, err_positive: str, err_invalid: str) -> float:
    """Prompt the user for a positive floating point number with error handling."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print(err_positive)
                continue
            return value
        except ValueError:
            print(err_invalid)


def calculate_bmi_metric(weight_kg: float, height_cm: float) -> float:
    """Calculate BMI using metric units (kg and cm)."""
    height_m = height_cm / 100.0
    return weight_kg / (height_m ** 2)


def calculate_bmi_imperial(weight_lbs: float, height_inches: float) -> float:
    """Calculate BMI using imperial units (lbs and inches)."""
    return (weight_lbs / (height_inches ** 2)) * 703


def get_bmi_category(bmi: float, lang: str = "en") -> tuple[str, str]:
    """Return BMI category and recommendation based on WHO standards in selected language."""
    categories = TRANSLATIONS[lang]["categories"]
    if bmi < 18.5:
        return categories["underweight"]
    elif 18.5 <= bmi < 25.0:
        return categories["normal"]
    elif 25.0 <= bmi < 30.0:
        return categories["overweight"]
    elif 30.0 <= bmi < 35.0:
        return categories["obese_1"]
    elif 35.0 <= bmi < 40.0:
        return categories["obese_2"]
    else:
        return categories["obese_3"]


def calculate_healthy_weight_range(height_cm: float) -> tuple[float, float]:
    """Calculate healthy weight range (BMI 18.5 to 24.9) in kg for a given height in cm."""
    height_m = height_cm / 100.0
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 24.9 * (height_m ** 2)
    return min_weight, max_weight


def select_language() -> str:
    """Interactive language selection."""
    while True:
        print("\nPlease select your language / 請選擇語言:")
        print("1. English (英文)")
        print("2. 繁體中文 (Traditional Chinese - zh-TW)")
        choice = input("Enter choice / 請選擇 (1/2): ").strip()
        if choice == "1":
            return "en"
        elif choice == "2":
            return "zh-tw"
        print("Invalid selection / 選項無效，請輸入 1 或 2。")


def run_calculator():
    lang = select_language()

    while True:
        t = TRANSLATIONS[lang]
        line_len = 50
        print("\n" + "=" * line_len)
        print(f" {t['title']:^{line_len - 2}}")
        print("=" * line_len)

        print(t["menu_system"])
        print(t["option_metric"])
        print(t["option_imperial"])
        print(t["option_switch_lang"])
        print(t["option_exit"])

        choice = input("\n" + t["enter_choice"]).strip()

        if choice == "1":
            print(t["metric_header"])
            weight = get_positive_float(t["prompt_weight_kg"], t["err_positive"], t["err_invalid_num"])
            height = get_positive_float(t["prompt_height_cm"], t["err_positive"], t["err_invalid_num"])
            bmi = calculate_bmi_metric(weight, height)
            min_w, max_w = calculate_healthy_weight_range(height)
            weight_display = f"{min_w:.1f} kg - {max_w:.1f} kg"

        elif choice == "2":
            print(t["imperial_header"])
            weight = get_positive_float(t["prompt_weight_lbs"], t["err_positive"], t["err_invalid_num"])
            height = get_positive_float(t["prompt_height_in"], t["err_positive"], t["err_invalid_num"])
            bmi = calculate_bmi_imperial(weight, height)
            height_cm = height * 2.54
            min_w, max_w = calculate_healthy_weight_range(height_cm)
            min_w_lbs = min_w * 2.20462
            max_w_lbs = max_w * 2.20462
            weight_display = f"{min_w_lbs:.1f} lbs - {max_w_lbs:.1f} lbs"

        elif choice == "3":
            lang = select_language()
            continue

        elif choice == "4":
            print(t["goodbye"])
            break

        else:
            print(t["invalid_choice"])
            continue

        category, recommendation = get_bmi_category(bmi, lang)

        print("\n" + "-" * line_len)
        print(f" {t['results_header']:^{line_len - 2}}")
        print("-" * line_len)
        print(f"{t['label_bmi']}{bmi:.2f}")
        print(f"{t['label_category']}{category}")
        print(f"{t['label_healthy_weight']}{weight_display}")
        print(f"{t['label_recommendation']}{recommendation}")
        print("-" * line_len)

        again = input(t["calc_again"]).strip().lower()
        if again not in ('y', 'yes', '是'):
            print(t["goodbye"])
            break


if __name__ == "__main__":
    run_calculator()
