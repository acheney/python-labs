# patternB.py
# creates another simple number pattern
#
# Henry Lionni Guss
# 1/5/12

def main():
    n = eval(input("Enter a positive integer: "))
    for i in range(1, n + 1):
        for x in range(1, n + 1):
            print(i, end=' ')
        print()
main()