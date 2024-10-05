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

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def display_solution():
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

    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, board[i][j])
    else:
        messagebox.showinfo("No Solution", "No solution exists for the given puzzle.")

# GUI using tkinter
def create_gui():
    global entries
    root = tk.Tk()
    root.title("Sudoku Solver")

    entries = [[None for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            entries[i][j] = tk.Entry(root, width=2, font=("Arial", 24), justify='center')
            entries[i][j].grid(row=i, column=j, padx=5, pady=5)

    solve_button = tk.Button(root, text="Solve", command=display_solution, font=("Arial", 14))
    solve_button.grid(row=9, column=0, columnspan=9, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
