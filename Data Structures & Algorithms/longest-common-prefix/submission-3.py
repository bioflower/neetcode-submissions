class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str: str = strs[0]
        
        for input_str in strs:
            if len(input_str) < len(shortest_str):
                shortest_str = input_str
        
        for i in reversed(range(len(shortest_str))):
            prefix: str = shortest_str[:i+1]
            contain_prefix: bool = True
            for index, input_str in enumerate(strs):
                if prefix not in input_str:
                    contain_prefix = False
                    break
                if index == len(strs) - 1 and contain_prefix:
                    return prefix
        return ""
                

                
        
            