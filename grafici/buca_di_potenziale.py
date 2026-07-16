import math

def main():
    f1 = open('buca_di_potenziale_cos.txt', 'w')
    f2 = open('buca_di_potenziale_sin.txt', 'w')
    x = -3
    while x <= 3:
        y = 2.5 * math.cos(math.pi * x / 6.)
        f1.write(f'{x} {y}\n')
        y = 2.5 * math.sin(math.pi * x / 3.)
        f2.write(f'{x} {y}\n')
        x += .02
    f1.close()
    f2.close()
    return 0

if __name__ == '__main__':
    main()