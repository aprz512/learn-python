def range_list(start, end):
    """ this fun generate range numbers to create list. """
    if (start < end):
        while (start < end + 1):
            print start
            start += 1
    else:
        print "error"

range_list(0, 9)

i = 0
elements = []

while i < 6:
    print "At the top i is %d" % i
    elements.append(i)
    i += 1
    print "Numbers now: ", elements
    print "At the bottom i is %d" % i

for i in elements:
    print i
