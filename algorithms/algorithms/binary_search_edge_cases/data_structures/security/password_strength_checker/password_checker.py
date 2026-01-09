import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Less than 8 characters"
    if not re.search(r"[A-Z]", password):
        return "Weak: Missing uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Weak: Missing lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Weak: Missing number"
    if not re.search(r"[!@#$%^&*()_+=-]", password):
        return "Weak: Missing special character"
    return "Strong"

# Edge case tests
if __name__ == "__main__":
    test_passwords = [
        "short",             # too short
        "alllowercase1!",    # no uppercase
        "ALLUPPERCASE1!",    # no lowercase
        "NoNumber!",         # no number
        "NoSpecial123",      # no special character
        "GoodPass1!"         # strong
    ]

    for pw in test_passwords:
        print(f"{pw}: {check_password_strength(pw)}")
