def calc_parking_fee(hours, vehicle, is_member):
    if vehicle == "car":
        rate_per_hour = 4.0
    elif vehicle == "truck":
        rate_per_hour = 8.0
    else:
        raise ValueError("Invalid vehicle type. Must be 'car' or 'truck'.")

    fee = hours * rate_per_hour
    if is_member:
        fee *= 0.8
    return round(fee, 2)


def main():
    try:
        hours = float(input("Enter hours parked: "))
        if hours <= 0:
            print("Hours parked must be greater than 0.")
            return

        vehicle = input("Enter vehicle type (Car or Truck): ").strip().lower()
        membership = input("Are you a member? (Yes/No): ").strip().lower()
        if membership not in ("yes", "no"):
            print("Invalid Membership input. Please enter 'yes' or 'no'.")
            return

        fee = calc_parking_fee(hours, vehicle, membership == "yes")
        print(f"Parking fee: ${fee:.2f}")
    except ValueError as error:
        if str(error).startswith("Invalid vehicle type"):
            print("Invalid vehicle type. Please enter 'car' or 'truck'.")
        else:
            print("Invalid input. Enter numeric values for hours.")


if __name__ == "__main__":
    main()
