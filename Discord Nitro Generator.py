import random
import string
import requests

print("Discord Nitro Generator + Checker V1.0 - GAMMING-SERVICE & (TEAM)")
print("GAMMING-SERVICE & (TEAM)'")
print("Discord Server: https://discord.gg/rgk7EAGe")

def check_nitro_code(code):
    response = requests.get(f"https://discord.com/api/v8/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
    if response.status_code == 200:
        print(f'Valid | {code}')
        with open('Valid-discord-codes.txt', 'a') as f:
            f.write(f'{code}\n')
        return True
    else:
        print(f'Invalid | {code}')
        with open('Invalid-discord-codes.txt', 'a') as f:
            f.write(f'{code}\n')
        return False

# Prompt user to choose validation order
validation_order = input("Enter 'B' for Nitro Boost codes, 'C' for Nitro Classic codes, or 'Q' to quit: ")

if validation_order.lower() == 'b':
    amount = int(input('Amount of Nitro Boost codes to generate: '))
    value = 1

    while value <= amount:
        code_boost = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=24))
        if check_nitro_code(code_boost):
            value += 1
            continue

elif validation_order.lower() == 'c':
    amount = int(input('Amount of Nitro Classic codes to generate: '))
    value = 1

    while value <= amount:
        code_classic = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        if check_nitro_code(code_classic):
            value += 1
            continue

elif validation_order.lower() == 'q':
    print("Exiting...")
else:
    print("Invalid input. Exiting...")

input("Press Enter to exit...")