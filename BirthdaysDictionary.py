# Birthdays.py

# This program accepts name and birthday information from a user, stores it in a dictionary, then appends it to a file and prints it to the terminal in the following format: [Full Name]'s birthday is [Month] [Day], [Year]

bDaysDict = {}  # Create dictionary to store birthdays

# Valid months list
valid_months = [
    "January", "February", "March", "April", "May", "June", "July", "August", "September", 
    "October", "November", "December"
]

# Validates name input (only allow letters, spaces, and hyphens as input characters)
def validate_name(name):
    if name.isalpha() or all(char.isalpha() or char.isspace() or char == "-" for char in name):
        return True
    else:
        print("Invalid name")
        return False

# Validates month input
def validate_month(month):
    if month.capitalize() in valid_months:
        return True
    else:
        print("Invalid month")
        return False

# Validates day input based on the month
def validate_day(month, day):
    try:
        day = int(day)
        if month == "February" and not (1 <= day <= 29): return False
        elif month in ["April", "June", "September", "November"] and not (1 <= day <= 30): return False
        elif not (1 <= day <= 31): return False
        return True
    except ValueError:
        print("Invalid day")
        return False

# Validates year input
def validate_year(year):
    try:
        year = int(year)
        if 1900 <= year <= 2025:
            return True
        else:
            print("Year must be between 1900 and 2025")
            return False
    except ValueError:
        print("Invalid year")
        return False

def getBdayInfo():  # Collects and stores birthday info in bDaysDict
    while True:  # Loop until user decides to stop
        bName = input("Enter your full name: ")
        if not validate_name(bName): continue
        
        bMonth = input("Enter the month you were born: ")
        if not validate_month(bMonth): continue
        
        bDay = input("Enter the day you were born: ")
        if not validate_day(bMonth, bDay): continue
        
        bYear = input("Enter the year you were born: ")
        if not validate_year(bYear): continue
        
        bDaysDict[bName] = [bMonth, bDay, bYear]  # Store birthday info
        
        answer = input("Would you like to enter another birthday? (Yes/No) ")
        if answer.lower() == "yes":
            continue  # Repeat if 'yes'
        elif answer.lower() == "no":
            break  # Exit loop if 'no'
        else:
            print("Please enter Yes or No")

# Run the function
getBdayInfo()

# Append birthday info to file
with open("C:\\Users\\your_username\\Desktop\\PythonScripts\\BirthdaysList.txt", "a") as bl:
    for keyName in bDaysDict:
        print(f"{keyName}'s birthday is {bDaysDict[keyName][0]} {bDaysDict[keyName][1]}, {bDaysDict[keyName][2]}", file=bl)

# Display added birthdays
print(f"\nNew Birthday(s): {bDaysDict}\nAll Birthdays:")

# Read and display file contents
with open("C:\\Users\\your_username\\Desktop\\PythonScripts\\BirthdaysList.txt", "r") as bl:
    print(bl.read(), end="")
