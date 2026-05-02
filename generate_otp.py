#!/usr/bin/env python3
import json
import pyotp
import time
import sys
import os


def main():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")

    if not os.path.exists(config_path):
        print(f"Error: {config_path} not found.")
        sys.exit(1)

    try:
        with open(config_path, "r") as f:
            config = json.load(f)
    except Exception as e:
        print(f"Error reading config: {e}")
        sys.exit(1)

    accounts = config.get("accounts", [])
    if not accounts:
        print("No accounts found in config.json")
        sys.exit(1)

    # Pick the first account for simplicity, or we could list them
    account = accounts[0]
    secret = account.get("totp_secret")

    if not secret:
        print(f"No totp_secret found for account: {account.get('name', 'Unknown')}")
        sys.exit(1)

    totp = pyotp.TOTP(secret)

    print(f"\nAccount: {account.get('name')}")
    print(f"Username: {account.get('username')}\n")

    try:
        while True:
            current_otp = totp.now()
            # Calculate remaining seconds
            remaining = 30 - (int(time.time()) % 30)

            # Use ANSI escape sequences to overwrite the same line
            sys.stdout.write(
                f"\rCurrent OTP: \033[1;32m{current_otp}\033[0m (expires in {remaining:2d}s) "
            )
            sys.stdout.flush()

            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nExiting...")


if __name__ == "__main__":
    main()
