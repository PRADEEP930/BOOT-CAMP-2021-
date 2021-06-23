#------------------------------------------------------------------------------
#     ***     TO CHECK GIVEN YEAR IS A LEAP YEAR OR NOT     ***
#==============================================================================
#     Take year as input in integer form and save in variable "year".
#     Default value of leap.
#     pass year in if condition,true:leap=1 or false:leap=0/not a leap year.
#------------------------------------------------------------------------------
year = int(input(" enter the year to check leap year = "))
leap = 0
if year % 400 == 0:
    leap=1
elif year % 4 == 0 and year % 100 != 0:
    leap = 1
if leap == 1:
    print("{} year is a leap year".format(year))
else :
    print("{} year is not a leap year ".format(year))