#1
from datetime import datetime, timedelta
x = datetime.now() - timedelta(5)
print(x)
print()
#2
from datetime import datetime, timedelta
print("Yesterday: ", datetime.now() - timedelta(1))
print("Today: ", datetime.now())
print("Tomorrow: ", datetime.now() + timedelta(1))
print()
#3
import datetime
x = datetime.datetime.now().replace(microsecond=0)
print(x)
print()
#4
from datetime import datetime, timedelta
x = datetime.now()
y = datetime.now() + timedelta(seconds = 50)
z = y - x
z.seconds
print(z)