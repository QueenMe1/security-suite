import re

def password_strength_checker(password):
    score = 0;

    if re.search(r'[a-z]',password):
        score += 1;
    if re.search(r'[A-Z]',password):
        score += 1;
    if re.search(r'\d', password):
        score += 1;
    if 