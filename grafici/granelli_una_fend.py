import math

def main():
    f = open('granelli_una_fend_1.txt', 'w')
    y = -3
    while y <= 3:
        x = math.exp(-math.pow(y + 1,2))
        f.write(f'{x} {y}\n')
        y += .01

    f.close()

    f = open('granelli_una_fend_2.txt', 'w')
    y = -3
    while y <= 3:
        x = math.exp(-math.pow(y - 1,2))
        f.write(f'{x} {y}\n')
        y += .01

    f.close()

    return 0

if __name__ == '__main__':
    main()