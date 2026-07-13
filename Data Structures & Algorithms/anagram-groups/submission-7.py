class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checked_indices: List[int] = [] 
        output: List[List[str]] = []

        for index, input_str in enumerate(strs):
            if index not in checked_indices:
                output.append([input_str])
                checked_indices.append(index)
                target_dict: Dict[str, int] = dict()
                for target_char in list(input_str):
                    if target_char not in target_dict:
                        target_dict[target_char] = 1
                    else:
                        target_dict[target_char] += 1

                for cand_index in range(index, len(strs), 1):
                    if cand_index not in checked_indices:
                        cand_input_str = strs[cand_index]
                        if len(cand_input_str) != len(input_str):
                            continue
                        
                        cand_dict: Dict[str, int] = dict()
                        for cand_char in list(cand_input_str):
                            if cand_char not in cand_dict:
                                cand_dict[cand_char] = 1
                            else:
                                cand_dict[cand_char] += 1

                        is_anagrams: bool = True
                        for char in target_dict:
                            if char not in cand_dict or target_dict[char] != cand_dict[char]:
                                is_anagrams = False
                                break
                        
                        if is_anagrams:
                            checked_indices.append(cand_index)
                            output[-1].append(cand_input_str)        
                            
        return output
