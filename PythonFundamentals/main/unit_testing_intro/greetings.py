def get_greeting(time_of_day: int) -> str:
    if time_of_day > 24 or time_of_day < 1:
        raise Exception("Illegal Argument Exception")
    elif 5 < time_of_day < 12:
        return 'Good morning!'
    elif 12 <= time_of_day < 18:
        return 'Good afternoon!'
    else:
       return 'Good evening'

try:
    get_greeting(-1)
except Exception as err:
    print(f"{err=}")
    print(type(err))

