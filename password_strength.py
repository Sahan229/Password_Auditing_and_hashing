import re

def check_password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search("[A-Z]", password):
        score += 1

    if re.search("[a-z]", password):
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*()_+=]", password):
        score += 1

    levels = [
        "Very Weak",
        "Weak",
        "Medium",
        "Strong",
        "Very Strong"
    ]

    print("\nPassword Strength:")

    if score == 0:
        print("Very Weak")
    else:
        print(levels[score-1])