class Solution(object):
    def backspaceCompare(self, s, t):
        def checkletters(string):
            s = list()
            for letters in string:
                s.append(letters)
            s.reverse()
            keep = 0
            res = list()
            skip = 0
            for letters in s:
                # skip = 0
                if letters == '#':
                    skip += 1
                if skip == 0 and letters != '#':
                    res.append(s[keep])
                if skip > 0 and letters != '#':
                    skip = skip - 1
                keep += 1
            res.reverse()
            return res

        temp = checkletters(s)
        temp2 = checkletters(t)
        if temp == temp2:
            return 'true'