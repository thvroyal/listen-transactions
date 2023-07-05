from datetime import datetime
import pytz

timestamp = 1688460743
vietnam_timezone = pytz.timezone('Asia/Ho_Chi_Minh')
datetime_str = datetime.fromtimestamp(timestamp, tz=vietnam_timezone).strftime('%Y-%m-%d %H:%M:%S')
print(datetime_str)