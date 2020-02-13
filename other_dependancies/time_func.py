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


