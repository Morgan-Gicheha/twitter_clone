from datetime import date
def time_():
    now= date.today()
    format_today= now.strftime("%B %d, %Y")
    return format_today

