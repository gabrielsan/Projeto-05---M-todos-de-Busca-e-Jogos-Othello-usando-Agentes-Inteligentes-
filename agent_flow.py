from langchain_groq import ChatGroq
from othello_game import OthelloGame
import json
import re

game_instance = OthelloGame()

class OthelloAgentDirect:
    def __init__(self, api_key: str):
        self.llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0, api_key=api_key)

    def play_turn(self) -> str:
        board = game_instance.get_board_state()
        board_str = "\n".join([" ".join(row) for row in board])
        valid_moves = game_instance.get_valid_moves()
        
        if not valid_moves:
            return "Não há jogadas válidas disponíveis."

        prompt = f"""
        Você é um agente especialista no jogo Othello (Reversi).
        Estado atual do tabuleiro (8x8):
        {board_str}

        Suas jogadas válidas atuais no formato (linha, coluna) são: {valid_moves}

        Responda estritamente com um objeto JSON puro contendo a linha e a coluna escolhidas da lista acima. 
        Exemplo exato do formato esperado:
        {{"row": {valid_moves[0][0]}, "col": {valid_moves[0][1]}}}
        """

        try:
            response = self.llm.invoke(prompt)
            content = response.content
            
            match = re.search(r'\{.*?\}', content, re.DOTALL)
            if match:
                data = json.loads(match.group(0))
                r, c = int(data["row"]), int(data["col"])
                if (r, c) not in valid_moves:
                    r, c = valid_moves[0]
            else:
                r, c = valid_moves[0]

            success = game_instance.make_move(r, c)
            if success:
                return f"Jogada realizada com sucesso em ({r}, {c})."
            else:
                r, c = valid_moves[0]
                game_instance.make_move(r, c)
                return f"Movimento alternativo executado em ({r}, {c})."
        except Exception as e:
            r, c = valid_moves[0]
            game_instance.make_move(r, c)
            return f"Jogada automática de segurança em ({r}, {c})."

def create_othello_agent(api_key: str):
    return OthelloAgentDirect(api_key)