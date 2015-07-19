# coding:utf-8

import db


problem_db_file = 'problem.db.txt'
# 创建一个存取数据的文本文件

def load():
    return db.load(problem_db_file)


def save(data):
    db.save(data, problem_db_file)


def save_solution_db_file(problem_id, data):
    solution_db_file = 'problem_' + str(problem_id) + '_solution.db.txt'
    db.save(data, solution_db_file)


def load_solution_db_file(problem_id):
    solution_db_file = 'problem_' + str(problem_id) + '_solution.db.txt'
    return db.load(solution_db_file)
