from datetime import datetime

def generate_birthdays():
    birthdays = []
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                datetime.strptime(f"{month:02d}{day:02d}", "%m%d")
                birthdays.append(f"{month:02d}{day:02d}")
            except ValueError:
                continue
    return birthdays

def generate_birthrack(username, symbols):
    birthdays = generate_birthdays()
    password_list = []
    
    for symbol in symbols:
        for bday in birthdays:
            password_list.append(username + symbol + bday)
            password_list.append(username.capitalize() + symbol + bday)
            password_list.append(username.upper() + symbol + bday)
    
    return password_list

# Input
username = input("Enter username: ")
symbol_input = input("Enter symbols separated by commas (e.g., _, @, -): ")
symbols = [s.strip() for s in symbol_input.split(',') if s.strip()] + [""]

# Generate
passwords = generate_birthrack(username, symbols)

# Output
with open("birthrack_output.txt", "w") as f:
    for pw in passwords:
        print(pw)
        f.write(pw + "\n")
