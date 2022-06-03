# n皇后问题是指在n×n的棋盘上，放置n个皇后，使其不能互相攻击，问共有多少种摆法。
def solve_n_queens(n):
    grid = [['X' for _ in range(n)] for _ in range(n)]  # 初始化n*n网格棋盘

    col = [False] * n  # 标记列是否放过
    dg = [False] * (2 * n)  # 标记对角线是否放过
    udg = [False] * (2 * n)  # 标记反对角线是否放过

    res = []  # 结果存放

    # 回溯法求解n后问题
    def dfs(u):
        if u == n:  # 当u==n时，已经放入n个皇后，得到一个解
            temp = []  # 记录一个解。每个元素是一行棋盘。用'Q'表示放置了皇后，用'X'表示没有放置皇后
            for i in range(n):
                cur = ''
                for j in range(n):
                    cur += grid[i][j]
                temp.append(cur)
            res.append(temp)
            return

        else:  # 当 u < n 表示该分支的棋盘还没有放置完，需要继续放置皇后
            for i in range(n):  # 遍历每个位置的分支
                if not col[i] and not dg[u + i] and not udg[n - u +
                                                            i]:  # 如果不满足剪枝条件
                    col[i] = dg[u + i] = udg[n - u + i] = True  # 标记
                    grid[u][i] = 'Q'  # 放置皇后
                    dfs(u + 1)  # 深度搜索下一层
                    col[i] = dg[u + i] = udg[n - u + i] = False  # 回溯并复位
                    grid[u][i] = 'X'

    dfs(0)
    return res


if __name__ == '__main__':
    print(solve_n_queens(4))
