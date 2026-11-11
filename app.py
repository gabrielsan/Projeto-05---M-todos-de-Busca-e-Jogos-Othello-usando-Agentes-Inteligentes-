import streamlit as st
from othello_game import OthelloGame
from agent_flow import game_instance, create_othello_agent

st.set_page_config(
    page_title="Othello IA - TP05",
    layout="centered"
)

st.title("🤖 Othello AI - GCC128 (Inteligência Artificial)")
st.sidebar.header("Configurações da Partida")

api_key = st.sidebar.text_input(
    "Chave Groq API",
    type="password"
)

mode = st.sidebar.selectbox(
    "Modo de Jogo",
    ["Humano vs Agente", "Agente vs Agente"]
)

if "game" not in st.session_state:
    st.session_state.game = game_instance

game = st.session_state.game

if st.sidebar.button("Reiniciar Jogo"):
    game.reset()
    st.rerun()

status = game.get_game_status()

# Placar
col1, col2, col3 = st.columns(3)

col1.metric("Peças Pretas (X)", status["x_count"])
col2.metric("Peças Brancas (O)", status["o_count"])
col3.metric("Turno Atual", status["current_player"])

if status["is_over"]:
    st.success(f"Fim de Jogo! Vencedor: {status['winner']}")
else:
    board = game.get_board_state()
    valid_moves = status["valid_moves"]

    st.write("### Tabuleiro Atual:")

    for r in range(8):
        cols = st.columns(8)
        for c in range(8):
            cell = board[r][c]
            label = cell if cell != '.' else '·'

            is_valid = (r, c) in valid_moves

            if (
                mode == "Humano vs Agente"
                and status["current_player"] == 'X'
                and is_valid
            ):
                if cols[c].button(
                    label,
                    key=f"btn_{r}_{c}",
                    use_container_width=True
                ):
                    game.make_move(r, c)
                    st.rerun()
            else:
                cols[c].markdown(
                    f"""
                    <div style="
                        width: 100%;
                        height: 38px;
                        background-color: #26734D;
                        border: 1px solid #16452E;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        color: white;
                        font-size: 22px;
                        font-weight: bold;
                    ">
                        {label}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # Execução do agente
    agent_turn = (
        mode == "Agente vs Agente"
        or (
            mode == "Humano vs Agente"
            and status["current_player"] == 'O'
        )
    )

    if agent_turn and not status["is_over"]:
        if api_key:
            if st.button("Fazer Jogada da IA"):
                with st.spinner("Agente analisando a jogada..."):
                    try:
                        agent = create_othello_agent(api_key)
                        # Chamada correta para o método play_turn()
                        resultado = agent.play_turn()
                        st.write(resultado)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro ao executar agente: {e}")
        else:
            st.warning(
                "Insira sua chave da API Groq "
                "na barra lateral para o agente jogar."
            )