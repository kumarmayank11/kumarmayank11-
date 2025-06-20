import json
import random

BOARD_SIZE = 10
STATE_FILE = 'snake_state.json'

def load_state():
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except:
        return {"snake": [[5, 5]], "dir": [0, 1]}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def move_snake(state):
    snake = state["snake"]
    direction = state["dir"]
    head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    
    # Wrap around
    head = [head[0] % BOARD_SIZE, head[1] % BOARD_SIZE]
    snake.insert(0, head)
    snake.pop()  # Remove tail

    state["snake"] = snake
    return state

def draw_board(state):
    board = [["⬛"] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    for x, y in state["snake"]:
        board[x][y] = "🟩"
    return "\n".join("".join(row) for row in board)

def main():
    state = load_state()
    state = move_snake(state)
    save_state(state)

    board = draw_board(state)
    with open("README.md", "w") as f:
        f.write("# 🐍 Snake Game\n\n")
        f.write(board + "\n")

if __name__ == "__main__":
    main()
