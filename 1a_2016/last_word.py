
def last_word(inp):
    out = [inp[0]]
    for ch in inp[1:]:
        if ord(ch) >= ord(out[0]):
            out.insert(0, ch)
        else:
            out.append(ch)
    return "".join(out)

if __name__ == "__main__":
    import sys
    inp = open(sys.argv[1]).readlines()
    for ii, word in enumerate(inp[1:]):
        print "Case #" + str(ii+1) + ":", last_word(word.strip())
