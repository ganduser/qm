import math

def main():
    f = open('doppia_fenditura_1.txt', 'w')
    y = -3
    while y <= 3:
        x = math.cos(10*y) * math.cos(10*y) * math.exp(-y*y)
        f.write(f'{x} {y}\n')
        y += .01

    f.close()

    f = open('doppia_fenditura_2.txt', 'w')
    y = -3
    while y <= 3:
        x = math.exp(-y*y)
        f.write(f'{x} {y}\n')
        y += .01

    f.close()

    return 0

if __name__ == '__main__':
    main()