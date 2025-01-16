from datetime import datetime

def get_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def main():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    greeting = get_greeting()
    print(f"{greeting}, {first_name} {last_name}!")

if __name__ == "__main__":
    main()