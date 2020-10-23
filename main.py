import pytest
import subprocess

if __name__ == '__main__':
    pytest.main(['--html=./test.html'])
    subprocess.run('allure generate ./test.html -o ./report/ --clean')
