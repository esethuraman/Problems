class GroupAnagrams:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        hmap = {}
        for entry in strs:
            k = entry
            s = ''.join(sorted(k))
            if s in hmap:
                hmap[s].append(k)
            else:
                hmap[s] = [k]
        for v in hmap.itervalues():
            res.append(v)
        return res


obj = GroupAnagrams()
obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
