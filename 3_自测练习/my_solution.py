# n皇后问题是指在n×n的棋盘上，放置n个皇后，使其不能互相攻击，问共有多少种摆法。
def solve_n_queens(n):
    grid = [['X' for _ in range(n)] for _ in range(n)]  # 初始化n*n网格棋盘
    res = []  # 结果存放

    # 回溯法求解n后问题
    def dfs(u):
        if u == n:  # 当u==n时，已经放入n个皇后，得到一个解
            temp = []  # 记录一个解的盘面。每个元素是一行棋盘。用'Q'表示放置了皇后，用'X'表示没有放置皇后
            for i in range(n):
                cur = ''
                for j in range(n):
                    cur += grid[i][j]
                temp.append(cur)
            res.append(temp)
            return

        else:  # 当 u < n 表示该分支的棋盘还没有放置完，需要继续放置皇后
            raise NotImplementedError('编写剪枝条件，并在不满足剪枝条件为时,对该分支继续进行深度搜索')

    dfs(0)
    return res


if __name__ == '__main__':
    pass
