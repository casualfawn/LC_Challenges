
#from typing import List
strs = ['flower', 'flow', 'flown', 'flab', 'flrab']
























    def longestCommonPrefix(v):
        ans = ""
        v = sorted(strs)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans


longestCommonPrefix(strs)





