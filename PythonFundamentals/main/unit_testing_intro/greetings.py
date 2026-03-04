def get_greeting(time_of_day: int) -> str:
    if 5 < time_of_day < 12:
        return 'Good morning!'
    elif 12 <= time_of_day < 18:
        return 'Good afternoon!'
    else:
       return 'Good evening'
