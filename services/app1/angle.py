def hours_hand(hour, minutes):
    base = (hour % 12) * (360 / 12)
    correction = (minutes / 60) * (360 / 12)
    return base + correction


def minutes_hand(minutes):
    minutes = minutes * (360 / 60)
    return minutes


def between(hour, minutes):
    return abs(hours_hand(hour, minutes) - minutes_hand(minutes))
