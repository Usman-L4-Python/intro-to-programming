from datetime import datetime
c = datetime.now()
# Displays Time
current_time = c.strftime('%H:%M:%S')
print('Current Time is:', current_time)

print('Current Date and Time is:', c)