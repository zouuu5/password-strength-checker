import re

def check_password_strength(password):
    # Criteria flags
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    digit_criteria = re.search(r"\d", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    score = sum([
        length_criteria,
        lowercase_criteria,
        uppercase_criteria,
        digit_criteria,
        special_char_criteria
    ])

    # Strength classification
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Feedback
    print("\nPassword Strength:", strength)

    if not length_criteria:
        print("- Should be at least 8 characters long.")
    if not lowercase_criteria:
        print("- Should include at least one lowercase letter.")
    if not uppercase_criteria:
        print("- Should include at least one uppercase letter.")
    if not digit_criteria:
        print("- Should include at least one number.")
    if not special_char_criteria:
        print("- Should include at least one special character (!@#$, etc.)")

# ---- Main Execution ----
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    check_password_strength(user_password)
