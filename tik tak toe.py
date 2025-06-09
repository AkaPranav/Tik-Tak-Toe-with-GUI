import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        # Center the window
        window_width = 400
        window_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_widgets()

    def create_widgets(self):
        # Create heading
        self.heading = tk.Label(self.root, text="Tic Tac Toe", font=('normal', 20, 'bold'))
        self.heading.grid(row=0, column=0, columnspan=3)
        
        # Create player turn label
        self.player_turn = tk.Label(self.root, text=f"Player {self.current_player}'s turn", font=('normal', 15))
        self.player_turn.grid(row=1, column=0, columnspan=3)
        
        # Create board
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=" ", font=('normal', 40), width=5, height=2,
                                   command=lambda row=row, col=col: self.on_button_click(row, col))
                button.grid(row=row+2, column=col, padx=5, pady=5)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player,fg="blue" if self.current_player == "X" else "red")
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.player_turn.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self, player):
        # Check rows
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        # Check columns
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        # Check diagonals
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2-i] == player for i in range(3)]):
            return True
        return False

    def is_full(self):
        return all([cell != " " for row in self.board for cell in row])

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")
        self.current_player = "X"
        self.player_turn.config(text=f"Player {self.current_player}'s turn")

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)  # Prevent window from being resized
    game = TicTacToe(root)
    root.mainloop()
