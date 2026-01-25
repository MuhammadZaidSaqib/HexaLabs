# Name: Muhammad Zaid Saqib
# Reg No : B24F1722CYS084
# Section : CYS Green
# Date : 18/11/2025
# Lab No :11

# Lab Practise
'''
'''


#lab practice
# Task1: Implementing Alpha-Beta Pruning Algorithm
'''
def minimax(position, depth, is_maximizing):
    # terminal states
    if isinstance(position, int):
        return position

    if is_maximizing:
        best = float('-inf')
        for child in position:
            best = max(best, minimax(child, depth + 1, False))
        return best
    else:
        best = float('inf')
        for child in position:
            best = min(best, minimax(child, depth + 1, True))
        return best


# Bigger Example Game Tree
game = [
    [
        [3, 5, 2],    # branch 1.1
        [7, 9, 1],    # branch 1.2
        [8, 4, 6]     # branch 1.3
    ],
    [
        [3, 9, 1],    # branch 2.1
        [5, 2, 0],    # branch 2.2
        [6, 8, 4]     # branch 2.3
    ]
]

print("Minimax Value:", minimax(game, 0, True))


'''

# Task 2
'''
def alphabeta(position, depth, alpha, beta, is_maximizing):
    # terminal state: if leaf is an integer value
    if isinstance(position, int):
        return position

    # MAXIMIZING PLAYER
    if is_maximizing:
        best = float('-inf')
        for child in position:
            val = alphabeta(child, depth + 1, alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, best)

            # pruning
            if beta <= alpha:
                break
        return best

    # MINIMIZING PLAYER
    else:
        best = float('inf')
        for child in position:
            val = alphabeta(child, depth + 1, alpha, beta, True)
            best = min(best, val)
            beta = min(beta, best)

            # pruning
            if beta <= alpha:
                break
        return best


# SAME GAME TREE USED IN MINIMAX EXAMPLE
game = [
    [
        [3, 5, 2],      # branch 1.1
        [9, 1],         # branch 1.2
        [8, 6]          # branch 1.3
    ],
    [
        [3, 9],         # branch 2.1
        [5, 2, 0],      # branch 2.2
        [6, 8, 4]       # branch 2.3
    ]
]

print("Alpha-Beta Value:", alphabeta(game, 0, float('-inf'), float('inf'), True))
'''


# Lab Tasks

# Task 1
#Trace the given game tree using Minimax and determine the optimal move for MAX.
#Hint: Start from leaf nodes and propagate values up, choosing max at MAX levels and min at MIN level
'''
tree = [
    [ [3, 5], [2, 9] ],   # N1 -> N11 (3,5), N12 (2,9)
    [ [0, 6], [7, 4] ],   # N2 -> N21 (0,6), N22 (7,4)
    [ [5, 1], [2, 8] ]    # N3 -> N31 (5,1), N32 (2,8)
]

def minimax(node, is_maximizing):
    # terminal node (leaf)
    if isinstance(node, int):
        return node
    # non-terminal: node is a list of children
    if is_maximizing:
        best = float('-inf')
        for child in node:
            val = minimax(child, False)
            if val > best:
                best = val
        return best
    else:  # minimizing level
        best = float('inf')
        for child in node:
            val = minimax(child, True)
            if val < best:
                best = val
        return best

# Compute minimax value for each top-level branch (N1, N2, N3)
top_values = []
for i, branch in enumerate(tree, start=1):
    val = minimax(branch, False)  # children of root are MIN nodes
    top_values.append(val)
    print(f"N{i} minimax value = {val}")

# Root is MAX: choose branch with highest value
best_value = max(top_values)
best_branch = top_values.index(best_value) + 1  # 1-based index for N1,N2,...
print(f"Optimal move for MAX: choose N{best_branch} with value = {best_value}")
'''

