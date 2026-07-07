class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x_map = defaultdict(set)
        y_map = defaultdict(set)
        square_map = defaultdict(set)

        for x in range(9):
            for y in range(9):
                d = board[x][y]
                if d.isdigit():
                    if d in x_map[x] or d in y_map[y] or d in square_map[(x // 3, y // 3)]:
                        return False
                    else: 
                        x_map[x].add(d)
                        y_map[y].add(d)
                        square_map[(x // 3, y // 3)].add(d)
        

        return True