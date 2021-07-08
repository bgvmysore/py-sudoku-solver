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


def main():
    puz = SudokuGrid()
    print(puz)


if __name__ == '__main__':
    main()
