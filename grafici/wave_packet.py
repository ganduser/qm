import math

def main():
    f = open('wave_packet.txt', 'w')
    x = -2
    while x <= 6:
        y = 4 * math.cos(6*x) * math.exp(-(x - 2)*(x - 2)/3)
        f.write(f'{x} {y}\n')
        x += .02
    f.close()

    return 0

if __name__ == '__main__':
    main()