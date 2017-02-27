import math


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1
    sqr = min(sqr, 10000)
    for divisor in xrange(3, sqr, 2):
        if n % divisor == 0:
            return divisor
    return 0


def check_jam(n):
    out = [n]
    for base in range(2, 11):
        val = int(n, base)
        divisor = is_prime(val)
        if not divisor:
            return []
        out.append(divisor)
    return out


def gen_jams(length, num):
    out = []
    for ii in xrange(2**(length-2)):
        val = "1" + bin(ii)[2:].rjust(length-2, '0') + "1"
        val1 = check_jam(val)
        if val1:
            out.append(val1)
        if len(out) == num:
            break
    return out


if __name__ == "__main__":
    jams= gen_jams(32, 500)
    print "Case #1:"
    for jam in jams:
        print jam[0], " ".join(str(x) for x in jam[1:])

