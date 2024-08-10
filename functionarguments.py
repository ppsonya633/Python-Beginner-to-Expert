
def multiplication(list):
    return a*b;

print(multiplication(6,6))




def multiplication2(*args):
    total=1
    for n in args:
        total*=n
    return total

print(multiplication2(2,3,4,5,6,7,8,9,10))


def user_details(**user):
    print(user)

user_details(name="john",age=22,city="new york")

