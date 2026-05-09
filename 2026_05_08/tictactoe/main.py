import tkinter as tk
from tkinter import messagebox


class TicTacToeAI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kółko i Krzyżyk: Gracz vs Niezwyciężone AI")

        self.board = [" " for _ in range(9)]
        self.human = "X"
        self.ai = "O"

        # Statystyki
        self.wins = 0
        self.losses = 0
        self.draws = 0

        self.buttons = []
        self.setup_ui()

    def setup_ui(self):
        # Statystyki na górze
        self.stats_label = tk.Label(self.root,
                                    text=f"Ty (X): {self.wins} | AI (O): {self.losses} | Remisy: {self.draws}",
                                    font=('Arial', 12))
        self.stats_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Siatka 3x3
        for i in range(9):
            btn = tk.Button(self.root, text=" ", font=('Arial', 20, 'bold'), width=5, height=2,
                            command=lambda i=i: self.player_move(i))
            btn.grid(row=(i // 3) + 1, column=i % 3)
            self.buttons.append(btn)

        # Przycisk resetu
        reset_btn = tk.Button(self.root, text="Zresetuj planszę", command=self.reset_game, bg="#f0f0f0")
        reset_btn.grid(row=4, column=0, columnspan=3, sticky="we", pady=10)

    def player_move(self, i):
        if self.board[i] == " ":
            self.make_move(i, self.human)
            if not self.check_game_over():
                self.root.after(300, self.ai_move)

    def ai_move(self):
        best_score = -float('inf')
        move = None

        # AI sprawdza każdy możliwy ruch i ocenia go Minimaxem
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.ai
                score = self.minimax(self.board, 0, False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    move = i

        if move is not None:
            self.make_move(move, self.ai)
            self.check_game_over()

    def minimax(self, board, depth, is_maximizing):
        # Sprawdzenie stanów końcowych (wygrana/przegrana/remis)
        if self.check_win(board, self.ai): return 10 - depth
        if self.check_win(board, self.human): return depth - 10
        if " " not in board: return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = self.ai
                    score = self.minimax(board, depth + 1, False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = self.human
                    score = self.minimax(board, depth + 1, True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def make_move(self, i, player):
        self.board[i] = player
        color = "#2563eb" if player == "X" else "#dc2626"
        self.buttons[i].config(text=player, state="disabled", disabledforeground=color)

    def check_win(self, b, p):
        win_coords = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        return any(b[x[0]] == b[x[1]] == b[x[2]] == p for x in win_coords)

    def check_game_over(self):
        if self.check_win(self.board, self.human):
            self.wins += 1
            self.end_round("Wygrałeś!")
            return True
        if self.check_win(self.board, self.ai):
            self.losses += 1
            self.end_round("AI wygrało!")
            return True
        if " " not in self.board:
            self.draws += 1
            self.end_round("Remis!")
            return True
        return False

    def end_round(self, msg):
        messagebox.showinfo("Koniec partii", msg)
        self.reset_game()

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for btn in self.buttons:
            btn.config(text=" ", state="normal")
        self.stats_label.config(text=f"Ty (X): {self.wins} | AI (O): {self.losses} | Remisy: {self.draws}")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeAI(root)
    root.mainloop()