# encoding: utf-8
import pytest
import allure
import yaml
import os
from utils import get_file_path


@pytest.fixture(scope="session", autouse=True)
def env_config(request):
    """
    读取yaml配置文件
    """
    rootPath = get_file_path.get_root_path()
    config_path = os.path.abspath(rootPath + 'config\\env_config.yaml')
    with open(config_path) as f:
        env_config = yaml.load(f)  # 读取配置文件
    return env_config


