import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r'[@$!%*?&#]', password):
        strength += 1
    else:
        feedback.append("Include at least one special character (@, $, !, %, *, ?, &, #).")

    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    return strength_levels[strength], feedback

password = input("Enter a password: ")
strength, feedback = check_password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions:")
    for suggestion in feedback:
        print(f"- {suggestion}")