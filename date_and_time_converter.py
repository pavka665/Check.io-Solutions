def date_time(time: str) -> str:
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    date = time.split(' ')
    d = date[0].split('.')
    t = date[1].split(':')

    day = int(d[0])
    month = months[int(d[1]) - 1]
    year = f'{ int(d[2]) } year' 

    hour = f'{ int(t[0]) } hour' if int(t[0]) == 1 else f'{ int(t[0]) } hours'
    minute = f'{ int(t[1]) } minute' if int(t[1]) == 1 else f'{ int(t[1]) } minutes'

    time = f'{ day } { month } { year } { hour } { minute }'
    return time



# print("Example:")
# print(date_time("01.01.2000 00:00"))

print(date_time("01.01.2000 00:00")) # == "1 January 2000 year 0 hours 0 minutes"
print(date_time("09.05.1945 06:07")) # == "9 May 1945 year 6 hours 7 minutes"