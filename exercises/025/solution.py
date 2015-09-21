import datetime
d = datetime.date.today()
iso = d.isoformat()
print("Today is", iso[0:9], "and it is", iso[11:18])
