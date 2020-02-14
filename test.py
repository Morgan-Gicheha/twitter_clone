# # testing divmode
# def div_mode(seconds):
#     day ,seconds= divmod(seconds,86400 )
#     hour, seconds = divmod(seconds,3600)
#     minute, seconds= divmod(seconds, 60)


#     if day >0:
#         print(f'{day}days')
#     elif hour > 0:
#         print(f'{hour}hour(s)')
#     elif minute > 0:
#         print(f'{minute}minutes')
#     else:
#         print(f'{seconds}seconds')

from datetime import datetime

now_ = datetime.now()
print(now_)