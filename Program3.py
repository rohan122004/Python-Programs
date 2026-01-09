"""
Time Showing
"""

import time
t = time.strftime("%H:%M:%S")
print (t)
hour = int(time.strftime("%H"))
print (hour)

if (hour >= 5 and hour<=12):
    print("good morning")

elif (hour>=12 and hour<=15):
    print("good afternoon")

elif (hour>=15 and hour<=21):
    print("good evening")

else :
    print("good night")