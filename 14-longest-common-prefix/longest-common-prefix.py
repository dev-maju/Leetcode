class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix_set=set()
        # for num in strs:
        #     for i in range(1,len(num)+1):
        #         prefix_set.add(num[:i])
        # longest_prefix=""
        # for num in strs:
        #     for i in range(1,len(num)+1):
        #         prefix = num[:i]
        #         if prefix in prefix_set and len(prefix)>len(longest_prefix):
        #             longest_prefix=prefix
        # return longest_prefix

        if not strs:
            return ""
        prefix=strs[0]
        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix