class TicTacToe:

    def checkWinner(self, board: list[list[str]]) -> str:

        board_start = 0
        board_end = len(board) - 1

        #Check if all give values are the same and not empty tiles.
        def checkValues(values: list[str]) -> str:
            if values[0] != "" and all(v == values[0] for v in values):
                return values[0]
            return ""
        
        #Vertical
        for col in range(0, len(board)):
            value = checkValues([row[col] for row in board])
            if value != "":
                return value
            
        #Horizontal
        for row in board:
            value = checkValues(row)
            if value != "":
                return value
            
        #Diagonal
        value = checkValues([board[0][0],board[1][1],board[2][2],board[3][3]])
        if value != "":
            return value
        
        value = checkValues([board[0][3],board[1][2],board[2][1],board[3][0]])
        if value != "":
            return value

        #Corners
        value = checkValues([board[board_start][board_start],board[board_start][board_end],board[board_end][board_start],board[board_end][board_end]])
        if value != "":
            return value
        #Boxes
        for i in range(board_start, board_end-1):
            for j in range(board_start, board_end-1):
                value = checkValues([board[i][j],board[i+1][j],board[i][j+1],board[i+1][j+1]])
                if value != "":
                    return value
        
        #No winner found
        return ""

    def anyMovesLeft(self, board: list[list[str]]) -> bool:
        for row in board:
            for element in row:
                if element == "":
                    return True
        return False

    def isGameOver(self, board: list[list[str]]) -> bool:

        winner = self.checkWinner(board)

        if winner != "":
            print(winner + "'s Win!")
            return True
        elif winner == "" and not self.anyMovesLeft(board):
            print("Its a tie!")
            return True
        else:
            return False

