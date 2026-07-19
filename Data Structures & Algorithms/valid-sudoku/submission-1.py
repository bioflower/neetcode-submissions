class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidSeries(row: [List[str]]) -> bool:
            non_empty_entries: List[int] = []
            for entry in row:
                if entry != ".":
                    try:
                        non_empty_entries.append(int(entry))
                    except ValueError:
                        return False
            if len(non_empty_entries) != len(set(non_empty_entries)):
                return False
            if len(non_empty_entries) > 0 and max(non_empty_entries) > 9:
                return False
            if len(non_empty_entries) > 0 and min(non_empty_entries) < 0:
                return False
            return True

        def isValidEntry(entry: str, sequence: List[str]) -> bool:
            if entry == ".":
                return True
            
            try:
                entry_val = int(entry)
            except ValueError:
                return False
            if len(sequence) > 0 and entry in sequence:
                return False
            if entry_val > 9:
                return False
            if entry_val < 0:
                return False
            
            return True

        cols: List[List[str]] = [[] for _ in range(9)]
        squares: List[List[str]] = [[] for _ in range(9)]
        # iterate through all the rows to construct columns and 3x3 square
        for row_index, row in enumerate(board):
            if not isValidSeries(row):
                return False
            
            for col_index, entry in enumerate(row):
                if not isValidEntry(entry, cols[col_index]):
                    return False
                
                
                square_index: int = row_index // 3 * 3 + col_index // 3
                if not isValidEntry(entry, squares[square_index]):
                    return False

                if entry != ".":
                    cols[col_index].append(entry)
                    squares[square_index].append(entry)
                    
        return True