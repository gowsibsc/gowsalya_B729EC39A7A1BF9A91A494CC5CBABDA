#Leap year 

"""
year % 4 == 0 &
year % 100 != 0 /
year % 400 == 0

"""
def isLeapYear(Year):
  if (Year % 4 == 0 and Year % 100 != 0) or year % 400 == 0:
  return True
else:
   return False 
   
  Year =2012
if isLeapyear(Year):
  print(' {} is a leap year .'. format(year))
else:
  print('{} is not a leap year .'. format (year))
