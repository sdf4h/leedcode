class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int):
            if row == n:
                nonlocal count
                count += 1
                return
            for col in range(n):
                diag1 = row - col  # Диагональ с отрицательным наклоном
                diag2 = row + col    # Диагональ с положительным наклоном
                if (col in used_cols or 
                    diag1 in used_diag1 or 
                    diag2 in used_diag2):
                    continue
                
                used_cols.add(col)
                used_diag1.add(diag1)
                used_diag2.add(diag2)
                
                backtrack(row + 1)
                
                used_cols.remove(col)
                used_diag1.remove(diag1)
                used_diag2.remove(diag2)

        count = 0
        used_cols = set()      # Занятые столбцы
        used_diag1 = set()     # Занятые диагонали /
        used_diag2 = set()      # Занятые диагонали \
        
        backtrack(0)
        return count
