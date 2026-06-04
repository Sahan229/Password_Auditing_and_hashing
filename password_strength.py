import re
 
def check_password_strength(password):
    score = 0
    feedback = []
 
    if len(password) >= 8:
        score += 1
    else:
        feedback.append(" Use at least 8 characters")
 
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append(" Add uppercase letters (A-Z)")
 
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append(" Add lowercase letters (a-z)")
 
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append(" Add numbers (0-9)")
 
    if re.search(r'[!@#$%^&*()_\-+=/?<>.,|\\]', password):
        score += 1
    else:
        feedback.append(" Add special characters (!@#$...)")
 
    levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    print(f"\n Password : {password}")
    print(f" Strength : {levels[score - 1] if score > 0 else 'Very Weak'} ({score}/5)")
    if feedback:
        print(" Suggestions:")
        for f in feedback:
            print(f"   {f}")
    else:
        print(" Great password!")