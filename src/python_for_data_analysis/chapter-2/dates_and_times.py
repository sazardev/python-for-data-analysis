from datetime import date, datetime, time

dt = datetime(2011, 10, 29, 20, 30, 21)

print(dt.day)
print(dt.minute)
print(dt.date())
print(dt.time())
dt.strftime("%22/11/2026")
