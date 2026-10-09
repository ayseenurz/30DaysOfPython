from datetime import datetime
now = datetime.now()
print(now)                      
day = now.day        
month = now.month    
year = now.year         
minute = now.minute   
hour = now.hour      
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  

formatted_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("formatted time:",formatted_time)

today = "5 December, 2019"
str_to_time = datetime.strptime(today, "%d %B, %Y")
print(str_to_time)

print("todays date:", now)
new_year = datetime(2027, 1, 1)
print("new years date:",new_year)
diff = new_year - now
print("how much left for new year:", diff)

print("todays date:", now)
start = datetime(1970, 1, 1)
print("new years date:",start)
zero_to_now = now - start
print("how much time passed:", zero_to_now)