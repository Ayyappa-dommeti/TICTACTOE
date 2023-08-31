import tkinter as tk

from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.board = [["","",""],["","",""],["","",""]]
        self.current_player="X"
        self.window = tk.Tk()
        self.window.title("TIC TAC TOE")

        self.buttonsGrid = []

        for i in range(3):
            row=[]
            for j in range(3):
                button = tk.Button(self.window,text="",width=20,height=10,command = lambda i=i,j=j:self.start_game(i,j))
                button.grid(row=i,column=j)
                row.append(button)

            self.buttonsGrid.append(row)

    def start_game(self,row,column):
        if self.board[row][column] == "":
            self.board[row][column] = self.current_player
            self.buttonsGrid[row][column].config(text=self.current_player)

            if self.is_winner(self.current_player):
                messagebox.showinfo("game finished","winner is " + self.current_player)   
                self.window.quit()                     

            elif self.is_draw():
                messagebox.showinfo("game finished","draw")
                self.window.quit()  
            else:
                self.current_player="O" if self.current_player=="X" else "X"

    def is_winner(self,player):
        for i in range(3):
            if player == self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True  

            if player == self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True 

        if player == self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return True 

        if player == self.board[0][2] == self.board[1][1] == self.board[2][2]:
            return True 
        
        return False  

    def is_draw(self):

        for r in self.board: 
            if "" in r: 
                return False     
            
        return True



    def run(self):
        self.window.mainloop() 


game = TicTacToe()

game.run()