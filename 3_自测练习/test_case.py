#!/usr/bin/env python3

from my_solution import solve_n_queens


# 测试用例
def test_solution():
    queen_num = 4
    # 正确答案
    correct_solution = [['XQXX', 'XXXQ', 'QXXX', 'XXQX'],
                        ['XXQX', 'QXXX', 'XXXQ', 'XQXX']]
    # 程序求解结果
    result = solve_n_queens(queen_num)
    assert correct_solution == result