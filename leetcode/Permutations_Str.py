from __future__ import print_function


class Permutation:
    def __init__(self):
        pass

    def permute(self, s):
        s_list = list(s)
        self.permute_helper(s_list, 0, len(s)-1)

    def permute_helper(self, s, l, r):
        indent = "\t"*l
        # print(indent, "FIXED: ", self.get_str(s[0:l]), "CHOSEN: ", self.get_str(s[l:]))
        if r == l:
            print("".join(s[i] for i in range(len(s))))
        else:
            for i in range(l, r+1):
                # choose
                s[i], s[l] = s[l], s[i]
                # explore
                self.permute_helper(s, l+1, r)
                # unchoose - backtracking step
                s[i], s[l] = s[l], s[i]

    def get_str(self, l):
        return "".join(l[i] for i in range(len(l)))


obj = Permutation()
obj.permute("marty")
