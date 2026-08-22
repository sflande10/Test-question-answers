import datetime
sum =0
for i in range(1, 101):
    print(i)
    sum+= i
print("Sum:", sum)
today = datetime.date.today()
future_date = today + datetime.timedelta(days=30)
print("Todays date", today)
print("Date 30 days from now:", future_date)