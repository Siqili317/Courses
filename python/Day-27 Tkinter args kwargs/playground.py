# Unlimited positional arguments

def add(*args):
    # type(args) is tuple
    out = 0
    for arg in args:
        out += arg
    return out

print(add(1,2), add(3,3,3,3))

# Keyword arguments
def calculate(n, **kwargs):
    # type(kwargs) is dictionary
    # for key, value in kwargs.items():

    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs) -> None:
        self.make = kwargs['make']
        self.model = kwargs.get('model') #get is similar with []. Only it returns none when label is not defined such no crash

my_car = Car(make='Nissan', model='GTR')
print(my_car.model)