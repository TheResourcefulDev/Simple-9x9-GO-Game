import tkinter as tk
from tkinter import messagebox

class GoGameGUI:
    """A GUI for playing the game of Go on a 9x9 grid."""

    def __init__(self, master):
        self.master = master
        self.master.title("Simple 9x9 Go Game")

        self.board_size = 9
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'black'  # Start with black player

        self.canvas = tk.Canvas(master, width=400, height=400, bg='white')
        self.canvas.pack()

        self.draw_board()

    def draw_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                x1, y1 = i * 40, j * 40
                x2, y2 = x1 + 40, y1 + 40
                self.canvas.create_rectangle(x1, y1, x2, y2, outline='black')

    def place_stone(self, event):
        x, y = event.x // 40, event.y // 40
        if self.board[x][y] == '':
            self.board[x][y] = self.current_player
            self.draw_stone(x, y)
            if self.check_winner(x, y):
                messagebox.showinfo("Game Over", f"{self.current_player.capitalize()} wins!")
                self.master.quit()
            else:
                self.current_player = 'white' if self.current_player == 'black' else 'black'

    def draw_stone(self, x, y):
        stone_color = 'black' if self.board[x][y] == 'black' else 'white'
        stone_size = 15
        stone_x = x * 40 + 20
        stone_y = y * 40 + 20
        self.canvas.create_oval(stone_x - stone_size, stone_y - stone_size,
                                stone_x + stone_size, stone_y + stone_size,
                                fill=stone_color)

    def check_winner(self, x, y):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Horizontal, vertical, and diagonal
        for dx, dy in directions:
            count = 1
            for i in range(1, 5):
                nx, ny = x + i * dx, y + i * dy
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size and \
                   self.board[nx][ny] == self.current_player:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                nx, ny = x - i * dx, y - i * dy
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size and \
                   self.board[nx][ny] == self.current_player:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = GoGameGUI(root)
    root.bind("<Button-1>", app.place_stone)  # Left click to place stone
    root.mainloop()
