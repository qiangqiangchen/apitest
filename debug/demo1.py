def log(url,method):
    def decorator(func):
        def wrapper(*args, **kw):
            print('{},{}:'.format(url, method))
            return func(*args, **kw)
        return wrapper
    return decorator



@log(url="test",method="Get")
def now():
    print("test")




if __name__=='__main__':
    now()