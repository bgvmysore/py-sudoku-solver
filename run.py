from Sudoku import SudokuGrid


def main():
    puz = SudokuGrid()
    sudoku = '1,2,3,4,5,#,7,8,9,' \
             '1,2,3,4,5,6,7,8,9,' \
             '1,#,3,4,5,#,7,8,9,' \
             '1,2,#,4,5,6,7,8,9,' \
             '1,2,3,4,5,6,7,8,9,' \
             '1,2,3,4,5,6,7,8,9,' \
             '1,2,3,4,5,6,#,8,9,' \
             '1,2,#,4,5,6,7,8,9,' \
             '1,2,3,4,5,6,7,8,9'
    puz.source_grid_from(sudoku)
    print(puz)


if __name__ == '__main__':
    main()
