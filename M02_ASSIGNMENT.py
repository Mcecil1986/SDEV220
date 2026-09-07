while True:
    # Ask for last name
    last_name = input("Enter last name (or 'ZZZ' to quit): ")
    
    # Quit if sentinel value entered
    if last_name.upper() == "ZZZ":
        print("Exiting program.")
        break
    
    # Ask for first name
    first_name = input("Enter first name: ")
    
    # Ask for GPA
    try:
        gpa = float(input("Enter GPA: "))
    except ValueError:
        print("Enter a numeric value.")
        continue
    
    # Test GPA for Dean's List
    if gpa >= 3.5:
        print(f"{first_name} {last_name} made the Dean's List.")
    
    # Test GPA for Honor Roll
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} made the Honor Roll.")
    
    else:
        print(f"{first_name} {last_name} did not make the Dean's List or Honor Roll.")
