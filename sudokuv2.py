import tkinter as tk
from tkinter import messagebox

# Sudoku Solver using Backtracking Algorithm
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

# Find all possible solutions using backtracking
def find_solutions(board, solutions):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        find_solutions(board, solutions)
                        board[row][col] = 0
                return
    solutions.append([row[:] for row in board])

def solve_and_count_solutions(board):
    solutions = []
    find_solutions(board, solutions)
    return solutions

def display_solution(solution):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, solution[i][j])

def reset_grid():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

def revert_to_unsolved():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            value = original_grid[i][j]
            if value != 0:
                entries[i][j].insert(0, value)

def solve_sudoku():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            value = entries[i][j].get()
            if value == '':
                row.append(0)
            else:
                row.append(int(value))
        board.append(row)
    
    global original_grid, solutions, current_solution_index
    original_grid = [row[:] for row in board]  # Save the original grid
    solutions = solve_and_count_solutions(board)  # Find all possible solutions
    
    if solutions:
        current_solution_index = 0
        display_solution(solutions[current_solution_index])
        messagebox.showinfo("Solutions Found", f"There are {len(solutions)} possible solutions.")
    else:
        messagebox.showinfo("No Solution", "No solution exists for the given puzzle.")

def switch_solution():
    global current_solution_index
    if solutions:
        current_solution_index = (current_solution_index + 1) % len(solutions)
        display_solution(solutions[current_solution_index])

# GUI using tkinter
def create_gui():
    global entries, original_grid, solutions, current_solution_index
    original_grid = None
    solutions = []
    current_solution_index = 0

    root = tk.Tk()
    root.title("Sudoku Solver")

    entries = [[None for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            entries[i][j] = tk.Entry(root, width=2, font=("Arial", 24), justify='center')
            entries[i][j].grid(row=i, column=j, padx=5, pady=5)

    solve_button = tk.Button(root, text="Solve", command=solve_sudoku, font=("Arial", 14))
    solve_button.grid(row=9, column=0, columnspan=3, pady=10)

    reset_button = tk.Button(root, text="Reset", command=reset_grid, font=("Arial", 14))
    reset_button.grid(row=9, column=3, columnspan=3, pady=10)

    revert_button = tk.Button(root, text="Revert", command=revert_to_unsolved, font=("Arial", 14))
    revert_button.grid(row=9, column=6, columnspan=3, pady=10)

    next_solution_button = tk.Button(root, text="Next Solution", command=switch_solution, font=("Arial", 14))
    next_solution_button.grid(row=10, column=0, columnspan=9, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
