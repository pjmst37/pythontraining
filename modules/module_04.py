# Useful modules Part II: datetime and array
import datetime
from array import array

# creates time object
print(datetime.time(5, 45, 2))

print(datetime.date.today())

# arrays
arr = array('i', [1, 2, 3])
print(arr)
print(arr[0])
