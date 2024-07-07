# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 21:34:28 2024

@author: User
"""

class TicTacToe:
    def __init__(self):
        self.board = {str(num): ' ' for num in range(1, 10)}
        self.current_player = 'X'
        self.winner = None

    def display_board(self):
        board = self.board
        print(f"{board['1']} | {board['2']} | {board['3']}")
        print("--+---+--")
        print(f"{board['4']} | {board['5']} | {board['6']}")
        print("--+---+--")
        print(f"{board['7']} | {board['8']} | {board['9']}")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Position already taken. Try again.")

    def check_winner(self):
        b = self.board
        winning_combinations = [
            ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],  # Horizontal
            ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],  # Vertical
            ['1', '5', '9'], ['3', '5', '7']  # Diagonal
        ]
        for combo in winning_combinations:
            if b[combo[0]] == b[combo[1]] == b[combo[2]] != ' ':
                return True
        return False

    def is_tie(self):
        return ' ' not in self.board.values()

    def play_game(self):
        while not self.winner and not self.is_tie():
            self.display_board()
            move = input(f"Player {self.current_player}, enter your move (1-9): ")
            if move in self.board.keys() and self.board[move] == ' ':
                self.make_move(move)
            else:
                print("Invalid move. Please enter a number between 1 and 9 that has not been taken.")
        
        self.display_board()
        if self.winner:
            print(f"Player {self.winner} wins!")
        else:
            print("It's a tie!")


game = TicTacToe()
game.play_game()
