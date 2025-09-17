from datetime import datetime, date, time, timedelta, timezone
import time as time_module # For the time module

# Current date and time
now = datetime.now()
today = date.today()
current_time = datetime.now().time()
print(now)
print(today)
print(current_time)

# Creating specific dates
dt = datetime(2023, 12, 25, 15, 30, 45) # Year, month, day, hour, minute, second
d = date(2023, 12, 25)
t = time(15, 30, 45)

# Formatting dates
formatted = now.strftime('%Y-%m-%d %H:%M:%S') # 2023-12-25 15:30:45
parsed = datetime.strptime('2023-12-25', '%Y-%m-%d') # String to datetime

# Date arithmetic
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
difference = datetime(2023, 12, 31) - datetime(2023, 1, 1) # Returns timedelta

# Timezone handling (requires pytz or Python 3.9+ zoneinfo)

utc_now = datetime.now(timezone.utc)

# Timestamps
timestamp = datetime.now().timestamp() # Seconds since epoch
dt_from_ts = datetime.fromtimestamp(timestamp)

# Sleeping (from time module)
time_module.sleep(2.5) # Sleep for 2.5 seconds