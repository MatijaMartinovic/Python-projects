import tkinter as tk
from datetime import datetime, timedelta
import time


time1, time2 = 4.34, 34.54
time3 = datetime.now()
difference = timedelta(time2)


print(timedelta(seconds=float()))
print(difference)
print(time3)
time.sleep(5)
time4 = datetime.now()

print(time4-time3)

root = tk.Tk()

