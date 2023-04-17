import random
def password()
    s1 = ['a','b','c','d','f','g','h','j','k','l','o','p','q','r']

    result = ''
    for i in range(11):
        result += random.choice(s1)
    return result


    p = password()
    print(p)