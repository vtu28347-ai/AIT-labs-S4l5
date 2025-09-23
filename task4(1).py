def alpha_beta_pruning(depth, index_node, maximizing_player, values, alpha, beta):
    # Base case: leaf node or depth limit reached
    if depth == 0 or index_node >= len(values):
        return values[index_node]

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(2):
            eval = alpha_beta_pruning(depth - 1, index_node * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            eval = alpha_beta_pruning(depth - 1, index_node * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


if __name__ == "__main__":
    values = [7, 3, 4, 2, 6, 4, 0, -3]
    depth = 3
    alpha = float('-inf')
    beta = float('inf')
    optimal_value = alpha_beta_pruning(depth, 0, True, values, alpha, beta)
    print(f"The optimal value is: {optimal_value}")
