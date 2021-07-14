import os
from sudoku import SudokuGrid, SudokuGridInput, SudokuSolver


def test_sudoku_grid_validator():
    var = SudokuGrid()
    assert var.validator('0') == '#'
    assert var.validator('1') == 1
    assert var.validator('6') == 6
    assert var.validator('9') == 9
    assert var.validator('10') == '#'
    assert var.validator('#') == '#'
    assert var.validator('q') == '#'
    assert var.validator(' ') == '#'


def test_sudoku_grid_source_grid_from():
    var = SudokuGrid()

    data0 = "1,2,3,4,5,6,7,8,9," \
            "1,2,3,4,5,6,7,8,9," \
            "1,2,3,4,9,6,7,8,9," \
            "1,2,3,4,5,6,7,8,9," \
            "1,2,#,4,5,6,7,#,9," \
            "1,2,3,4,5,6,7,8,9," \
            "1,2,3,4,5,6,7,8,9," \
            "1,2,3,4,5,#,7,8,9," \
            "1,2,3,4,5,6,7,8,9"

    var.source_grid_from(data0)
    assert len(var.grid[0]) == 9
    assert len(var.grid) == 9
    assert var.grid[0][0] == 1
    assert var.grid[2][4] == 9
    assert var.grid[8][4] == 5
    assert var.grid[3][1] == 2
    assert var.grid[4][2] == '#'
    assert var.grid[7][5] == '#'


def test_save_grid_to_txt():
    var = SudokuGrid()
    file_name = 'sol.txt'
    data0 = "1,2,3,4,5,6,7,8,9," \
            "1,2,3,4,5,6,7,8,9," \
            "1,2,3,4,9,6,7,8,9," \
            "1,2,3,4,5,6,7,8,9," \
            "1,2,#,4,5,6,7,#,9," \
            "1,2,3,4,5,6,7,8,9," \
            "1,2,3,4,5,6,7,8,9," \
            "1,2,3,4,5,#,7,8,9," \
            "1,2,3,4,5,6,7,8,9"
    var.source_grid_from(data0)

    var.save_grid_to_txt(file_name)
    assert file_name in os.listdir('./')

    os.remove(file_name)


def test_read_txt_file():
    var = SudokuGridInput()
    file_in = 'example_puzzles/puzzle1.txt'
    var.read_txt_file(file_in)
    eq = "9,#,#,2,1,#,4,#,#,#,3,2,#,4,#,#,#,#,#,4,#,8,#,#,#" \
         ",#,7,#,#,7,#,5,#,#,#,9,#,#,1,7,#,2,3,#,#,3,#,#,#,8," \
         "#,1,7,#,5,#,#,#,#,9,#,8,#,#,#,#,#,2,8,5,4,#,#,#,8,#,#,#,#,#,1,"
    assert var.data == eq
    assert len(var.data) == 162


def test_sudoku_solver_is_valid_entry():
    data = SudokuGridInput()
    data.read_txt_file('example_puzzles/puzzle1.txt')

    puz = SudokuGrid()
    puz.source_grid_from(data)

    solver = SudokuSolver(puz)

    assert solver.is_valid_entry(0, 1, 5)
    assert not solver.is_valid_entry(0, 1, 3)
    assert not solver.is_valid_entry(2, 0, 7)
    assert not solver.is_valid_entry(3, 0, 1)
    assert solver.is_valid_entry(8, 4, 3)


def test_sudoku_solver_solve():
    data = SudokuGridInput()
    data.read_txt_file('example_puzzles/puzzle1.txt')

    puz = SudokuGrid()
    puz.source_grid_from(data)

    solver = SudokuSolver(puz)
    answer = solver.solve()

    file_sol = open('example_puzzles/puzzle1_sol.txt', 'r')
    assert list(map(lambda x: x.replace('\n', ''), file_sol.readlines())) == str(answer).strip().split('\n')
    file_sol.close()
