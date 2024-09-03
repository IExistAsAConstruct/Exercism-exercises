def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (not (a > 0 or b > 0 or c > 0)) or (a + b < c and a + c < b and b + c < a):
        return False
    if a == b and b == c:
        return True
    return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (not ( a > 0 or b > 0 or c > 0)) or (not (a + b >= c and a + c >= b and b + c >= a)):
        return False
    print("a + b:")
    print(a + b)
    print("a + c:")
    print(a + c)
    print("b + c:")
    print(b + c)
    if (a == b or b == c or a == c):
        return True
    return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (not (a > 0 or b > 0 or c > 0)) or (not (a + b >= c and a + c >= b and b + c >= a)):
        return False
    print("a + b:")
    print(a + b)
    print("a + c:")
    print(a + c)
    print("b + c:")
    print(b + c)
    if a != b and b != c and a != c:
        return True
    return False
