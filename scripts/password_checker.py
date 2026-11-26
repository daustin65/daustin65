def check_password(password):
    score = 0
    if len(password) >= 12:
        score = score + 1
    
    has_upper = False
    has_digit = False
    has_symbol = False

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True

    if has_upper:
        score = score + 1
    if has_digit:
        score = score + 1
    if has_symbol:
        score = score + 1
    
    return score

while True:
    password = input("Enter a password to test (or quit); ")

    if password == "quit":
        break
        
    score = check_password(password)
    print("Score:", score, "out of 4")

    if score == 4:
        print("Strong password.")

    elif score >= 2:
        print("Medium password.  Add what is missing.")
    else:
        print("Weak password. Do not use this one.")