#Task 02:
#Implement Minimax for a number-picking game where players pick numbers from either end of a list.
#Hint: Use recursion to simulate both players’ turns and return the optimal score and move sequence for MAX.
'''
def minimax(nums, left, right, is_maximizing):
    # base case: only one number left
    if left == right:
        return nums[left], [nums[left]]

    if is_maximizing:
        # MAX's turn: choose the best option
        pick_left_score, pick_left_seq = minimax(nums, left + 1, right, False)
        pick_right_score, pick_right_seq = minimax(nums, left, right - 1, False)

        if nums[left] + pick_left_score > nums[right] + pick_right_score:
            return nums[left] + pick_left_score, [nums[left]] + pick_left_seq
        else:
            return nums[right] + pick_right_score, [nums[right]] + pick_right_seq
    else:
        # MIN's turn: choose the worst option for MAX
        pick_left_score, _ = minimax(nums, left + 1, right, True)
        pick_right_score, _ = minimax(nums, left, right - 1, True)

        if pick_left_score < pick_right_score:
            return pick_left_score, []
        else:
            return pick_right_score, []
# Example number list
numbers = [3, 9, 1, 2]
optimal_score, move_sequence = minimax(numbers, 0, len(numbers) - 1, True)
print(f"Optimal score for MAX: {optimal_score}")
print(f"Move sequence for MAX: {move_sequence}")

'''

#Task 03:
#Implement Minimax with Alpha-Beta pruning for the given tree and compare visited nodes with regular Minimax.
#Hint: Maintain alpha for MAX and beta for MIN; prune branches where possible to reduce computation.

'''
from math import inf
tree = [
    [[3, 5], [2, 9], [1, 7]],   # N1
    [[4, 6], [8, 2], [0, 5]],   # N2
    [[7, 3], [6, 1]]            # N3
]

# Counters
visited_minimax = 0
visited_alphabeta = 0
pruned_count = 0

def minimax(node, is_maximizing):
    global visited_minimax
    visited_minimax += 1  # count this node visit
    # terminal
    if isinstance(node, int):
        return node
    if is_maximizing:
        best = -inf
        for child in node:
            val = minimax(child, False)
            if val > best:
                best = val
        return best
    else:
        best = inf
        for child in node:
            val = minimax(child, True)
            if val < best:
                best = val
        return best

def alphabeta(node, alpha, beta, is_maximizing):
    global visited_alphabeta, pruned_count
    visited_alphabeta += 1  # count this node visit
    # terminal
    if isinstance(node, int):
        return node
    if is_maximizing:
        value = -inf
        for i, child in enumerate(node):
            val = alphabeta(child, alpha, beta, False)
            value = max(value, val)
            alpha = max(alpha, value)
            if alpha >= beta:
                # remaining children are pruned
                pruned_count += len(node) - (i + 1)
                break
        return value
    else:
        value = inf
        for i, child in enumerate(node):
            val = alphabeta(child, alpha, beta, True)
            value = min(value, val)
            beta = min(beta, value)
            if alpha >= beta:
                pruned_count += len(node) - (i + 1)
                break
        return value

# --- Run Minimax (count visits) per top branch ---
visited_minimax = 0
minimax_top_values = []
for idx, branch in enumerate(tree, start=1):
    val = minimax(branch, False)  # children of root are MIN nodes
    minimax_top_values.append(val)
    print(f"N{idx} minimax value = {val}")
best_val_minimax = max(minimax_top_values)
best_branch_minimax = minimax_top_values.index(best_val_minimax) + 1
print(f"Minimax: Optimal move = N{best_branch_minimax} with value = {best_val_minimax}")
print(f"Minimax visited nodes: {visited_minimax}\n")

# --- Run Alpha-Beta (count visits and prunes) per top branch ---
visited_alphabeta = 0
pruned_count = 0
ab_top_values = []
for idx, branch in enumerate(tree, start=1):
    val = alphabeta(branch, -inf, inf, False)
    ab_top_values.append(val)
    print(f"N{idx} alpha-beta value = {val}")
best_val_ab = max(ab_top_values)
best_branch_ab = ab_top_values.index(best_val_ab) + 1
print(f"Alpha-Beta: Optimal move = N{best_branch_ab} with value = {best_val_ab}")
print(f"Alpha-Beta visited nodes: {visited_alphabeta}")
print(f"Alpha-Beta pruned leaf/branch visits: {pruned_count}")

'''

