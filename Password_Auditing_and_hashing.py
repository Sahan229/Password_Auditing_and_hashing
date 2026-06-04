import re

def check_password_strength(password):
	score = 0
	feedback = []

if len(password) >= 8:
	score += 1
else:
	feedback.append("Use at least 8 charachters")

if re.search(r'[A-z]',password):
	score += 1
else:
	feedback.append("Add upper case letters")

if re.search(r'[a-z]',password):
	score += 1
else:
	feedback.append("Add lower case letter")

if re.search(r'[0-9]',password)
	score += 1\
else:
	feedback.append("Add numbers")

if re.search(r'[!@#$%^&*()_-+=/?<>.,\|]',password)
	score += 1
else:
	feedback.append("Add the special characters(!@#$...)")

level = ["Nery Weak","Weak","Modarate","Strong","Very Strong"]
print(f"\n password: {password}")
print(f"\ Strength: {levels[score - 1] if score > 0 else 'very Weak'} ({score}/5)")
  print(f)