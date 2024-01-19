import random
import bisect


def __init__(self, w: list[int]):
    self.cdf = []
    self.wlen = length(w)
    self.wsum = sum(w)
    self.probs = []
    for i in range(len(w)):
        self.probs.append(w[i]/sum(w))





def pickIndex(self) -> int:
    rand = random.randint(1, self.cdf[-1])
    idx = bisect.bisect_left(self.cdf, rand)
    return idx -1


