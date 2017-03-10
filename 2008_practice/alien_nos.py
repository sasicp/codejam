def str_to_num(inp, digits):
    base = len(digits)
    base_to_ind = dict((ch, jj) for jj, ch in enumerate(digits))
    out = 0
    mult = 1
    for ch in inp[-1::-1]:
        out += base_to_ind[ch]*mult
        mult *= base
    return out


def num_to_str(inp, digits):
    out = []
    num_to_ch = dict((jj, ch) for jj, ch in enumerate(digits))
    base = len(digits)
    while inp:
        out.insert(0, num_to_ch[inp % base])
        inp /= base
    return "".join(out)


if __name__ == "__main__":
    import sys
    for ii, line in enumerate(open(sys.argv[1]).readlines()[1:], 1):
        str_num, digit1, digit2 = line.split()
        num = str_to_num(str_num, digit1)
        str_out = num_to_str(num, digit2)
        print "Case #%d: %s" % (ii, str_out)