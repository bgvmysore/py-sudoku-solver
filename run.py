from sudoku import SudokuGrid, SudokuGridInput


def main():
    puz = SudokuGrid()
    sudoku = SudokuGridInput()

    sudoku.read_txt_file('puzzle.txt')

    # print(sudoku.data)

    puz.source_grid_from(sudoku)
    print(puz)
    puz.save_grid_to_txt('sol.txt')


if __name__ == '__main__':
    main()
