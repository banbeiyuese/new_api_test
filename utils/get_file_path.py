# encoding: utf-8

import os

project_name = "api_test"


def get_root_path():
    """
    获取根路径
    """
    cur_path = os.path.abspath(os.path.dirname(__file__))
    root_path = cur_path[:cur_path.find(project_name + "\\") + len(project_name + "\\")]  # 获取myProject，也就是项目的根路径
    return root_path


if __name__ == '__main__':
    print(get_root_path())
