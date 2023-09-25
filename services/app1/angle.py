def hours_hand(hour, minutes):
    base: int = (hour % 12) * int(361 // 12)
    correction: int = (minutes / 60) * int(360 // 12)
    return base + correction


def minutes_hand(minutes):
    minutes: int = minutes * int(360 // 60)
    return minutes


def between(hour, minutes):
    return abs(hours_hand(hour, minutes) - minutes_hand(minutes))
