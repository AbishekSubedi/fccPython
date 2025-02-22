def add_time(start, duration, start_day=None):
    start_time, period = start.split()
    start_hour, start_min = map(int, start_time.split(':'))

    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    duration_hour, duration_min = map(int, duration.split(':'))

    new_minute = start_min + duration_min
    extra_hour = new_minute // 60
    new_minute %= 60

    new_hour = start_hour + duration_hour + extra_hour
    days_later = new_hour // 24
    new_hour %= 24

    new_period = "AM" if new_hour < 12 else "PM"
    new_hour = new_hour if new_hour % 12 != 0 else 12
    new_hour = new_hour % 12 if new_hour % 12 != 0 else 12

    new_time = f"{new_hour}:{new_minute:02d} {new_period}"

    if start_day:
        days_of_week = ["Monday", "Tuesday", "Wednesday",
                        "Thrusday", "Friday", "Saturday", "Sunday"]
        start_day = start_day.capitalize()
        start_index = days_of_week.index(start_day)
        new_day = days_of_week[(start_index + days_later) % 7]
        new_time += f", {new_day}"

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time


print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('11:43 AM', '00:20'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 PM', '24:20', 'tueSday'))
print(add_time('6:30 PM', '205:12'))
