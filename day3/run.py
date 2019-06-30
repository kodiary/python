# a = True
# b = False
#
# if(b):
#     print('b is true')
# else:
#     print('b is false')
#

# c = input("Enter First Number\n")
# d = input("Enter Second Number\n")
# e = int(c) + int(d)
# print(e)


# f = input("Enter the number\n")
# f = int(f)
#
# if(f % 2 == 0):
#     print("The number is even")
# else:
#     print("The humber is odd")

# g = input("Enter First Number\n")
# h = input("Enter Second Number\n")
#
# g = int(g)
# h = int(h)
#
# if(g > h):
#     print( str(g) + " is greater than " + str(h))
# elif(h > g):
#     print(str(h) + " is greater than " + str(g))
# else:
#     print("Both the numbers are equal")


g = input("Enter First Number\n")
h = input("Enter Second Number\n")

g = int(g)
h = int(h)

if(g >= h):
    if(g == h):
        print("Both the numbers are equal")
    else:
        print( str(g) + " is greater than " + str(h))
else:
    print(str(h) + " is greater than " + str(g))
