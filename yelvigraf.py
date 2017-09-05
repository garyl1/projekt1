from turtle import Turtle   # import tridy Turtle pro zelvi grafiku

julie = Turtle()            # vytvoreni nove zelvy jmenem julie


def polygon(n, size):
    for i in range(n):

        julie.forward(size)
        julie.right(360/n)

# polygon(12, 50)

def diamant(n, size):
    for i in range(n):
        polygon(n, size)
        julie.right(360/n)

diamant(8, 10)

input()