#Task 04:
#Develop an AI player for Tic-Tac-Toe using Minimax or Alpha-Beta pruning to always make optimal moves.
#Hint: Represent the board as a list, simulate game moves recursively, and make the AI block wins or choose winning moves.
'''
import math

AI = "X"
HUMAN = "O"
EMPTY = " "

WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diags
]

def print_board(board):
    for r in range(0, 9, 3):
        print(" | ".join(board[r:r+3]))
        if r < 6:
            print("-" * 9)

def check_winner(board):
    for a, b, c in WIN_COMBOS:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    if EMPTY not in board:
        return "DRAW"
    return None

def minimax(board, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == AI:
        return 1, None
    if winner == HUMAN:
        return -1, None
    if winner == "DRAW":
        return 0, None

    if is_maximizing:
        best_score = -math.inf
        best_move = None
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score, _ = minimax(board, False, alpha, beta)
                board[i] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = i
                alpha = max(alpha, best_score)
                if alpha >= beta:
                    break
        return best_score, best_move
    else:
        best_score = math.inf
        best_move = None
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score, _ = minimax(board, True, alpha, beta)
                board[i] = EMPTY
                if score < best_score:
                    best_score = score
                    best_move = i
                beta = min(beta, best_score)
                if alpha >= beta:
                    break
        return best_score, best_move

def get_ai_move(board):
    _, move = minimax(board, True, -math.inf, math.inf)
    return move

def play():
    board = [EMPTY] * 9
    current = HUMAN  # human starts; change to AI to let AI start
    print("Positions are 1..9 left-to-right, top-to-bottom")
    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == "DRAW":
                print("Game ended in a draw.")
            else:
                print(f"{winner} wins!")
            break

        if current == HUMAN:
            try:
                pos = int(input("Your move (1-9): ")) - 1
                if pos < 0 or pos > 8 or board[pos] != EMPTY:
                    print("Invalid move. Try again.")
                    continue
                board[pos] = HUMAN
            except ValueError:
                print("Enter a number 1-9.")
                continue
            current = AI
        else:
            move = get_ai_move(board)
            if move is None:
                # no moves left
                current = HUMAN
                continue
            board[move] = AI
            print(f"AI moves to {move + 1}")
            current = HUMAN

if __name__ == "__main__":
    play()
    '''

# Conclusion:
'''
In this lab, I learned how decision-making algorithms work in game theory and how they help an AI choose the best possible move. 
I started with the basic Minimax algorithm, where I practiced tracing a game tree manually and then implemented it in Python. 
This helped me understand how values propagate from the leaf nodes to the top by taking the maximum at MAX levels and minimum at MIN levels.
Next, I applied Minimax to a number-picking game, which strengthened my understanding of recursion and how two players can be simulated by alternating
 maximizing and minimizing turns. I also learned how to return not only the final score but also the move sequence that leads to the optimal result.
In Task 3, I implemented Alpha-Beta pruning, which improved the Minimax algorithm by cutting off unnecessary branches. This reduced the number of
visited nodes and showed how pruning makes game-search algorithms much more efficient. Comparing visited nodes in Minimax and Alpha-Beta gave me 
a practical understanding of the performance improvement.
Finally, in Task 4, I used these concepts to build a complete Tic-Tac-Toe AI that always plays optimally. By integrating Minimax with Alpha-Beta 
pruning, the AI was able to block the opponent, choose winning moves, and avoid losing positions. This task helped me understand real-world usage 
of search algorithms in games.
Overall, these tasks improved my skills in recursion, tree search, optimal decision-making, and algorithm optimization. I also learned how 
classical AI techniques are used to build intelligent game agents.

'''
