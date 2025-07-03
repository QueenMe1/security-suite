import re

def password_strength_checker(password):
    score = 0;

    if re.search(r'[a-z]',password):
        score += 1;
    if re.search(r'[A-Z]',password):
        score += 1;
    if re.search(r'\d', password):
        score += 1;
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score +=1;
    if len(password) >= 8:
        score += 1;

    with open('data/Top_common_passwords.txt') as file:
        if password in file.readline():
            return "Weak (Common Password, Change it!!)";

    if score <= 2:
        return "Weak";
    elif score == 3 or score ==4 :
        return "Medium";
    else:
        return "Strong";


def main ():

    passwords = input("Enter your password: ")
    print("Password Strength: " + password_strength_checker(passwords))


if __name__ == '__main__':
    main()
    