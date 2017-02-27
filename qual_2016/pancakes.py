import heapq
import string
import sys

tran = string.maketrans('+-', '-+')


def eval_cand_cost(cand):
    if cand[-1] != '+':
        cand += '+'
    return sum(cand[ii] != cand[ii+1] for ii in range(len(cand)-1))


def gen_new_candidates(item, steps, heap):
    cost = eval_cand_cost(item)
    for ii in range(len(item)):
        cand = string.translate(item[:ii+1], tran) + item[ii+1:]
        new_cost = eval_cand_cost(cand)
        if new_cost < cost + 1:
            heapq.heappush(heap, (new_cost + steps + 1, new_cost, steps + 1, cand))

def count_steps(cand):
    heap = [(eval_cand_cost(cand), eval_cand_cost(cand), 0, cand)]
    cost = heap[0][1]
    steps = 0
    item = heap[0]
    while heap and (cost !=0 ):
        item = heapq.heappop(heap)
        cost = item[1]
        if cost:
            gen_new_candidates(item[-1], steps, heap)
            steps += 1
    if not cost:
        return item[-2]
    raise ValueError

if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    for ii, line in enumerate(lines[1:],1):
        print 'Case #' + str(ii) + ":", count_steps(line.strip())

