from sudoku import SudokuGrid, SudokuGridInput, SudokuSolver


def main():
    file_data = SudokuGridInput()
    path_to_puzzle = input("Enter the path to txt file containing the puzzle: ")
    try:
        file_data.read_txt_file(path_to_puzzle)
    except ValueError:
        print(f"[ERR]: \"{path_to_puzzle}\" - Input file does not contain sudoku puzzle in the right format!")
        print("Try Again :-( ")
        return
    except IOError as exception_here:
        print(exception_here)
        print("Try Again :-( ")
        return

    puz = SudokuGrid()
    puz.source_grid_from(file_data)

    print("PUZZLE:")
    print(puz)

    my_solver = SudokuSolver(puz)
    print("\nsolving puzzle....\n")
    answer = my_solver.solve()

    print("SOLUTION:")
    print(answer)

    wanna_save = input("Do you want to save solution to a file? [y/N]")
    if wanna_save == 'y':
        error = True
        while error:
            output_file = input("Enter output filename: ")
            try:
                answer.save_grid_to_txt(output_file)
            except FileExistsError:
                print("File already exists!...Try again")
            else:
                error = False
    else:
        return


if __name__ == '__main__':
    main()
