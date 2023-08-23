def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)
    
    return hour_str + minute_str


print(convert_to_24_hour(12, 30, "am")) 
print(convert_to_24_hour(12, 30, "pm")) 
