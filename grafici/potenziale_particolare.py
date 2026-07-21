import math

def main():
    f = open('potenziale_particolare.dat', 'w')
    x = -4.5
    while x <= 4.5:
        y = -2 * math.exp(-x*x / 4.)
        f.write(f'{x} {y}\n')
        x += .02
    f.close()

    f = open('potenziale_particolare_1.dat', 'w')
    x = -5.
    while x <= 5.:
        y = 2.5 * math.exp(-.25*x*x)
        f.write(f'{x} {y}\n')
        x += .02
    f.close()

    f = open('potenziale_particolare_2.dat', 'w')
    x = -5.
    while x <= 5.:
        y = 3 * x * math.exp(-.25*x*x)
        f.write(f'{x} {y}\n')
        x += .02
    f.close()

    f = open('potenziale_particolare_3.dat', 'w')
    # 2.5*exp(-.25*(\x-1)*(\x-1)
    x = 0
    while x <= 5.:
        y = 2.5 * math.exp(-.25*(x-1)*(x-1))
        f.write(f'{x} {y}\n')
        x += .02
    f.close()

    return 0

if __name__ == '__main__':
    main()