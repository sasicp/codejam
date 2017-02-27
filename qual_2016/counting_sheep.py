import sys

def nums(inp):
    out = set()
    while (inp):
        out.add(inp%10)
        inp = inp/10
    return out
def find_final(num):
    found = set()
    num1 = 0
    while(len(found)< 10):
        num1 += num
        found.update(nums(num1))
    return num1


if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    for ii, line in enumerate(lines[1:],1):
        num = int(line)
        if not num:
            print "Case #%d: INSOMNIA" % ii
        else:
            print "Case #%d: %d" % (ii, find_final(num))
