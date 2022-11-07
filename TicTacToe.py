# Tic-Tac-Toe Game
import random
from tkinter import messagebox


class Game:
    def __init__(self):
        self.dict={'1': ' ',
                   '2': ' ',
                   '3': ' ',
                   '4': ' ',
                   '5': ' ',
                   '6': ' ',
                   '7': ' ',
                   '8': ' ',
                   '9': ' '}

    def printBoard(self):
        print(self.dict['1'] + "|" + self.dict['2'] + "|" + self.dict['3'])
        print('-+-+-')
        print(self.dict['4'] + "|" + self.dict['5'] + "|" + self.dict['6'])
        print('-+-+-')
        print(self.dict['7'] + "|" + self.dict['8'] + "|" + self.dict['9'])

    def update(self, target, symbol):
        self.dict[target]=symbol

    def win(self):
        if self.dict['1']==self.dict['2']==self.dict['3']:
            return self.dict['1']
        if self.dict['4']==self.dict['5']==self.dict['6']:
            return self.dict['4']
        if self.dict['7']==self.dict['8']==self.dict['9']:
            return self.dict['7']
        if self.dict['1']==self.dict['4']==self.dict['7']:
            return self.dict['1']
        if self.dict['2']==self.dict['5']==self.dict['8']:
            return self.dict['2']
        if self.dict['3']==self.dict['6']==self.dict['9']:
            return self.dict['3']
        if self.dict['1']==self.dict['5']==self.dict['9']:
            return self.dict['1']
        if self.dict['3']==self.dict['5']==self.dict['7']:
            return self.dict['3']

    @staticmethod
    def message(winner):
        messagebox.showinfo("Winner", "Player "+winner+" won the match.")
        print("\nPlayer "+winner+" won the match.")


if __name__=='__main__':
    game=Game()
    game.printBoard()
    print("9 boxes are represented by numbers 1-9 from top-left to bottom-right")
    toss=random.randint(0, 1)
    turn="X" if toss==0 else "O"

    run=9
    draw=True
    while run>0:
        print(f"It's {turn}'s turn.\nEnter box number")
        move=input()
        game.update(move, turn)  # Update the Game Table
        game.printBoard()
        if run<6:
            win=game.win()
            if win=='X' or win=='O':  # Check if there's a winning situation
                game.message(win)
                draw=False
                break

        turn="X" if turn=="O" else "O"
        run-=1

    if draw:
        messagebox.showinfo("Draw", "Match drawn")
        print("\nMatch drawn...")
