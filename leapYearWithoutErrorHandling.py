# Checking if year is a leap year
def isLeapYear(year) :
    if (int(year) % 400) == 0:
        return True
    if (int(year) % 100) == 0:
        return False
    if (int(year) % 4) == 0:
        return True
    else:
        return False

# ask for input
year = input("Enter year: ")

if (isLeapYear(year)):
    print(year + " is a leap year.")
else:
    print(year + " is not a leap year")
