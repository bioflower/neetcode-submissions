class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s: List[str] = list(s)
        char_t: List[str] = list(t)
        dict_s : Dict[str, int] = dict()
        for char in char_s:
            if char not in dict_s:
                dict_s[char] = 1
            else:
                dict_s[char] += 1

        for char in char_t:
            if char not in dict_s:
                return False
            dict_s[char] -= 1
        
        for char in dict_s:
            if dict_s[char] != 0:
                return False

        return True
    
            


        