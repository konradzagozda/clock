class Clock(object):
    def __init__(self, hour, minute):
        while minute >= 60:
            minute -= 60
            hour += 1
        while hour >= 24:
            hour -= 24
        while minute < 0:
            minute += 60
            hour -= 1
        while hour < 0:
            hour += 24
        self.hour = hour
        self.minute = minute
        self.string = f'{self.hour:02d}:{self.minute:02d}'
        self.time_in_minutes = minute + hour*60

    def __repr__(self):
        return self.string

    def __eq__(self, other):
        return self.time_in_minutes == other.time_in_minutes

    def __add__(self, minutes):
        self.time_in_minutes += minutes
        return Clock(0,self.time_in_minutes)

    def __sub__(self, minutes):
        self.time_in_minutes -= minutes
        return Clock(0,self.time_in_minutes)




clock = (Clock(0, 45) + 40)

print(clock)