class SudokuGrid:
    def __init__(self):
        self.grid = [['#' for _ in range(9)] for _ in range(9)]

    def __str__(self):
        ret_var = '─'*25 + '\n'
        ci, cj = 0, 0
        for i in self.grid:
            ci += 1
            ret_var += '│ '
            for j in i:
                cj += 1
                ret_var += str(j) + " "
                if cj % 3 == 0:
                    ret_var += '│ '
            ret_var += '\n'
            if ci % 3 == 0:
                ret_var += '─'*25 + '\n'
                ci = 0
        return ret_var

    def source_grid_from(self, ip_object, separator=','):
        ip_object = str(ip_object).split(sep=separator)
        ip_object = list(map(SudokuGrid.validator, ip_object))
        for i in range(9):
            for j in range(9):
                self.grid[i][j] = ip_object[j + 9*i]
        return

    @staticmethod
    def validator(num):
        if num.isdigit() and int(num) in range(1, 10):
            return int(num)
        else:
            return '#'
