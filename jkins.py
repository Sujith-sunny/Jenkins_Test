import datetime
# from functools import wraps
# def Greet(fn):
#     @wraps(fn)
#     def wrapped(*args, **kwargs):
#         return 'Hello guys how are' + fn(*args, **kwargs) + 'Have a nice day'
#     return wrapped


Today_time = datetime.datetime.today()
Today = datetime.datetime.today().strftime('%A')
print(str(Today))
print(str(Today_time.date()))
print('Today is', str(Today))

#details()