# Coding problem 1 HW5
age = int(input("Enter your age:"))

if age < 0:
    print("Error: Age cannot be less than 0")
else:
    matinee_input = input("Is this a showing? (yes/no):").strip().lower()
    is_matinee = matinee_input == "yes"

    if age < 13:
        price = 6.00 if is_matinee else 8.00
    elif age <= 17:
        price = 7.00 if is_matinee else 10.00
    elif age <= 64:
        price = 8.00 if is_matinee else 13.00
    else:
        price = 6.00 if is_matinee else 7.00

    print(f"Ticket price: ${price:.2f}")
