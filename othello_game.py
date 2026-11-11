class OthelloGame:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.board = [['.' for _ in range(8)] for _ in range(8)]
        # Posições iniciais centrais
        self.board[3][3] = 'O'
        self.board[3][4] = 'X'
        self.board[4][3] = 'X'
        self.board[4][4] = 'O'
        self.current_player = 'X' # 'X' = Preto (primeiro), 'O' = Branco
        
    def get_board_state(self):
        return self.board
    
    def get_valid_moves(self, player=None):
        if player is None:
            player = self.current_player
        opponent = 'O' if player == 'X' else 'X'
        valid_moves = []
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        for r in range(8):
            for c in range(8):
                if self.board[r][c] != '.':
                    continue
                is_valid = False
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    found_opponent = False
                    while 0 <= nr < 8 and 0 <= nc < 8 and self.board[nr][nc] == opponent:
                        found_opponent = True
                        nr += dr
                        nc += dc
                    if found_opponent and 0 <= nr < 8 and 0 <= nc < 8 and self.board[nr][nc] == player:
                        is_valid = True
                        break
                if is_valid:
                    valid_moves.append((r, c))
        return valid_moves

    def make_move(self, r, c, player=None):
        if player is None:
            player = self.current_player
        valid_moves = self.get_valid_moves(player)
        if (r, c) not in valid_moves:
            return False
        
        opponent = 'O' if player == 'X' else 'X'
        self.board[r][c] = player
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            to_flip = []
            while 0 <= nr < 8 and 0 <= nc < 8 and self.board[nr][nc] == opponent:
                to_flip.append((nr, nc))
                nr += dr
                nc += dc
            if to_flip and 0 <= nr < 8 and 0 <= nc < 8 and self.board[nr][nc] == player:
                for fr, fc in to_flip:
                    self.board[fr][fc] = player
                    
        self.current_player = opponent
        if not self.get_valid_moves(self.current_player):
            self.current_player = player
            if not self.get_valid_moves(self.current_player):
                pass # Fim de jogo
        return True

    def get_game_status(self):
        x_count = sum(row.count('X') for row in self.board)
        o_count = sum(row.count('O') for row in self.board)
        empty_count = sum(row.count('.') for row in self.board)
        valid_current = self.get_valid_moves(self.current_player)
        opponent = 'O' if self.current_player == 'X' else 'X'
        valid_opponent = self.get_valid_moves(opponent)
        is_over = (empty_count == 0) or (not valid_current and not valid_opponent)
        
        winner = None
        if is_over:
            if x_count > o_count: winner = 'X'
            elif o_count > x_count: winner = 'O'
            else: winner = 'Empate'
            
        return {
            "x_count": x_count,
            "o_count": o_count,
            "empty_count": empty_count,
            "current_player": self.current_player,
            "is_over": is_over,
            "winner": winner,
            "valid_moves": valid_current
        }