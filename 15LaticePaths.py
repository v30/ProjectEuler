def lattice_paths_of_n(n):
    dp = [[1] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[n][n]

print(lattice_paths_of_n(20))  # Example for a 20x20 grid