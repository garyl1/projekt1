def even_numbers(n):
        for i in range(n//2):
            print(i+2+i, end=' ')






# 2 4 6 8 10 12 14 16 18 20
def powers(base, n):
    for i in range(n):
        print(base**i)

# 1 2 4 8 16 32 64 128 256 i+1512


def divisors(n):
    for i in range(1, n+1):
        if n%(i) == 0:
            print(i)

def fibonacci(n):
    first = 1
    second = 1
    print(1)
    print(1)
    for i in range(n-2):
        print(first + second)
        tmp = first
        first = second
        second = tmp + second


def fibonacci2(n):
    first = 1
    second = 1
    for i in range(n):
        print(first)
        sum = first + second
        first = second
        second = sum



# 1 1 2 3 2(10)


# 1 2 7 14

def table_products(n):
    print("   ",end=" ")
    for i in range(n):
        print(i+1, end=" ")

    print()
    print("   ", end=" ")
    for i in range (n):
        print("_", end=" ")
    print(" ")
    for row in range(n):
        print(row+1, "|", end=" ")
        for column in range(n):
            print((row+1)*(column+1), end=" ")
        print()



"""
    1 2 3 4 5
    - - - - -
1 | 1 2 3 4 5
2 | 2 4 6 8 10
3 | 3 6 9 12 15
4 | 4 8 12 16 20
5 | 5 10 15 20 25
"""


def square(n):
    for row in range(n):
        for column  in range(n):
            print("#", end=" ")
        print()

"""
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
"""

def empty_square(n):
    for row in range(n):
        for column  in range(n):
            if row == 0 or row == n-1 or column == 0 or column == n-1:
                print("#", end=" ")
            else:
                print(".", end=" ")

        print()


"""
# # # # #
# . . . #
# . . . #
# . . . #
# # # # #
"""



def chessboard(n):
    for row in range(n):
        for column in range(n):
            if row % 2 == 0:
                print("# .", end=" ")
            else:
                print(". #", end=" ")
        print()


"""
# . # . # . # .
. # . # . # . #
# . # . # . # .
. # . # . # . #
# . # . # . # .
. # . # . # . #
# . # . # . # .
. # . # . # . #
"""
chessboard(8)




