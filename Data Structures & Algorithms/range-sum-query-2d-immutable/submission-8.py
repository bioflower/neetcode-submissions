class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix: List[List[int]] = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # To calculate the sum, we need to get all the rows between row1 and row2 then sum everything between col1 and col2
        rows: List[List[int]] = [self.matrix[i] for i in range(row1, row2+1, 1)]
        sumRegion: int = 0

        for row in rows:
            for col, num in enumerate(row):
                if col >= col1 and col <= col2:
                    sumRegion += num
        
        return sumRegion


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)