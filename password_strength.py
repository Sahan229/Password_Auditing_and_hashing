import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
	  score += 1
    else:
	  feedback.append("Use at least 8 charachters")

    if re.search(r'[A-Z]',password):
	  score += 1
    else:
	feedback.append("Add upper case letters(A-Z)")

    if re.search(r'[a-z]',password):
	score += 1
    else:
	feedback.append("Add lower case letter(a-z)")

    if re.search(r'[0-9]',password):
	score += 1
    else:
	feedback.append("Add numbers")

    if re.search(r'[!@#$%^&*()_-+=/?<>.,\|]',password)
	score += 1
    else:
	feedback.append("Add the special characters(!@#$...)")

    levels = ["Nery Weak","Weak","Modarate","Strong","Very Strong"]
    print(f"\n password: {password}")
    print(f"\ Strength: {levels[score - 1] if score > 0 else 'very Weak'} ({score}/5)")

    if feedback:
        print(" Suggestions:")
        for f in feedback:
            print(f"   {f}")
    else:
        print(" Great password!")
  