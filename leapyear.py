
#To run this program do python3 {file name} 
#take in the year as an int
year = input("Enter in a year(must be positive).")
if not type(year) is int:
    raise TypeError("Please enter an integer")

#check for divisability
if year % 4 == 0 and year % 100 != 0:
    print(str(year) + " is a leap year")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(str(year) + " is a leap year!")

else:
    print(str(year) + " not a leap year")