from datetime import date
import datetime
def time_():
    '''this function gets the date of registration'''
    now= date.today()
    format_today= now.strftime("%B %d, %Y")
    return format_today

def time_post():
    datetime_post = datetime.datetime.now()
    return datetime_post


# testing divmode
def div_mode(seconds):
    day ,seconds= divmod(seconds,86400 )
    hour, seconds = divmod(seconds,3600)
    minute, seconds= divmod(seconds, 60)


    if day >0:
        print(f'{day}days')
    elif hour > 0:
        print(f'{hour}hour(s)')
    elif minute > 0:
        print(f'{minute}minutes')
    else:
        print(f'{seconds}seconds')

