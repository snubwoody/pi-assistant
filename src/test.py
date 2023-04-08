import time

#TODO make this shit work man
def timer(func):
    def wrapper(*args):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print(f'{func.__name__} took {end - start:0.1f}s')
        
    return wrapper

@timer
def p(k):
    print(k)

p(9)