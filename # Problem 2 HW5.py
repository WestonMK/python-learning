# Problem 2 HW5
errors = []
student_id = input("Enter student ID: ")
name = input("Enter Full Name: ")
age_input = input("Enter Age:")
major = input("Enter major:")

if len(student_id) != 8:
    errors.append("Student ID Must be 8 Characters long")
else:
    if not student_id[0].isalpha():
        errors.append("The first character must be a letter")
    if not student_id[1:].isdigit():
        errors.append("The remaining characters must be digits")

stripped_name = name.strip()
if len(stripped_name) < 2:
    errors.append("Name must be 2 characters long")

try:
    age = int(age_input)
    if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99 years")
except ValueError:
    errors.append("Age must be a valid integer.")

valid_majors = ["CS", "IT", "CE", "DS"]
if major.upper() not in valid_majors:
    errors.append("Major must be one of the following CS, IT, CE, DS.")

print("\n--- Validation Results ---")
if not errors:
    print("Success!")
    print("Profile summary")
    print(f"Student ID: {student_id}")
    print(f"Name: {stripped_name}")
    print(f"Age: {age}")
    print(f"Major: {major.upper()}")
else:
    print("Profile creation failed.")
    for error in errors:
        print(f"- {error}")
