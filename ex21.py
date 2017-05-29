def add(a, b):
    print "adding %d + %d" % (a, b)
    return a + b

def subtract (a, b):
    print "subtract %d - %d" % (a, b)
    return a - b

def multiply (a, b):
    print "multiply %d * %d" % (a, b)
    return a * b

def divide (a, b):
    print "divide %d / %d" % (a, b)
    return a / b

print "Let's do some math!"

age = add(40, 8)
height = subtract(45, 6)
weight = multiply(50, 5)
iq = divide(300, 2)

print "age = %d, height = %d, weight = %d, iq = %d" % (age, height, weight, iq)

print "Here is a complex math:"

what = add(age, subtract(height, multiply(weight, divide(iq, 3))))

print "That becomes: ", what, "Can you do it by hand?"
