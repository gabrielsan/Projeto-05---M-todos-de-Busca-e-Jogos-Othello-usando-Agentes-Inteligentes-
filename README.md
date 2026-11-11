# 🤖 Othello AI - GCC128 (Inteligência Artificial)

Trabalho Prático 05 desenvolvido para a disciplina de Inteligência Artificial (GCC128) da Universidade Federal de Lavras (UFLA). O projeto consiste na implementação de um **Agente Inteligente Autónomo** capaz de jogar Othello (Reversi) num tabuleiro $8\times8$, utilizando Modelos de Linguagem de Grande Escala (LLMs) integrados via **LangChain** e a API da **Groq**.

---

## 📋 Requisitos Atendidos

* **Regras Completas do Othello:** Tabuleiro $8\times8$, verificação de jogadas válidas, captura/inversão de peças nas 8 direções e deteção de fim de partida (vitória, derrota ou empate).
* **Agente Autónomo com LLM:** Integração do modelo `openai/gpt-oss-20b` via `ChatGroq` para analisar o estado do tabuleiro e escolher jogadas válidas.
* **Ferramentas (Tools) e Estado:** Exposição dos métodos `get_board_state()`, `get_valid_moves()`, `make_move()` e `get_game_status()` para interação do agente com o ambiente.
* **Modos de Jogo:** Suporte para partidas **Humano vs Agente** e **Agente vs Agente**.
* **Interface Interativa:** Aplicação web desenvolvida com **Streamlit** contendo tabuleiro dinâmico, placar em tempo real e controlos de partida.

---

## 📂 Estrutura do Projeto

```text
TrabalhoPratico05/
├── othello_game.py   # Lógica do jogo, regras do Othello, validação e inversão de peças
├── agent_flow.py     # Arquitetura do agente LLM (ChatGroq), prompt e parser JSON com fallback
├── app.py            # Interface gráfica em Streamlit e gestão de sessão
└── README.md         # Documentação e instruções de execução
```

---

## ⚙️ Pré-requisitos e Instalação

Certifique-se de ter o **Python 3.10 ou superior** instalado na sua máquina.

1. **Abra o terminal** na pasta raiz do projeto.
2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```
3. **Instale as dependências necessárias:**
   ```bash
   pip install streamlit langchain langchain-groq
   ```
4. **Obtenha uma chave de API:** Crie uma conta gratuita em [console.groq.com](https://console.groq.com/) e gere uma **API Key**.

---

## 🚀 Como Executar e Testar

1. **Inicie a aplicação Streamlit** executando o comando abaixo no terminal:
   ```bash
   streamlit run app.py
   ```

2. **Aceda à interface:** O navegador abrirá automaticamente em `http://localhost:8501`.

3. **Configure a partida na barra lateral (Sidebar):**
   * Cole a sua **Chave Groq API** no campo indicado e pressione `Enter`.
   * Selecione o **Modo de Jogo** desejado:
     * **Humano vs Agente:**
       * Você controla as **Peças Pretas (`X`)**. As casas onde pode jogar aparecem como botões clicáveis no tabuleiro.
       * Após a sua jogada, o turno passa para as **Peças Brancas (`O`)** (IA). Clique no botão **"Fazer Jogada da IA"** para o agente analisar o tabuleiro e executar o movimento.
     * **Agente vs Agente:**
       * Ambos os jogadores são controlados pela IA. Clique em **"Fazer Jogada da IA"** a cada turno para observar o confronto autónomo entre os agentes e recolher métricas de desempenho.

4. **Reiniciar a Partida:**
   * A qualquer momento, clique no botão **"Reiniciar Jogo"** na barra lateral para limpar o tabuleiro e iniciar uma nova partida.

---

## 🛡️ Tratamento de Erros e Segurança

Para evitar que respostas inesperadas da LLM interrompam a execução da partida, o `agent_flow.py` implementa uma camada de validação via Expressões Regulares (`regex`) para extrair o objeto JSON (`{"row": r, "col": c}`). Caso o modelo retorne um formato inválido ou uma coordenada fora da lista de jogadas permitidas, um mecanismo de *fallback* seleciona automaticamente uma jogada válida disponível.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **LangChain** (`langchain-groq`)
* **Groq Cloud API** (`openai/gpt-oss-20b`)
* **Streamlit**
