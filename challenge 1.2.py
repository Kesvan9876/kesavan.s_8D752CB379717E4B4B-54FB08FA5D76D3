# To get the year (integer input) from the user
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
