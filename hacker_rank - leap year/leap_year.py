def is_leap(year):
    leap = False
    if year % 400 == 0:
        return True
    # Check if the year is divisible by 100 but not by 400
    elif year % 100 == 0:
        return False
    # Check if the year is divisible by 4 but not by 100
    elif year % 4 == 0:
        return True
    # If none of the above conditions are met, it is not a leap year
    else:
        return False

year = int(input("Enter an year to check leap year: "))
print(is_leap(year))